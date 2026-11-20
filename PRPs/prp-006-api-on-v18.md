## FEATURE: The API and its sandbox runner written in Lugha v18 (lughac 0.18.0, tag m238), serving requests at the same time, while visitors' code keeps compiling with m159 until the course moves

Status: **approved by the owner, 2026-11-20** (it touches the code that runs submitted programs and the rate limit: CLAUDE.md, SECURITY). The droplet's memory check for API-11 is pending.

### What changed while building it (2026-11-20)

- **The API's compiler is m238, not m237.** v18's process lockdown refused `socketpair` to programs without `Net`. The runner holds `Fs` and `Proc`, and Ubuntu 26.04's `timeout` (uutils) makes an `AF_UNIX` socket pair to start its child, so every compile failed. The owner chose to fix it in `../lugha` (PRP-270, milestone 238: an unnamed socket pair needs no `Net`). **m238 must be merged and tagged in `../lugha` before this PRP merges**, or the image build fails at the clone.
- **The slots are a channel of tokens, not an actor.** An actor handles one message at a time, so a `take()` waiting for a free slot would block the `give()` that frees one. This is the fallback the design named.
- **Tests that start Docker also take `Net`, unused.** `docker` talks to its daemon through a unix socket, which the lockdown refuses without `Net`.
- **`lughac test src test`, not a bare `lughac test`, in `services/api`.** The bare form also compiles `sandbox/warm/`, a program written for the visitors' compiler (m159).
- **Verified locally without building lughac in Docker.** Test images were `lugha-sandbox:m159` and `lugha-api:local`, each with the new binary, built with `../lugha` at PRP-270. Results:
  - `scripts/hostile`: 12 passed;
  - `scripts/content`: 3 passed;
  - two Runs at once: a normal program answered in 0.6 s while an endless loop ran to its 5 s limit;
  - `npm run e2e` against the fresh `dist` through the new API: 26 passed. The one failure is the stand-in server's `/playground/` redirect, as before.

  The Dockerfile's two-compiler build itself has only run in CI, after merging.

## OBJECTIVE

A visitor notices nothing except that the site no longer queues behind other visitors. Run, Test and Format give exactly the same results as today, because their code is still compiled by m159. But two visitors pressing Run at once now both get an answer without one waiting for the other's sandbox, up to two sandboxes at a time. Every refusal, limit and sentence stays as it is.

For us: the API's own code and tests compile with the lughac now installed (0.18.0), so `lughac test` and `scripts/content` in `services/api` pass again. The sandbox image ships two things built by two different compilers: the m159 `lughac` that compiles visitors' code, and the runner, built by m237.

## CONTEXT

- Read first:
  - `services/api/src/main.la`, which wires the server. It uses `std.env`, `std.time`, `http.serve_with` and a `Ref` limiter, and calls `eprintln`/`exit`.
  - `src/runner/main.la`, which uses `std.fs`, `std.env.set_current_dir`, `std.process`, `args()`, `read_stdin_bytes`, `read_file`/`write_file` and `println`.
  - `src/server/sandbox.la` (`process.run_with`, the `docker run` flags) and `src/server/ratelimit.la` (`#{}`).
  - `src/server/routes.la`, `src/checks/*.la` and `src/runner/{steps,outcome}.la`, which need patterns and literals updated.
  - `test/*.la`. `content.la` and `hostile.la` start Docker.
  - `Dockerfile`, which has one `lughac` stage for both images, `docker-compose.yml`, `.github/workflows/deploy.yml` (`LUGHAC_REF: m159`), and `scripts/content` and `scripts/hostile`.
- **Sources, each confirmed to exist:**
  - `../lugha` at tag **m237**, with `lughac --version` reporting `lughac 0.18.0`.
  - The installed compiler: `~/.cargo/bin/lughac`, 0.18.0.
  - `../lugha/skill/`, mainly `concepts/10-capabilities.md`, `11-tasks-and-scopes.md`, `12-channels-and-actors.md`, `library/http.md` and `library/env-and-processes.md`.
  - `../lugha/docs/specs/Language v18 Specification.md`. `lughac spec` no longer exists in 0.18.0.
