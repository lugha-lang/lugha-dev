---
title: Each one once
start_error: E0304
---

Line 1 asks for two consoles, `console` and `out`.
Press Run.

`lughac` gives E0304: `main` takes each capability at most once, and nothing else except `string[]` and the root `Scope`, which Concurrency uses.
A parameter `main` can't be given, such as `n: i64`, is E0304 too.
Remove `, out: Console` from line 1, or press Solve.
