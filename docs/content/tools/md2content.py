"""Turns the course drafts (docs/content/v5) into the site's lesson folders (content/learn).

A draft is one markdown file per lesson: its objectives, then `## Step N: Title` sections, each
with a `Kind:` line, the step's text, and labelled code blocks (Start, Solution, Output, a file's
path). This writes each step as the site reads it: `step.md` (front matter and text), `start/` and
`solution/` projects, and `expected.txt`.

The step's text is copied as it is, never reworded. Anything the converter can't place, such as a
label it doesn't know or text between code blocks, stops it with the lesson and step named.

Usage:
    python3 md2content.py [--check] [--api URL] [--out DIR]
--check reports what it would write without writing. --api runs, through the site's API, each step
that records no output of its own (a step whose tests are the point), to fill its expected.txt.
"""
import glob
import json
import os
import re
import shutil
import sys
import time
import urllib.request
from dataclasses import dataclass, field

HERE = os.path.dirname(os.path.abspath(__file__))
DRAFTS = os.path.join(HERE, "..", "v5")
OUTLINE = os.path.join(HERE, "..", "outline.md")
REPO = os.path.join(HERE, "..", "..", "..")

# Files a lesson takes from a step of another lesson, which its text names in words ("the package
# `geometry`, as in Visibility") rather than showing again.
BORROWED = {"11.3": [("11.2", 2, "lugha.toml")]}

FENCE = re.compile(r"^```(\w*)[^\n]*\n(.*?)^```[ \t]*\n?", re.S | re.M)
LABEL = re.compile(r"^(Start\b|Solution\b|Output\b|Tests\b|Lines \d|`(src|test)/[^`]+`|`lugha\.toml`).*:$")
# A label giving a result in words, with no block after it: "Tests (solution): `ok`, ...".
RESULT = re.compile(r"^(Tests|Output)\b[^:]*\): \S")
PATH = re.compile(r"`((?:src|test)/[\w/]+\.la|lugha\.toml)`")
DIAGRAM = re.compile(r'^Diagram: v4\'s `([^`]+)`, kept \(alt "([^"]+)"\)\.$', re.M)


class ConvertError(Exception):
    """Something in a draft the converter can't place."""


@dataclass
class Kind:
    fix: bool
    test: bool
    error: str | None = None
    prints: bool = False
    silent: bool = False
    failing: list = field(default_factory=list)


@dataclass
class Step:
    n: int
    title: str
    kind: Kind
    prose: str
    material: str


@dataclass
class Lesson:
    num: str
    title: str
    slug: str
    head: str
    steps: list
    done: dict = field(default_factory=dict)


@dataclass
class Converted:
    n: int
    title: str
    front: dict
    text: str
    start: dict
    solution: dict | None
    expected: str | None
    diagrams: list
    carried: list


def slug(title):
    """Gives a folder name for a title: lower case, words joined by hyphens."""
    return re.sub(r"[^a-z0-9]+", "-", re.sub(r"['’]", "", title.lower())).strip("-")


def parse_kind(text):
    """Reads a step's `Kind:` line, without the `Kind: ` in front."""
    if text.startswith("read"):
        return Kind(fix=False, test="(Test" in text)
    if not text.startswith("fix"):
        raise ConvertError(f"unknown Kind: {text}")
    k = Kind(fix=True, test="Test" in text)
    if "start gives" in text:
        m = re.search(r"E\d{4}", text.split("start gives", 1)[1])
        k.error = m.group(0) if m else None
    k.failing = re.findall(r"`(\w+)` fails", text)
    # A start that neither fails to compile nor fails a test runs: "prints …", "runs with warnings …".
    k.prints = k.error is None and not k.failing
    # A start described only by what it writes to stderr prints nothing.
    k.silent = "no stdout" in text or "stderr `" in text
    return k