- **Facts checked on this machine (2026-11-20).** Each is a program of ours, built with 0.18.0 and run under `runsc` with the sandbox's own `docker run` flags:
  - a `Dir` writes, reads and makes folders inside gVisor, and refuses `../etc/hostname`;
  - a scope's tasks run and join;
  - lockdown reports "seccomp applied; landlock not applied". gVisor has no Landlock, which v18 skips quietly;
  - a program holding `Fs` and `Proc` ran `cat` with stdin and ran the image's m159 `lughac --version`, which reported "lughac 0.1.0".

  So a v18 runner can drive the m159 compiler.
- **Decisions:**
  - API-1 to API-6 and API-8 to API-10 hold.
  - **API-7 changes:** requests are served at the same time, at most 2 sandboxes at once. The deferred entry "Non-blocking `std.process`" is resolved by v18's helper threads (`../lugha` milestone 206).
  - New, for the owner's approval: **API-11**, under Design.
- **Discovery answers (owner, 2026-11-20):**
  1. Split compilers. The API and runner are ported to v18 and built with m237. Visitors' code stays on m159 until the v18 course is ready, and the sandbox then switches to m237 in its own PRP.
  2. Concurrency is on, capped at 2 sandboxes.
  3. lughac 0.18.0 is installed. The owner builds images, or approves a build, as before.

## REQUIREMENTS

### Must Do

- **Port every file in `services/api/src` and `test/` to v18, without changing behaviour.** Each request still produces the same response, status and log line as before.
  - Capabilities replace globals:
    - `main(console, env, clock, net, proc)` for the API;
    - `main(args, console, fs, proc)` for the runner, with `console.read_bytes()` for the job on stdin.
  - The exit code is `main`'s `i32` result.
  - Patterns take a leading dot. `#{…}` becomes `Map {…}`. Lossy `as` becomes `truncate`/`round`/`try_into`. A dropped `Result` becomes `let _ =`.
  - Types meet their interfaces through `impl`/`with` where v18 asks for it. Printing that relied on built-in text uses `.debug()` or `Display`.
- **Runner** (`src/runner/main.la`):
  - writes and reads the job's files through `fs.cwd()`. The container already starts in `/work` (`--workdir=/work`), so `set_current_dir` and the `[WORK_FOLDER]` argument go;
  - runs commands through `proc`.
  - `runner --version` still answers with the sandbox's `lughac --version`, which is m159's until the switch.
- **API** (`src/main.la`):
  - `http.serve_with(net, addr, limits, handler)`, with a handler that is `Sendable`.
  - **The rate limiter becomes an actor**, `Counts`, holding a `Limiter` with one message, `allow(ip, now_ms): bool`. `allow` and `client_ip` stay pure functions with their tests. The handler captures only the actor, the image name, the version and the `Proc`.
- **At most 2 sandboxes at a time.** A request that would start a third waits in the API until one finishes. The design is in API-11 below.
- **A panic in one request doesn't take the others down.**
  - `serve` returns `Err` when a connection panics, and in v18 it cancels the others first. So `main` logs the error and serves again, in a loop, and exits 1 only when it can't listen.
  - No handler path calls `unwrap`, `expect` or indexing that could panic on a visitor's input. The existing checks already refuse bad input with sentences; the port keeps that.
- **Two compilers in the build** (`Dockerfile`, `docker-compose.yml`, `deploy.yml`):
  - `LUGHAC_REF` (m159) builds the `lughac` that visitors' code meets.
  - `API_LUGHAC_REF` (m237) builds the `lughac` that compiles `runner` and `api`. The two are separate stages, each cached in the registry as now.
  - The sandbox image takes `lughac` from the first and `runner` from the second, and keeps its tag `lugha-sandbox:${LUGHAC_REF}`.
- **Tests that start Docker:**
  - `test/content.la` and `test/hostile.la` take `Proc` and `Env`, so they become `@test(integration)`.
  - `scripts/content` and `scripts/hostile` pass `--integration`. The other test files stay plain `@test`s.
- **The hostile suite passes as today.** Add one case where two jobs run at once and both are still held by their own limits.
- **Docs:**
  - DECISIONS.md: API-7 updated, API-11 added, and the deferred entry moved to resolved.
  - `services/api/src/main.la`'s header loses the "one at a time" paragraph.
  - CLAUDE.md's COMMANDS block: `lughac spec` is gone from 0.18.0, so it points to `../lugha/skill/` and the v18 spec file instead. The owner approves that line.

### Must NOT Do

