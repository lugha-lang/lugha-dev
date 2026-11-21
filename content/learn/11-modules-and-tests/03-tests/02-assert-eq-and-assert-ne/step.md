---
title: assert_eq and assert_ne
start_failing: area_of_three
---

`assert` only says that it failed, so line 6 of `test/shapes_test.la` uses `assert_eq(a, b)` instead, which fails unless `a` and `b` are equal.
`assert_ne` on line 13 fails if they are equal.
When `assert_eq` fails, it shows both values, the first as left and the second as right.
When `assert_ne` fails, it shows the value both have.
In `src/shapes.la`, `area` on line 3 multiplies the side by `2.0`.
Press Test.

`area_of_three` is `FAILED`, and the line under it gives the panic: "assert_eq failed: left 6.0, right 9.0".
`area` gave 6.0, and the test expects 9.0.
`at shapes_test.la:6:5` is line 6 of the test file, where `assert_eq` was called.
`bigger_side_bigger_area` is `ok`, since the two areas still differ, and the last line counts 2 tests: 1 passed, 1 failed.
A square's area is its side multiplied by itself, not by `2.0`.
Change `2.0` to `s.side` on line 3 of `src/shapes.la` and press Test again, or press Solve.
