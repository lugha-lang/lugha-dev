---
title: Chaining iterators
---

Iterators have `map` and `filter` too, and each gives back another iterator, so they line up one after another.
Line 2 starts from `range(1, 10)`, the numbers 1 to 9, keeps the multiples of 3 with `filter`, and squares them with `map`.
`collect()` at the end of the line puts the results in an array.
On line 4, `chain` gives the values of `[1, 2].iter()`, then those of `[3, 4].iter()`, and `collect()` gathers them too.
Press Run.

The first line is the squares of 3, 6 and 9.
The second holds both arrays' items in one array.
