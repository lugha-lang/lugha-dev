---
title: Identity with is
start_error: E0404
---

`b` on line 3 is a copy of `a`, so the two name one box, and `c` on line 4 is a second box that also holds `1`.
Lines 5 and 6 compare them with `==`.
Press Run.

That's E0404 again, "cannot apply `==` to `Ref<i64>`", with the help from the last step.
Boxes have no `==`.
`a.is(b)` says whether both name the same box, and `a.get() == b.get()` compares what's inside.
To see which names share a box, change `a == b` to `a.is(b)` on line 5 and `a == c` to `a.is(c)` on line 6, or press Solve.
