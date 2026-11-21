---
title: collect, sum, count and find
---

Some helpers use an iterator up: they pull its values and give back one answer instead of another iterator.
Line 2 makes `scores`, an iterator over four numbers, and every line after it uses the same `scores`.
Lines 3 and 4 add the values up with `sum()` and count them with `count()`.
`find` on line 5 gives the first value its closure returns `true` for, as an `Option`, since there may be none.
`min`, `max` and `position` on lines 6 to 8 give an `Option` for the same reason.
Line 9 ends a `filter` with `collect()`, another of these helpers.
Press Run.

Each helper works on its own copy of the iterator, so every line starts again from `7`.
The sum is `23`, and `count()` still finds four values.
`find` gives `Some(9)`, the first score above 8, and `min` and `max` give `Some(3)` and `Some(9)`.
`position` gives `Some(2)`: `9` is at position 2, counting from 0.
The last line holds the scores above 5.
