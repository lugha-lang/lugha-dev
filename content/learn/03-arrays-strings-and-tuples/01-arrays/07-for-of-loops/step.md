---
title: for … of loops
start_error: E0201
---

Line 3 loops over `scores` with `for score in scores`, the way the Loops lesson counted over a range.
Press Run.

After `in`, `lughac` wants a range such as `0..3`, so it reads `scores` as the start of one and gives E0201, "expected `..`, found `{`".
`of` goes through an array, giving each element in turn.
Change `in` to `of` on line 3, or press Solve.
A `let mut` array can grow inside its own loop: the loop goes over the array as it was when it began, so it still ends.
