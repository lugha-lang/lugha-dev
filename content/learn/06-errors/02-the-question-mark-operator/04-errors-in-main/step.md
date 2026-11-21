---
title: Errors in main
start_error: E0424
---

`main` gives back nothing or an `i32` exit code, never a `Result`, so a `?` in it has no way to return an `Err`.
Line 7 uses `?` there anyway.
Press Run.

E0424 again: the help says `main` can't return an error, and to handle it with `match`.
Replace lines 7 to 9 with a `match` on `doubled("x")`, with no `;` after it, so that it's `main`'s last expression and its value is the exit code.
Its `.Ok(n)` arm is a block that prints `n` with `console.println` and ends with `0`, as the `.Some(mut n)` arm in mut bindings was a block.
Its `.Err(e)` arm is a block that prints `"error: {e}"` and ends with `1`, the exit code for a failure.
Write that `match`, or press Solve.
