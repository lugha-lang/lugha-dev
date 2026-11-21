---
title: Errors in main
start_error: E0424
error_note: `main` returns an exit code, not a `Result`, so the `?` on line 7 can't return an `Err`. Use a `match` instead.
---

`main` on line 6 returns an `i32` exit code, and line 7 uses `?` on what `doubled("x")` gives.
Press Run.

The program doesn't run.
`main` gives back nothing or an exit code, never a `Result`, so a `?` in it has no way to return an `Err`.
E0424's help says to handle it with `match`.
Replace lines 7 to 9 with a `match` on `doubled("x")`, with no `;` after it, so that it's `main`'s last expression and its value is the exit code.
An arm can be a block: `{` after the `=>`, its lines, then the value on a last line without `;`, then `}`; no comma is needed after it.
The `.Ok(n)` arm's block prints `n` and ends with `0`.
The `.Err(e)` arm's block prints `"error: {e}"` and ends with `1`, a failure's exit code.
Write it and run again, or press Solve.
