## FEATURE: Visitors' code moves from lughac m159 to m240 (Lugha v18), and the site's content moves with it: the v18 course replaces the old one, and the examples, the home card and the Playground's program are ported

Status: **approved by the owner, 2026-11-21** (it changes the compiler that submitted code meets and the runner's environment: CLAUDE.md, SECURITY). The m240 images and the droplet's memory check are the owner's.

## OBJECTIVE

A visitor writes and runs Lugha v18 everywhere on the site.
- **Learn** shows the v18 course: 12 chapters, 57 lessons, as drafted and approved in `docs/content/v5`. Each step's code, output and errors are the ones m240 gives. Everyone starts the course fresh at 1.1.
- **Examples** shows the same five programs, written for v18.
- **Home** keeps its code card, written for v18.
- **Playground** opens with a v18 program. Its input tab's help says how a v18 program reads arguments and standard input.
- Run, Test and Format compile with m240, and a program's tasks run on one worker thread, the same on every machine.

For us: one compiler, m240, builds visitors' code, the runner and the API.

## CONTEXT

- **Read first:**
  - `docs/content/v5/**` (the approved drafts) and `docs/content/outline.md`.
  - `services/ui-web/src/content/load.ts`, the step format: `step.md` front matter `title`, `start_error`, `start_output`, `start_failing`, `error_note` and `see_also`; `start/` and `solution/` projects; `expected.txt`; `lesson.toml` and `chapter.toml` titles.
  - `services/api/test/content.la`, the content check.
  - `services/api/src/runner/steps.la` (`prlimit`) and `src/server/sandbox.la` (`docker run`).
  - `Dockerfile`, `docker-compose.yml`, `.github/workflows/deploy.yml` and `deploy/prod.env`. All of them hold `LUGHAC_REF=m159`; the API's ref is `m238`.
  - `services/api/sandbox/warm/` (m159 code).
  - `services/ui-web/scripts/explanations.sh` (its default image is `lugha-sandbox:m159`).
  - `services/ui-web/grammar/lugha.tmLanguage.json`, `src/editor/lugha.ts` and `test/tokenizer.test.ts`.
  - `services/ui-web/src/lib/copy.ts` (`argumentsHelp`, `stdinHelp`), `src/lib/progress.ts` and `src/lib/storage.ts`.
  - `services/ui-web/test/e2e/*.spec.ts`, which name v4 lesson URLs.
- **Creates:**
  - `content/learn/**` (replaced wholesale);
  - `docs/content/tools/md2content.py`, the converter, which uses only Python 3's standard library and runs only on a developer's machine.
- **Changes:**
  - `content/examples/*`, `content/home`, `content/playground`;
  - every file above that names m159 or m238;
  - `services/api/src/runner/steps.la`, `copy.ts` and `progress.ts`;
  - the e2e specs, the grammar, and DECISIONS.md.
- **Sources (each confirmed to exist, 2026-11-21):**
  - `../lugha` tag **m240** (PRP-272, the per-task cycle collector), and the installed `lughac 0.18.0`.
  - `../lugha/docs/specs/Language v18 Specification.md`: workers at L1126; `LUGHA_WORKERS` takes 1 to 256.
  - `../lugha/skill/`.
  - `../lugha/editors/vscode/syntaxes/lugha.tmLanguage.json`.
- **Decisions:** no open one blocks this work.
  - O10 is resolved at m239, so lesson 6.3 step 3 works from m239 on.
  - API-1 to API-11 hold. API-11's memory check on the droplet is still pending from PRP-006, and stays an acceptance item here.
  - O7 and O9 are not touched.
- **Discovery answers (owner, 2026-11-21):**
  1. **The compiler is m240.** Every lesson step, example and program is re-run on it.
  2. **All the site's programs are ported in this PRP:** the five examples, the home card and the Playground's program. Changed copy comes to the owner word for word (CONTENT below).
  3. **`LUGHA_WORKERS=1` for visitors' programs.**
  4. **Old progress is dropped:** a visitor's saved v4 progress and edits are ignored and cleared, and everyone starts at 1.1.
  5. Not needed: an arguments or stdin box in Learn. No v18 step asks for input. 10.1 and 10.3 point to the Playground's input tab, which this PRP brings to v18.

## REQUIREMENTS

### Must Do

- **One compiler, m240.**
  - `LUGHAC_REF` and `API_LUGHAC_REF` both become `m240` in `Dockerfile`, `docker-compose.yml`, `deploy.yml` and `deploy/prod.env`. The two build args stay, so the API and the visitors' compiler can part again later; the two stages build the same tag.
  - `scripts/explanations.sh` defaults to `lugha-sandbox:m240`. Its output, `generated/explanations.txt`, is regenerated from the m240 image.
- **The API on m240.** `lughac test src test` in `services/api` passes on m240. Any change m240 asks of the API's code is made without changing its behaviour, as in PRP-006.
- **One worker per visitor's program.** `Proc` has no way to set a child's environment (skill, `library/env-and-processes.md`), so `run_command` in `src/runner/steps.la` starts the program through `env`: `prlimit … -- env LUGHA_WORKERS=1 <program> <args>`. It is still a list of arguments, with no shell. Tests need nothing: `lughac test` already runs a program's tests on one worker (spec L1126, "A deterministic or shuffled run … uses one worker"). The sandbox image's `env` is checked to be present and to keep the program's arguments as they are.
- **The warm program in v18.** `sandbox/warm/src/main.la` becomes `fun main(console: Console) { console.println("warm"); }` and keeps its test. Its comment loses "and the garbage collector", since v18 has no tracing collector (spec L1388).
- **The course.**
  - `docs/content/tools/md2content.py` turns each v5 draft into `content/learn/NN-chapter/NN-lesson/NN-step/`.
  - What the draft says goes where:
    - The step text goes to `step.md`, without the `Kind:` line, the code blocks or the Notes.
    - The title goes to the front matter.
    - The Start goes to `start/`, and the Solution to `solution/`, each with every file the step shows. A step that says "as in step 1" for a file gets that step's file.
    - The step's output goes to `expected.txt`.
    - `start_error` / `start_output` / `start_failing` come from the step's `Kind:` line, and are checked against the run.
  - Chapter and lesson titles and slugs come from the outline. 8.7's two files make one lesson.
  - The old `content/learn/` is removed.
  - A step's text is copied exactly as the owner approved it. The converter never rewrites a sentence. Anything it can't place (a block it can't assign to a file, a Kind it can't read) stops the conversion with the file and step named. It never guesses.
- **The examples, home and Playground** become the v18 programs in CONTENT, with the `expected.txt` that m240 prints. Each example's notes (`//:` lines) and its `example.toml` take the approved copy.
- **The input tab's help.** `argumentsHelp` and `stdinHelp` in `copy.ts` take the approved copy.
- **Highlighting.** `grammar/lugha.tmLanguage.json` is copied again from `../lugha` at m240. `KEYWORDS` in `src/editor/lugha.ts` follows it, and the tokenizer test that checks the two keeps passing.
- **A fresh start in Learn.**
  - The progress and edits kept in the browser carry a course version. A stored value from before this PRP has none.
  - When the version on the page is newer than what's stored, Learn clears the old progress and step edits once and starts empty. Nothing else stored is touched: the Playground's project stays, though its code may be m159 and no longer compile.
- **e2e tests** name v18 lesson URLs: the multi-file steps are 11.1 Modules and 11.2 Visibility. Their flows stay the same.
- **DECISIONS.md:**
  - a resolved entry for this switch: m240, one worker, old progress dropped;
  - the deferred "Non-blocking" and O10 notes that wait on "when visitors move" are updated.

### Must NOT Do

- **No change to the sandbox's limits, flags or isolation** (API-5, API-6), apart from the one environment variable. `--cpus=1`, `prlimit --as/--nproc`, `--network=none` and the rest stay.
- **No lesson text changed in conversion.** Any change the m240 run calls for goes to the owner first; see "A changed output" below.
- **No new copy beyond CONTENT.**
- **No new runtime dependency.** The converter is a developer's tool only.
- **No migration of old progress** (discovery answer 4).
- **No arguments or stdin box in Learn.**

## DESIGN

- **Order of work:**
  1. Convert, with the converter's own tests on a few drafts: a read step, a fix step, a multi-file step, a test step, and the split 8.7.
  2. Ask the owner to build the m240 images (CLAUDE.md: they're never built locally without asking).
  3. Run `scripts/content` on the m240 sandbox.
  4. Run the rest of the suite.
- **A changed output.** The drafts ran on m239 with one worker per CPU (four here). On m240 with one worker, an output can differ: a message's wording, a column in a panic, or the order of task output in chapter 12.
  - The converter writes the draft's output.
  - When `scripts/content` disagrees, the step's m240 output and the draft's are shown to the owner side by side, with any sentence that names the old value. Nothing is changed until the owner approves it.
  - The draft in `docs/content/v5` is updated to match, so the drafts stay the record.
- **What the content check compares.** As today, it compares stdout and the error code. The stderr panic lines and exit codes written in the drafts' Output labels aren't checked, and the site shows whatever m240 prints.
- **The course version** is a constant beside the progress code. Bumping it means "the course changed shape". It is not bumped for a text edit.
- **Security notes (for the owner's review):**
  - A new compiler meets submitted code. The hostile suite (`scripts/hostile`) runs against the m240 sandbox before merging. Its cases are unchanged.
  - `LUGHA_WORKERS=1` lowers the threads a program starts. It is a fixed value the runner sets, never anything from the request.
  - The playground still refuses `[link]` and git packages (API-3), which is unchanged in v18's manifest format. The content check confirms that the default `lugha.toml` (`src/checks/manifest.la`) is still accepted by m240.
- **The droplet:**
  - the images are built in Actions as today (API-10);
  - `deploy/prod.env` moves to m240;
  - pushing to `main` deploys, so the owner pushes.

## CONTENT

Every visitor-facing sentence that changes. Lesson text is the approved v5 drafts, unchanged. Each program below was run on lughac m239 in the drafting sandbox (`lugha-sandbox:m239-draft`), and the outputs are what it printed. `scripts/content` re-checks them on m240.

### Input tab help (`copy.ts`)

- `argumentsHelp`, now "Passed after `--`; read them with `args()`." → **"Passed after `--`; `main` takes them as `args: string[]`."**
- `stdinHelp`, now "What `read_line()` reads, one line at a time." → **"What `console.read_line()` reads, one line at a time."**

### Examples

**hello-world**: title, intro and group unchanged. Tags `["fun main", "println"]` → `["fun main", "Console", "println"]`.

```lugha
//: Every program starts at `main`, which is given the console to print through. Without a return type, it exits with code 0 when it ends.
fun main(console: Console) {
//: `console.println` prints a value and a newline.
    console.println("Hello, world!");
}
```
```text
Hello, world!
```

**fibonacci**: `example.toml` unchanged. The notes are unchanged; only the code changes.

```lugha
//: A function whose body is one expression can use `=`. `if` is an expression too, so its branches give the result directly.
fun fib(n: i64): i64 = if n < 2 { n } else { fib(n - 1) + fib(n - 2) };

//: `main` can return an `i32`: the program's exit code. Its last expression, `0`, is the value it returns.
fun main(console: Console): i32 {
    console.println(fib(30));
    0
}
```
```text
832040
```

**green-threads**: the folder stays as it is, so its URL doesn't change.
- Title "Green threads" → **"Tasks"**.
- Intro "Run two calls at the same time and add up their results, with no async and no await." → **"Run two calls at the same time and add up their results."** (owner, 2026-11-21: the old ending leaned on other languages)
- Tags → `["scope", "spawn", "join"]`.

```lugha
//: An ordinary function. Nothing marks it as concurrent.
fun work(n: i64): i64 = n * n;

//: A task starts in a scope: `s.spawn` starts a call as a task and hands back a handle straight away.
fun main(console: Console) {
    let r = scope s {
        let a = s.spawn(work(3));
        let b = s.spawn(work(4));
//: `join` waits for a task and gives back its result, `Ok` unless the task failed. Every function stays an ordinary function.
        a.join().unwrap() + b.join().unwrap()
    };
//: The scope ends only when all its tasks have, and its value is `Ok` with what its body gave.
    console.println(r.debug());
}
```
```text
Ok(25)
```

**actor-counter**: title unchanged.
- Intro "State that one green thread owns. …" → **"State that one task owns. Other code talks to it by calling its methods, which become messages."**
- Tags → `["actor", "scope", "mut self"]`.

```lugha
//: An `actor` declares state that one task owns. Its fields are private to it.
actor Counter {
    count: i64,
//: Its methods are messages, handled one at a time, so the state needs no locks.
    fun add(mut self, n: i64) { self.count += n; }
    fun get(self): i64 = self.count;
}

//: An actor starts in a scope, as a task does. `c.add(5)` is queued; `c.get()` waits for the answer.
fun main(console: Console) {
    let r = scope s {
        let c = s.spawn(Counter { count: 0 });
        c.add(5);
        c.add(2);
        c.get()
    };
    console.println(r.debug());
}
```
```text
Ok(7)
```

**word-frequency**: `example.toml` unchanged, `stdin` included. Two notes change (`#{}`, `read_line()`).

```lugha
//: A map literal is `Map {}`. Its type says what it holds: each word and how often it appears.
fun main(console: Console) {
    let mut counts: Map<string, i64> = Map {};
//: `console.read_line()` gives `Ok(None)` at the end of the input, which ends the `while let`. Each line is split on spaces, and the empty pieces are skipped.
    while let .Ok(.Some(line)) = console.read_line() {
        for w of line.split(" ") {
            let word = w.trim();
            if word != "" {
//: `get` returns an `Option`, so `unwrap_or(0)` starts a new word at zero.
                counts[word] = counts.get(word).unwrap_or(0) + 1;
            }
        }
    }

//: A map iterates as `(key, value)` tuples. Copy them into an array so they can be sorted.
    let mut entries: (string, i64)[] = [];
    for (w, c) of counts {
        entries.push((w, c));
    }
//: `sort_by` takes a function that says whether `a` comes before `b`: the highest count first, then alphabetical. It returns a new, sorted array.
    let top = entries.sort_by(fun(a, b) = a.1 > b.1 || a.1 == b.1 && a.0 < b.0);

//: Format specifiers line the columns up: `{w:<8}` pads the word to 8 characters, `{c:>3}` right-aligns the count.
    console.println("{counts.len} different words");
    for (w, c) of top.iter().take(5) {
        console.println("{w:<8} {c:>3}");
    }
}
```
```text
8 different words
the        5
sat        3
cat        2
mat        2
on         2
```

### Home code card (`content/home`)

```lugha
fun fib(n: i64): i64 =
    if n < 2 { n } else { fib(n - 1) + fib(n - 2) };

fun main(console: Console): i32 {
    console.println(fib(30));
    0
}
```
```text
832040
```

### Playground's starting program (`content/playground`)

```lugha
enum Shape { Circle(f64), Square(f64) }

fun area(s: Shape): f64 = match s {
    .Circle(r) => 3.14159 * r * r,
    .Square(side) => side * side,
};

fun main(console: Console): i32 {
    let shapes = [Shape.Circle(1.0), Shape.Square(2.0), Shape.Circle(0.5)];
    for s of shapes {
        console.println("{s.debug()} has area {area(s):.2}");
    }
    let total = shapes.iter().map(area).sum();
    console.println("total: {total:.2}");
    0
}

@test fun square_area() {
    assert_eq(area(Shape.Square(3.0)), 9.0);
}
```
```text
Circle(1.0) has area 3.14
Square(2.0) has area 4.00
Circle(0.5) has area 0.79
total: 7.93
```
Test: `playground.main.square_area` passed, 1 test: 1 passed, 0 failed.

## TESTS

- [ ] **Converter, on fixture drafts.** Each of these produces the expected step folders:
  - a read step;
  - a fix step with `start_error`;
  - a fix step with `start_output` (1.1 step 4);
  - a multi-file step whose file is "as in step 1" (11.2 step 2);
  - a test step with `start_failing` (11.4 step 3, with its split blocks);
  - the split 8.7.

  An unknown Kind, or a block it can't place, stops it with the file and step named.
- [ ] **`npm run build`** loads the whole converted course with no problems. Every step has a title, its files, and the start fields that its kind needs.
- [ ] **`scripts/content` on m240:** every step's start and solution, every example (word-frequency with its stdin), home and the Playground program.
- [ ] **`scripts/hostile` on m240:** every case passes, unchanged.
- [ ] **Runner:** `run_command` gives `prlimit … -- env LUGHA_WORKERS=1 <program> <args>` (unit test). In the sandbox, a program printing `LUGHA_WORKERS` from its `Env` prints `1`, and an argument holding spaces or `=` reaches the program unchanged.
- [ ] **Progress (Vitest):**
  - stored progress without a version is cleared once and reads as nothing done;
  - progress with the current version is kept;
  - the Playground's stored project is untouched.
- [ ] **Tokenizer:** the keyword lists match the m240 grammar.
- [ ] **e2e:** the Learn file flows on 11.1/11.2, the Playground's Run and Test, and word-frequency's Open in Playground.
- [ ] **`lughac test src test` in `services/api`** passes on m240.
- [ ] `GET /api/version` reports the m240 `lughac`.

## ACCEPTANCE

- [ ] `npm test`, `npm run check`, `npm run build` and, with the stack up, `npm run e2e` pass in `services/ui-web`.
- [ ] `lughac test src test`, `scripts/content` and `scripts/hostile` pass in `services/api` against the m240 images.
- [ ] Every output that m240 prints differently from the drafts has been shown to the owner and approved, and the drafts were updated to match.
- [ ] The full suite passes, including every lesson step and example run through `lughac`.
- [ ] For the owner, by eye, on the local stack:
  - Learn opens at 1.1 with the 12 chapters;
  - a fix step's Run, Solve and Reset work;
  - 6.3 step 3 prints its stack overflow panic;
  - a chapter 12 step runs;
  - the five examples, Home's card and the Playground run;
  - the input tab's help reads as approved.
- [ ] For the owner: the droplet's memory fits two sandboxes (API-11, from PRP-006), or `SANDBOXES` is set to 1 before this deploys.
