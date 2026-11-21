---
title: Arrays of functions
---

Functions can sit in an array like any other value.
`steps` on line 6 holds three of them.
Its type, `(fun(i64): i64)[]`, needs the parentheses, because `fun(i64): i64[]` is a function that returns an array.
The loop on line 8 goes over them in order, and line 9 calls each one as `step(n)` and keeps the result in `n`.
Press Run.

`n` starts at `3`: `double` makes it `6`, `square` makes it `36`, and `negate` makes it `-36`, which line 11 prints.
