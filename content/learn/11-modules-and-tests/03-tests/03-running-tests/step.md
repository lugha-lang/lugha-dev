---
title: Running tests
start_failing: largest_of_none
---

`largest` in `shapes.la` should give the largest of an array of squares, or `None` for an empty one, and the test file checks both.
Press Test.

`largest_of_none` fails with a panic, "index out of bounds", but each test runs as its own process, so `largest_of_two` still runs and passes.
The last line, "2 tests: 1 passed, 1 failed", counts the whole run.
Run builds the program without its tests, so only Test runs them.
Line 6 of `shapes.la` reads `squares[0]` before checking that there is one.
After line 5 of `shapes.la`, add `if squares.len == 0 { return None; }`, on three lines, or press Solve, and press Test again.
