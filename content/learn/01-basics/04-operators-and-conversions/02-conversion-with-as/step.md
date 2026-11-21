---
title: Conversion with as
start_error: E0401
---

Line 2 declares `total` as an `i32`, and line 3 tries to get half of it by dividing it by `2.0`.
Press Run.

The program doesn't run: E0401 says "float literal where i32 expected", pointing at the `2.0` on line 3.
The `2.0` takes its type from `total` on the other side of the `/`, as the `300` took its type from `height` in the last lesson, and a float can't be an `i32`.
So `total` has to become an `f64` first.
`as` converts a number to another type when nothing can be lost, and every `i32` has an exact `f64`.
`as` is worked out before `/`, so `total as f64 / 2.0` converts `total` and then divides.
Write `total as f64 / 2.0` in place of `total / 2.0` on line 3 and run again, or press Solve.
