---
title: Boolean conditions
start_error: E0403
---

`unread` is `3`, and line 3 uses it as the condition.
Press Run.

`lughac` gives E0403 again, the code for a value of the wrong type, this time "expected bool, found i64".
A condition must be a `bool`, and a number is never read as one, so the comparison with `0` has to be written out.
Write `unread > 0` on line 3 and run again, or press Solve.
