---
title: Boolean conditions
start_error: E0403
error_note: An `if`'s condition has to be a `bool`, `true` or `false`. `unread` is an `i64`, and a number is never read as a `bool`.
---

`unread` is `3`, and line 3 uses it as the `if`'s condition.
Press Run.

The program doesn't run: E0403 again, the code for a value of the wrong type, this time "expected bool, found i64", pointing at `unread` on line 3.
A condition must be a `bool`, and a number is never read as one, so the comparison with `0` has to be written out.
Write `unread > 0` on line 3 and run again, or press Solve.
