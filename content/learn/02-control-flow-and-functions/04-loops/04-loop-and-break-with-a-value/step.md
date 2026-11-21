---
title: loop and break with a value
---

`loop` runs its block again and again until something leaves it, usually a `break`.
Like `if` and `match`, it's an expression, and `break n;` on line 6 ends it with `n` as its value, which goes into `first`.
Line 4 doubles `n` each time round, and line 5 checks whether it has passed 100.
Press Run.

It prints `128`, the first doubling of 1 to pass 100.
Only a `loop` gives a value this way: `break` with a value inside a `while` or `for` is E0514 and won't compile, because those loops can also end without reaching a `break`.
