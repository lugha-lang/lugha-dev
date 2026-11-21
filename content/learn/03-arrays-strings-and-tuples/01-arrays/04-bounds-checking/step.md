---
title: Bounds checking
start_output: 70\n
---

Line 3 prints the first score, `scores[0]`.
Line 4 tries to print the last one with `scores[scores.len]`, and `scores.len` is `3`.
Press Run.

This program compiles and starts, and line 3 prints `70`.
Then line 4 asks for index 3, and there's no element there: the three elements are at indexes 0, 1 and 2.
The program panics, stopping with "index out of bounds: the length is 3 but the index is 3" and where it happened, `src/main.la:4:27`.
It exits with code 101.
The last index is always `.len - 1`.
Change line 4's index to `scores.len - 1` and run again, or press Solve.
