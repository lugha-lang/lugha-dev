## FEATURE: Format and Test show a compile error the way Run does: lughac's own text with the code under it, its explanation beside it, and the line marked in the editor

Status: **approved by the owner, 2026-11-22** (it changes the runner's commands for submitted code: CLAUDE.md, SECURITY).

## OBJECTIVE

When code that doesn't compile is formatted or tested, the visitor sees the same thing as when they press Run:
- each error in `lughac`'s own words, with the code under it and a mark at the exact spot;
- its explanation (or a step's own note) beside it;
- the line marked in the editor.

Today Format and Test show `lughac`'s plain text instead: no explanation box, no editor mark.

## CONTEXT

- **Read first:**
  - `services/api/src/runner/steps.la`: `test_command` and `format_command`.
  - `services/api/src/runner/outcome.la`: `diagnostics(stderr)`, `test_result`'s `compile_error` and `format_result`'s `error`.
  - `services/ui-web/src/lib/api.ts`: `readTest`, `readFormat`, and their `test-compile-error` and `format-error` states.
  - `services/ui-web/src/components/workspace/Workspace.svelte` (`test()` and `format()`) and `src/lib/panel.ts` (the `compile-error` panel Run already uses).
- **Sources, checked 2026-11-22 with lughac 0.18.1:**
  - `lughac test --json --diagnostics=json .` puts the results on stdout and each compile error on stderr as one JSON diagnostic per line, `rendered` included.
  - `lughac fmt --diagnostics=json <files>` does the same for its syntax errors and exits 1.
  - Both are `../lugha` milestone 244 (PRP-277), in tag `v0.18.1`.
- **Decisions:**
  - It resolves the deferred item "JSON errors from `lughac fmt` and `lughac test --json`".
  - API-1 to API-11 hold. No open decision applies.

## REQUIREMENTS

### Must Do

- **Runner:**
  - `test_command` and `format_command` add `--diagnostics=json`.
  - `test_result` and `format_result` add a `diagnostics` array, built by the same `diagnostics(stderr)` Run uses.
  - `compile_error` (Test) and `error` (Format) stay as they are, so the content check and any older client keep working.
- **Site:**
  - `readTest` and `readFormat` read `diagnostics`.
  - When it's non-empty, the Tests tab (for Test) or the Output tab (for Format) shows the `compile-error` panel, the same component Run uses.
  - The editor marks the error lines, as for Run.
  - With no `diagnostics` in the answer, the plain text shows as now.
  - A Learn step's own error note still applies only to Run's start error, as now.

### Must NOT Do

- No change to the sandbox's limits, flags or isolation. The runner gains one flag on two commands; arguments stay a list.
- No new copy, no new dependency.

## DESIGN

- **API answer**, test: `{ v, kind: "test", tests, summary, compile_error, stopped, diagnostics: [ … ] }`.
- **API answer**, format error: `{ v, kind: "format", error, stopped, diagnostics: [ … ] }`.
- Each diagnostic has the shape Run already returns: severity, code, message, file, span, help, `rendered`.
- **Known quirk, for `../lugha`:** `lughac test`'s diagnostics name the file `main.la` where `build`'s and `fmt`'s say `src/main.la`. The panel shows `rendered` as `lughac` wrote it. The editor marks lines by matching the file name, so `main.la` is read as `src/main.la` for those marks.

## CONTENT

None.

## TESTS

- [ ] Runner (`test/steps.la`): both commands carry `--diagnostics=json`, with arguments still a list.
- [ ] Runner (`test/outcome.la`): a test and a format result with JSON diagnostics on stderr give them back in `diagnostics`, and keep `compile_error`/`error`.
- [ ] Site (`api.test.ts`):
  - `readTest` and `readFormat` return the diagnostics;
  - an answer without them still gives the text state.
- [ ] e2e: in the Playground, code that doesn't compile shows `error[E…]` and its explanation under Format, and again under Tests.
- [ ] `scripts/hostile` and `scripts/content` pass on the rebuilt image.

## ACCEPTANCE

- [ ] The full suite passes (`npm test`, `check`, `build`, `e2e`; `lughac test src test`; `scripts/content`; `scripts/hostile`).
- [ ] For the owner, by eye: in the Playground, break a line, then press Format and Test. Each shows the error the way Run does.
