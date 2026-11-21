---
title: map and and_then
---

`map` on an `Option` calls its closure on what a `Some` holds and gives back a new `Some` with the result, and leaves a `None` as it is.
On a `Result`, `map` works the same way on an `Ok` and leaves an `Err` as it is, the other way round from `map_err`.
`and_then` takes a closure that returns an `Option` or a `Result` itself, so the closure decides whether the answer is a success or a failure.
Line 9 writes its closure's return type, `Result<i64, string>`: a closure that gives back `Ok` or `Err` to a `Result`'s `and_then` needs it written, or `lughac` stops with E0412.
Press Run.

Line 2 prints `Some(42)`: `parse_i64("21")` gives `Some(21)`, and `map` doubles it.
Line 3 prints `None`, since `"x"` isn't a number.
Lines 6 and 7 print `Ok(5)` and `Err("no")`: only the `Ok` changed.
Line 8 prints `None`, because the closure returns `None` for `-3`.
Line 9 prints `Err("too small")`, because `good` holds `4`, which isn't more than `9`.
