---
title: Early return
---

So far a function's value has been its last expression.
`return` ends a function straight away and gives back the value after it.
In `distance`, line 2 checks whether `to` is smaller than `from`, and if it is, line 3 returns `from - to` and the rest of the body is skipped.
Otherwise the function goes on to line 5, its last expression.
Press Run.

It prints `7` twice.
Line 9's call goes on to line 5, and line 10's returns on line 3.
`return to - from;` on line 5 would work too, but a function that reaches its end gives back its last expression without needing `return`.
