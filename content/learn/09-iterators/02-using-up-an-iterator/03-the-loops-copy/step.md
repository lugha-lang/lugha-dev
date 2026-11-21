---
title: The loop's copy
---

The loop on lines 3 to 5 goes through every value, and lines 6 and 7 use `it` again afterwards.
Press Run.

A plain `for … of`, without `mut`, works on a copy of the iterator, as a helper does: `it` is unchanged, so `count()` still finds three values and `take(1)` still starts from `1`.
