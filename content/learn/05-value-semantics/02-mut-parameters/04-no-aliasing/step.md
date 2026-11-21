---
title: No aliasing
start_error: E0508
---

`add_to` on line 3 adds `other`'s count to `total`, which is a `mut` parameter.
Line 9 passes `c` as both, to double its count.
Press Run.

E0508: "cannot pass `c` as `mut` and also as another argument".
One variable can't be both the place a call changes and another argument of the same call.
As with `p.add(p)` in Methods, copy it first: put `let w = c;` on a line before the call and pass `w` on line 9, or press Solve.
