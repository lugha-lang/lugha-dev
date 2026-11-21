---
title: The loop's copy
---

Line 2 makes `it`, an iterator over three numbers.
The loop on lines 3 to 5 goes through every value, and lines 6 and 7 use `it` again afterwards.
Press Run.

The loop prints `1` to `3`.
A loop like line 3's, `for x of it`, works on a copy of the iterator, as a helper does, so `it` is unchanged after the loop.
That's why `count()` on line 6 still finds three values, and `take(1)` on line 7 still starts from `1`.
