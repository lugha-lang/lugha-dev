---
title: Error types
start_error: E0424
---

`?` returns a failure from the function it's in, so the failure has to fit that function's return type.
`doubled` on line 1 returns a `Result<i64, string>`, and line 2 uses `?` on the `Option` that `parse_i64` gives.
Press Run.

`lughac` stops at line 2 with E0424, "`?` can't return here".
A `None` has no error in it to return, and the help suggests a `match`, but `ok_or("not a number")` is shorter.
It turns the `Option` into a `Result`, with that string as its error, and then `?` works.
Add `.ok_or("not a number")` before the `?` on line 2, or press Solve.
On a `Result` the error type has to fit too: in this function, `?` on a `Result<i64, i64>` is E0424, "the error types must match: `i64` and `string`", and `map_err` can change the error first.
