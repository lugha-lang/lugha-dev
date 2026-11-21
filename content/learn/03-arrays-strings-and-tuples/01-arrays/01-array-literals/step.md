---
title: Array literals
---

An array holds values of one type, in order.
Line 2 writes one as a list in square brackets.
Line 3 uses the other form, `[value; count]`: four elements, each a copy of `0`.
`.len` is the number of elements, written without parentheses, and lines 4 and 5 print it for each array.
Press Run.

The output panel shows `3` for `scores` and `4` for `zeros`, then "Exited with code 0".
`scores` has the type `i64[]`, an array of `i64`: nothing gives its numbers a type, so they're `i64`.
