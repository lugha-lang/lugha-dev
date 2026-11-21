---
title: Return checking
start_error: E0503
---

Now the `if`s on lines 2 and 5 each hold a `return`, and every call takes one of them, since `to` is either smaller than `from` or not.
Press Run.

It gives E0503, "`distance` may end without returning a value of type i64", with the help "end the body with a value, or `return` on every path".
An `if` without an `else` never counts as returning, whatever its condition, so `lughac` sees a way to reach the last `}` with nothing to give back.
An `if` with an `else` counts when both branches return.
Replace lines 5 to 7 with `to - from`, or press Solve.
