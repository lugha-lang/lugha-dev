---
title: Running tests
start_failing: largest_of_none
---

`largest`, on lines 5 to 13 of `src/shapes.la`, should give the largest of an array of squares, or `None` for an empty one.
The test file checks both: `largest_of_none` on line 4 gives it an empty array, and `largest_of_two` on line 10 gives it two squares.
Press Test.

`largest_of_none` is `FAILED`, with the panic "index out of bounds: the length is 0 but the index is 0" at line 6 of `src/shapes.la`.
That line reads `squares[0]` before checking that there is one.
Each test runs as its own process, so `largest_of_two` still runs, and it's `ok`.
The last line, "2 tests: 1 passed, 1 failed", counts the whole run.
Run builds the program without its tests, so only Test runs them.
After line 5 of `src/shapes.la`, add `if squares.len == 0 { return None; }` on three lines and press Test again, or press Solve.
