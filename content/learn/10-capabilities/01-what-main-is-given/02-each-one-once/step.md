---
title: Each one once
start_error: E0304
error_note: `main` is given its parameters when the program starts, matched by type, and it can take each capability only once. Line 1 asks for a `Console` twice, as `console` and `out`.
---

Line 1 asks for two consoles, `console` and `out`.
Press Run.

The program doesn't run.
E0304 on line 1 lists everything `main` can take, each at most once: `string[]`, the capabilities, and the root `Scope`, which concurrent code uses.
It also says `main` returns `()` or `i32`, and its help shows a `main` that fits.
A parameter `main` can't be given at all, such as `n: i64`, is E0304 too.
Remove `, out: Console` from line 1 and run again, or press Solve.