def parse_lesson(name, text):
    """Reads one draft file: its title and its steps, without the Notes."""
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S).split("\n## Notes")[0]
    # A lesson split across two files says where it goes on; that line is about the drafts.
    text = re.sub(r"^Steps \d+ to \d+ and the notes continue in `[^`]+`.*\n", "", text, flags=re.M)
    first = text.split("\n", 1)[0]
    m = re.match(r"# (\d+\.\d+) (.+?) \(v5", first)
    if not m:
        raise ConvertError(f"{name}: the first line isn't `# N.N Title (v5, …)`")
    head, *chunks = re.split(r"^## Step ", text, flags=re.M)
    steps = []
    for chunk in chunks:
        title_line, body = chunk.split("\n", 1)
        n, title = title_line.split(": ", 1)
        km = re.match(r"Kind: (.*)\n", body)
        if not km:
            raise ConvertError(f"{m.group(1)} step {n}: no Kind line")
        prose, material = split_prose(body[km.end():])
        steps.append(Step(int(n), title.strip(), parse_kind(km.group(1)), prose, material))
    lesson_slug = re.sub(r"^\d+\.\d+-|(-2)?\.md$", "", os.path.basename(name))
    return Lesson(m.group(1), m.group(2), lesson_slug, head, steps)


def split_prose(body):
    """Splits a step's body into its text and what follows: the labelled code blocks."""
    lines = body.rstrip("\n").split("\n")
    for i, line in enumerate(lines):
        nxt = next((l for l in lines[i + 1:] if l.strip()), "")
        if line.startswith("```") or (LABEL.match(line) and nxt.startswith("```")) or RESULT.match(line):
            return "\n".join(lines[:i]).strip("\n").rstrip(), "\n".join(lines[i:]) + "\n"
    return body.strip(), ""


def label_role(label):
    """Reads a code block's label: (start, solution or both; its path; first line; a file from another step)."""
    lower = label.lower()
    if "start and solution" in lower:
        role = "both"
    elif lower.startswith("start"):
        role = "start"
    elif lower.startswith("solution"):
        role = "solution"
    else:
        role = "both"
    rng = re.search(r"[Ll]ines? (\d+) to \d+", label)
    ref = re.search(r"`((?:src|test)/[\w/]+\.la|lugha\.toml)` as in step (\d+)", label)
    bare = re.sub(r"\([^)]*\)", "", label)
    paths = PATH.findall(bare.split(". ")[-1])
    return (
        role,
        paths[0] if paths else "src/main.la",
        int(rng.group(1)) if rng else None,
        (ref.group(1), int(ref.group(2))) if ref else None,
    )


def join_pieces(pieces):
    """Joins a file shown in parts ("lines 18 to 21"), each placed at its first line."""
    code = ""
    for first, text in sorted(pieces):
        have = code.count("\n")
        if have < first - 1:
            code += "\n" * (first - 1 - have)
        code += text
    return code


def imported(files, shown):
    """Drops each carried source file that no file the step shows imports, directly or through another."""
    module = {p: p[len("src/"):-len(".la")].replace("/", ".") for p in files if p.startswith("src/")}
    keep = {p for p in files if p in shown or not p.startswith("src/") or p == "src/main.la"}
    while True:
        names = {n for p in keep for n in re.findall(r"^\s*(?:public\s+)?import\s+([\w.]+)", files[p], re.M)}
        more = {p for p, mod in module.items() if p not in keep and any(n == mod or n.endswith("." + mod) for n in names)}
        if not more:
            return {p: files[p] for p in files if p in keep}
        keep |= more


def diagrams(text):
    """Turns each `Diagram:` line in a step's text into a diagram block; gives the text and the files."""
    files = DIAGRAM.findall(text)
    out = DIAGRAM.sub(lambda m: f'```diagram\nfile = "{m.group(1)}"\nalt = "{m.group(2)}"\n```', text)
    return out, [f for f, _ in files]


def blocks(material, where):
    """Gives each code block of a step's material with its label, refusing any other text."""
    out, pos = [], 0
    for m in FENCE.finditer(material):
        gap = [l for l in material[pos:m.start()].split("\n") if l.strip() and not RESULT.match(l)]
        if len(gap) > 1 or (gap and not LABEL.match(gap[0])):
            raise ConvertError(f"{where}: text between code blocks: {gap[0][:80]!r}")
        out.append((gap[0] if gap else "", m.group(1), m.group(2)))
        pos = m.end()
    rest = [l for l in material[pos:].split("\n") if l.strip() and not RESULT.match(l) and l.strip() != "---"]
    if rest:
        raise ConvertError(f"{where}: text after the code blocks: {rest[0][:80]!r}")
    return out


