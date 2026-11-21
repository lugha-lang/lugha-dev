---
title: No aliasing
start_error: E0508
error_note: `total` changes `c` itself, and `other` reads `c` where it is, so `add_to` would see its own change to `total` through `other`. Copy `c` first and pass the copy as `other`.
---

`add_to` on line 3 adds `other`'s count to `total`, its `mut` parameter.
Line 9 passes `c` as both arguments, to double its count.
Press Run.

The program doesn't run.
A `mut` parameter works on the caller's variable itself.
Without `mut`, a parameter acts as a copy because the function can't change it, but a struct isn't actually copied: the function reads it where it is.
So with `c` as both, `add_to` would change `c` through `total` and see that change through `other`.
E0508 says `c` can't be passed as `mut` and also as another argument, and its help says to copy it first, so the call reads a value that doesn't change.
Put `let w = c;` on a line before line 9 and pass `w` as the second argument, then run again, or press Solve.
