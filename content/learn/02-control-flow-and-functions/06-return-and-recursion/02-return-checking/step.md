---
title: Return checking
start_error: E0503
error_note: `distance` promises an `i64`, and `lughac` never counts an `if` without an `else` as returning, whatever its condition. So it sees a way past both `if`s to the `}` on line 8 with no value to give back.
---

Now the body is two `if`s, on lines 2 and 5, each holding a `return`, and every call takes one of them, since `to` is either smaller than `from` or not.
Press Run.

The program doesn't run: E0503 says "`distance` may end without returning a value of type i64".
An `if` without an `else` never counts as returning, whatever its condition, so `lughac` sees a way to reach the `}` on line 8 with nothing to give back.
The help line gives two ways out: end the body with a value, or `return` on every path.
An `if` with an `else` would count when both branches return.
Replace lines 5 to 7 with `to - from` and run again, or press Solve.