def convert_step(lesson, step, carried):
    """Gives one step's folder contents. `carried` holds the files earlier steps left in place."""
    where = f"{lesson.num} step {step.n}"
    start, solution = dict(carried), dict(carried)
    pieces = {"start": {}, "solution": {}}
    outputs = {}
    shown = set()
    for label, lang, code in blocks(step.material, where):
        if lang == "text":
            lower = label.lower()
            if lower.startswith("output"):
                outputs["start" if "(start" in lower else "solution"] = code
            elif not lower.startswith("tests"):
                raise ConvertError(f"{where}: a text block labelled {label!r}")
            continue
        if lang not in ("lugha", "toml"):
            raise ConvertError(f"{where}: a {lang!r} block")
        role, path, first, ref = label_role(label)
        if lang == "toml":
            path = "lugha.toml"
        if ref:
            other = lesson.done.get(ref[1])
            if other is None or ref[0] not in (other.solution or other.start):
                raise ConvertError(f"{where}: {ref[0]} isn't in step {ref[1]}")
            for d in (start, solution):
                d[ref[0]] = (other.solution or other.start)[ref[0]]
        shown.add(path)
        for r in ("start", "solution") if role == "both" else (role,):
            if first is not None:
                pieces[r].setdefault(path, []).append((first, code))
            else:
                (start if r == "start" else solution)[path] = code
    for r, files in pieces.items():
        for path, parts in files.items():
            (start if r == "start" else solution)[path] = join_pieces(parts)
    # Start and solution have the same files, so a file either one imports stays in both.
    keep = set(imported(start, shown)) | (set(imported(solution, shown)) if step.kind.fix else set())
    start = {p: c for p, c in start.items() if p in keep}
    solution = {p: c for p, c in solution.items() if p in keep}
    if "src/main.la" not in start:
        raise ConvertError(f"{where}: no src/main.la")
    if not step.kind.fix:
        solution = None
    elif solution == start:
        raise ConvertError(f"{where}: a fix step whose solution is the same as its start")
    front = {"title": step.title}
    if step.kind.fix:
        if step.kind.error:
            front["start_error"] = step.kind.error
        elif step.kind.failing:
            front["start_failing"] = ", ".join(step.kind.failing)
        elif "start" in outputs or step.kind.silent:
            front["start_output"] = outputs.get("start", "").replace("\n", "\\n")
        else:
            raise ConvertError(f"{where}: its start prints, but no `Output (start):` block says what")
    text, svgs = diagrams(step.prose)
    carried_names = sorted(p for p in start if p in carried and p not in shown)
    return Converted(step.n, step.title, front, text, start, solution, outputs.get("solution"), svgs, carried_names)


def write_step(folder, st, svg_dir):
    """Writes one converted step into `folder`."""
    os.makedirs(folder, exist_ok=True)
    front = "".join(f"{k}: {v}\n" for k, v in st.front.items())
    with open(os.path.join(folder, "step.md"), "w") as f:
        f.write(f"---\n{front}---\n\n{st.text}\n")
    for part, files in (("start", st.start), ("solution", st.solution or {})):
        for path, code in files.items():
            target = os.path.join(folder, part, path)
            os.makedirs(os.path.dirname(target), exist_ok=True)
            with open(target, "w") as f:
                f.write(code)
    with open(os.path.join(folder, "expected.txt"), "w") as f:
        f.write(st.expected or "")
    for name in st.diagrams:
        shutil.copy(os.path.join(svg_dir, name), os.path.join(folder, name))


def lesson_files(lesson):
    """Gives the files a lesson's text shows once for every step, before its first step."""
    files = {}
    for m in FENCE.finditer(lesson.head):
        if m.group(1) not in ("lugha", "toml"):
            continue
        label = [l for l in lesson.head[:m.start()].split("\n") if l.strip()][-1]
        files[label_role(label)[1] if m.group(1) == "lugha" else "lugha.toml"] = m.group(2)
    return files


def chapters():
    """Gives each chapter's number, title and draft folder, from the outline and the drafts."""
    out = []
    for num, title in re.findall(r"^## (\d+)\. (.+)$", open(OUTLINE).read(), re.M):
        title = re.sub(r"\s*(\*\([^)]*\)\*|\([^)]*\))$", "", title).strip()
        folder = glob.glob(os.path.join(DRAFTS, f"{int(num):02d}-*"))
        if len(folder) != 1:
            raise ConvertError(f"chapter {num}: no single draft folder")
        out.append((int(num), title, folder[0]))
    return out


