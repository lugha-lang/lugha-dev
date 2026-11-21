"""Shows each lesson step as a learner sees it after pressing Run, for reviewing the step's text.

For every step under the chapters asked for, prints the step's text, its start code with line
numbers, and what the output panel shows once the start runs through the site's API: the
diagnostics as the panel words them, the program's output and exit code, and the first paragraph
of the explanation beside each error.

Usage:
    python3 screens.py --api URL 01 02 > review.md
The numbers are chapter folders under content/learn.
"""
import glob
import json
import os
import re
import sys
import time
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.join(HERE, "..", "..", "..")
LEARN = os.path.join(REPO, "content", "learn")
EXPLANATIONS = os.path.join(REPO, "services", "ui-web", "generated", "explanations.txt")


def explanations():
    """Gives each code's first paragraph, as the panel shows it before "More about"."""
    out = {}
    for chunk in open(EXPLANATIONS).read().split("%%% ")[1:]:
        code, _, body = chunk.partition("\n")
        lines = body.split("\n")[1:]
        para = "\n".join(lines).strip().split("\n\n")[0]
        out[code.strip()] = " ".join(para.split())
    return out


def project(folder):
    """Gives every file of a step's start/ or solution/, with the default lugha.toml when it has none."""
    files = {}
    for path in glob.glob(os.path.join(folder, "**", "*"), recursive=True):
        if os.path.isfile(path):
            files[os.path.relpath(path, folder)] = open(path).read()
    if "lugha.toml" not in files:
        manifest = open(os.path.join(REPO, "services/api/src/checks/manifest.la")).read()
        files["lugha.toml"] = json.loads('"' + re.search(r'DEFAULT[^"]*"((?:[^"\\]|\\.)*)"', manifest).group(1) + '"')
    return files


def post(api, kind, files):
    """Sends a project to the API's run or test route and gives back its JSON."""
    body = {"files": [{"path": p, "text": t} for p, t in files.items()]}
    if kind == "run":
        body.update(entry="src/main.la", args=[], stdin="", opt=0)
    req = urllib.request.Request(f"{api}/api/{kind}", json.dumps(body).encode(), {"Content-Type": "application/json"})
    # The API takes 20 requests a minute from one address.
    time.sleep(3.1)
    return json.load(urllib.request.urlopen(req, timeout=180))


def panel(r, explained):
    """Gives the output panel's text for one run, as the site words it."""
    out = []
    codes = []
    for d in (r.get("compile") or {}).get("diagnostics", []):
        s = d["span"]["start"]
        out.append(f"{d['severity']}[{d['code']}]: {d['message']}\n  --> {d.get('file') or d['span'].get('file') or 'src/main.la'}:{s['line']}:{s['col']}")
        if d.get("help"):
            out.append(f"  = help: {d['help']}")
        if d["severity"] == "error" and d["code"] not in codes:
            codes.append(d["code"])
    prog = r.get("program")
    if prog:
        if prog.get("stdout"):
            out.append(prog["stdout"].rstrip("\n"))
        if prog.get("stderr"):
            out.append("(stderr) " + prog["stderr"].rstrip("\n"))
        out.append(f"Exited with code {prog.get('exit_code')}")
    for c in codes:
        out.append(f"\n[explanation box, {c}] {explained.get(c, '(none)')}")
    return "\n".join(out)


def numbered(code):
    return "\n".join(f"{i:>3}  {l}" for i, l in enumerate(code.rstrip("\n").split("\n"), 1))


def main(argv):
    api = argv[argv.index("--api") + 1]
    chapters = [a for a in argv if re.fullmatch(r"\d\d", a)]
    explained = explanations()
    for ch in chapters:
        for lesson in sorted(glob.glob(os.path.join(LEARN, f"{ch}-*", "[0-9]*"))):
            print(f"\n# {os.path.relpath(lesson, LEARN)}\n")
            for step in sorted(glob.glob(os.path.join(lesson, "[0-9]*"))):
                md = open(os.path.join(step, "step.md")).read()
                print(f"## {os.path.basename(step)}\n\n{md.strip()}\n")
                start = project(os.path.join(step, "start"))
                for path in sorted(p for p in start if p.endswith(".la")):
                    print(f"{path}:\n```\n{numbered(start[path])}\n```\n")
                kind = "test" if any(p.startswith("test/") or "@test" in t for p, t in start.items()) else "run"
                if kind == "test":
                    print("(a test step: press Test)\n")
                try:
                    shown = panel(post(api, "run", start), explained)
                except urllib.error.HTTPError as e:
                    shown = f"(the API answered {e.code}: {e.read().decode()[:200]})"
                print(f"After Run:\n```\n{shown}\n```\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
