---
title: for … of loops
start_error: E0201
error_note: After `in`, a `for` loop expects a range like `0..3`, so `scores` reads as the start of one and `{` comes where `..` should be. A loop over an array uses `of` instead of `in`.
---

Line 3 tries to loop over `scores` with `for score in scores`, the way the Loops lesson counted over a range such as `0..3`.
Press Run.

The program doesn't run.
After `in`, `lughac` expects a range, so it reads `scores` as the start of one and looks for the `..` that should follow.
It finds `{` instead, and E0201 says "expected `..`, found `{`" at line 3, column 25.
A loop over an array uses `of` where a range uses `in`: `for score of scores` gives `score` each element in turn.
A `for … of` loop goes over the array as it was when the loop began.
So the loop's body may push onto a `let mut` array, and the loop still ends.
Change `in` to `of` on line 3 and run again, or press Solve.
