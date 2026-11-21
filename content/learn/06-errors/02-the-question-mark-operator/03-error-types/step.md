---
title: Error types
start_error: E0424
error_note: The `?` on line 2 is on an `Option`, and a `None` has no error for `doubled` to return in its `Result`. Turn the `Option` into a `Result` first.
---

`?` returns a failure from the function it's in, so the failure has to fit that function's return type.
`doubled` on line 1 returns a `Result<i64, string>`, and line 2 uses `?` on the `Option` that `parse_i64` gives.
Press Run.

The program doesn't run, because a `None` has no error for `doubled` to return in an `Err`.
E0424 says "`?` can't return here", and its help suggests a `match`.
`ok_or("not a number")` is shorter: it turns the `Option` into a `Result`, with that string as its error, so `?` works.
A `Result`'s error type has to fit as well: in a function like `doubled`, `?` on a `Result<i64, i64>` is also E0424, and `map_err` can change the error first.
Add `.ok_or("not a number")` before the `?` on line 2 and run again, or press Solve.
