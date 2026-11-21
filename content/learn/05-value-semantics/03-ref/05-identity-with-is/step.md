---
title: Identity with is
start_error: E0404
error_note: Boxes have no `==`, so `a == b` is refused. Compare them with `is` to ask whether they're the same box, or compare what `get` gives to ask whether they hold the same value.
---

`b` on line 3 is a copy of `a`, so the two name one box, and `c` on line 4 is a second box that also holds `1`.
Lines 5 and 6 compare them with `==`.
Press Run.

The program doesn't run.
Boxes have no `==`, so E0404 says it "cannot apply `==` to `Ref<i64>`", once for line 5 and once for line 6.
The help under each gives the two ways to compare boxes: `a.is(b)` says whether both name the same box, and `a.get() == b.get()` compares what's inside.
To see which names share a box, change `a == b` to `a.is(b)` on line 5 and `a == c` to `a.is(c)` on line 6, then run again, or press Solve.
