---
title: assert_eq and assert_ne
start_failing: area_of_three
---

`assert` only says that it failed, so line 6 of `test/shapes_test.la` uses `assert_eq(a, b)` instead, which fails unless `a` and `b` are equal.
`assert_ne` on line 13 fails if they are equal.
When they fail, `assert_eq` prints both values, the first as left, and `assert_ne` the value both have.
`area` on line 3 of `shapes.la` isn't the one from Test functions.
Press Test.

`area_of_three` fails with "assert_eq failed: left 6.0, right 9.0": `area` gave 6.0, and the test expects 9.0.
The failure names line 6 of the test file, where `assert_eq` was called.
Line 3 of `shapes.la` multiplies the side by `2.0` instead of by itself.
Change `2.0` to `s.side` on line 3 of `shapes.la`, or press Solve, and press Test again.