- **No change to the sandbox's limits, flags or isolation** (API-5, API-6). The runner still reads only stdin and writes only stdout. The API still reads only the container's output.
- **No change to what visitors' code is compiled with.** The m159 `lughac` stays until the course PRP switches it.
- **No change to the API's routes, requests, responses, sentences or rate** (20 a minute per IP).
- **No new dependency.**

## DESIGN

- **API-11, at most two sandboxes at once** (for the owner's approval):
  - An actor, `Slots`, holds a count of jobs running, with a limit of 2.
  - Its message `take()` answers once a slot is free. Mailbox calls wait for their answer, and the actor answers in order. `give()` frees one.
  - `run_logged` takes a slot, runs the sandbox, and gives the slot back in a `defer`, so a cancelled or failed run still frees it.
  - **Why two:** the droplet has 1 CPU, and a compile may take up to 30 s against Caddy's 60 s upstream timeout. Two keeps a second visitor from queuing behind a long compile, without stretching both past the timeout. The limit is one constant, `checks.limits.SANDBOXES`.
  - **Why an actor and not a scope with `limit 2`:** each connection is already its own task in `serve`'s scope, so the limit has to be shared across connections. An actor is the v18 way to share state (`skill/concepts/12-channels-and-actors.md`).
  - If the actor approach proves wrong once built, a channel used as a semaphore is the fallback, with the same requirement.
- **Rate limiting with concurrency:** the `Counts` actor handles one `allow` at a time, so two requests from the same IP can't both slip under the count. The window and the rate are unchanged.
- **Error cases:**
  - When the sandbox can't be run, the visitor sees the existing service sentence.
  - When the API's `serve` returns `Err`, the log line is `serve stopped: …` and it serves again. A visitor whose connection was cancelled sees the site's existing "server is busy" message, the same as a timeout.
- **Security notes:**
  - The runner now holds `Fs` and `Proc` explicitly, so v18's lockdown limits it to those inside gVisor: seccomp refuses sockets, since it has no `Net`. That is a small gain on top of `--network=none`.
  - Inside gVisor, `Dir` refuses `..`, absolute paths and links leading out. That was checked.
  - The API takes `Net` (to listen) and `Proc` (to run `docker`). It takes no `Fs`, so lockdown refuses it file access beyond what `Net` and `Proc` need.
  - **For the owner:** two sandboxes at once on one droplet means two compiles' memory at once, up to 2 × 1 GB (API-5). Check this against the droplet's RAM before merging. If it doesn't fit, the limit is 1, and only the "server not blocked" half of this PRP ships.
- **Not in this PRP:**
  - switching visitors' code to m237, or `LUGHA_WORKERS`/`LUGHA_HELPERS` for visitors' programs (v18 starts a worker per CPU). Both belong to the switch PRP;
  - the course;
  - the home page's new headline.

## CONTENT

None. No visitor-facing text changes.

## TESTS

- [ ] Every existing test in `test/` (requests, manifest, job, files, outcome, steps, routes, ratelimit, sandbox), ported and passing under 0.18.0.
- [ ] `ratelimit`: the `Counts` actor allows 20 requests from one IP in a minute and refuses the 21st, with 21 requests sent from concurrent tasks. Two IPs are counted apart.
- [ ] `Slots`: with a limit of 2, a third `take()` waits until a `give()`. A run that fails still gives its slot back.
- [ ] `routes`: unchanged answers for every route and refusal, with the sandbox passed in as a function as now.
- [ ] Integration, `scripts/content`: every lesson step and example passes through the real sandbox (m159 visitors' compiler, m237 runner).
- [ ] Integration, `scripts/hostile`: every case passes. New case: two jobs start at once (an endless loop and a normal program), the loop is stopped at 5 s, and the normal one answers in about its usual time.
- [ ] `GET /api/version` still reports the sandbox's m159 `lughac`.

## ACCEPTANCE

- [ ] `lughac test` in `services/api` passes with lughac 0.18.0, along with `scripts/content` and `scripts/hostile`.
- [ ] `npm test`, `npm run check`, `npm run build` and `npm run e2e` in `services/ui-web` pass against the local stack built from the new images.
- [ ] With the stack up, two Runs sent at the same moment both answer. The second doesn't wait for the first's whole run (timed in the API log).
- [ ] The full suite passes, including every lesson step and example run through `lughac`.
- [ ] For the owner, by eye: on the local stack, open two Playground tabs, press Run in both, and see both answer.
- [ ] For the owner: the droplet's memory fits two sandboxes, or API-11's limit is set to 1.
