---
title: Conversion with as
start_error: E0401
---

To get half of `total`, an `i32`, line 3 divides it by `2.0`.
Press Run.

`lughac` refuses it with E0401.
The `2.0` takes its type from `total` on the other side of the `/`, as the `300` did in the last lesson, and a float can't be an `i32`.
`as` converts a number to another type when nothing can be lost, and every `i32` has an exact `f64`.
Write `total as f64 / 2.0` on line 3 and run again, or press Solve: `as` is worked out before `/`, so `total` is converted first.
