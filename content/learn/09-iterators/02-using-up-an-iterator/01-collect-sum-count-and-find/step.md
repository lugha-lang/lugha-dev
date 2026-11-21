---
title: collect, sum, count and find
---

Some helpers use an iterator up: they pull its values and give back one answer instead of another iterator.
`sum()` and `count()` on lines 3 and 4 add the values up and count them.
`find` on line 5 gives the first value its closure returns `true` for, as an `Option`, since there may be none.
`min`, `max` and `position` on lines 6 to 8 give `Option`s for the same reason.
`collect()` on line 9, after a `filter`, is one of them too, and `fold`, `any` and `all` from Array helpers work on iterators as well.
Every line uses the same `scores`.
Press Run.

Each helper works on its own copy of the iterator, so every line starts again from `7`, and `count()` still finds four values.