def read_course():
    """Reads every draft: a list of (chapter number, title, folder name, lessons)."""
    course = []
    for num, title, folder in chapters():
        by_num = {}
        for path in sorted(glob.glob(os.path.join(folder, "*.md"))):
            lesson = parse_lesson(path, open(path).read())
            if lesson.num in by_num:
                by_num[lesson.num].steps += lesson.steps
            else:
                by_num[lesson.num] = lesson
        lessons = sorted(by_num.values(), key=lambda l: int(l.num.split(".")[1]))
        course.append((num, title, os.path.basename(folder), lessons))
    return course


def convert(course):
    """Converts every step, carrying each lesson's files from step to step."""
    all_lessons = {l.num: l for _, _, _, ls in course for l in ls}
    for _, _, _, lessons in course:
        for lesson in lessons:
            carried = lesson_files(lesson)
            for other, n, path in BORROWED.get(lesson.num, []):
                done = all_lessons[other].done[n]
                carried[path] = (done.solution or done.start)[path]
            for step in lesson.steps:
                st = convert_step(lesson, step, carried)
                lesson.done[step.n] = st
                carried = dict(st.solution or st.start)


def run_api(api, files):
    """Runs a project through the site's API and gives its stdout, or raises with what went wrong."""
    body = {"files": [{"path": p, "text": t} for p, t in files.items()], "entry": "src/main.la",
            "args": [], "stdin": "", "opt": 0}
    if "lugha.toml" not in files:
        manifest = open(os.path.join(REPO, "services/api/src/checks/manifest.la")).read()
        default = json.loads('"' + re.search(r'DEFAULT[^"]*"((?:[^"\\]|\\.)*)"', manifest).group(1) + '"')
        body["files"].append({"path": "lugha.toml", "text": default})
    req = urllib.request.Request(f"{api}/api/run", json.dumps(body).encode(), {"Content-Type": "application/json"})
    # The API takes 20 runs a minute from one address.
    time.sleep(3.1)
    r = json.load(urllib.request.urlopen(req, timeout=180))
    errors = [d for d in (r.get("compile") or {}).get("diagnostics", []) if d["severity"] == "error"]
    if errors:
        raise ConvertError(f"doesn't compile: {errors[0]['code']} {errors[0]['message']}")
    return (r.get("program") or {}).get("stdout") or ""


def main(argv):
    check = "--check" in argv
    api = argv[argv.index("--api") + 1] if "--api" in argv else None
    out = argv[argv.index("--out") + 1] if "--out" in argv else os.path.join(REPO, "content", "learn")
    course = read_course()
    convert(course)
    missing, steps = [], 0
    for _, _, _, lessons in course:
        for lesson in lessons:
            for st in lesson.done.values():
                steps += 1
                if st.expected is None:
                    if api:
                        st.expected = run_api(api, st.solution or st.start)
                    else:
                        missing.append(f"{lesson.num} step {st.n}")
                if st.carried:
                    print(f"{lesson.num} step {st.n}: carries {', '.join(st.carried)}")
    if missing:
        print("no recorded output (run with --api to fill): " + "; ".join(missing))
    print(f"{len(course)} chapters, {sum(len(c[3]) for c in course)} lessons, {steps} steps")
    if check or missing:
        return 0 if check else 1
    if os.path.exists(out):
        shutil.rmtree(out)
    for num, title, folder, lessons in course:
        chapter = os.path.join(out, folder)
        os.makedirs(chapter)
        with open(os.path.join(chapter, "chapter.toml"), "w") as f:
            f.write(f"title = {json.dumps(title)}\n")
        for lesson in lessons:
            ldir = os.path.join(chapter, f"{int(lesson.num.split('.')[1]):02d}-{lesson.slug}")
            os.makedirs(ldir)
            with open(os.path.join(ldir, "lesson.toml"), "w") as f:
                f.write(f"title = {json.dumps(lesson.title)}\n")
            for st in lesson.done.values():
                svg_dir = os.path.join(DRAFTS, "assets", f"{lesson.num}-{st.n}")
                write_step(os.path.join(ldir, f"{st.n:02d}-{slug(st.title)}"), st, svg_dir)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv[1:]))
    except ConvertError as e:
        print(f"md2content: {e}", file=sys.stderr)
        sys.exit(1)
