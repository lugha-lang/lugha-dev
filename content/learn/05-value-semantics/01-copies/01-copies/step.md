---
title: Copies
---

Line 4 makes a `Point` named `a`, and line 5 assigns it to `b`.
Assigning a struct, an array or an enum gives the new variable a copy of its own, so `b` starts as a copy of `a`.
Line 6 changes `b.x` to `9`.
Press Run.

Line 7 prints `a`, and it still has `x: 1`: changing `b` didn't touch it, because they are two separate values.
Line 8 prints `b`, with `x: 9`.
