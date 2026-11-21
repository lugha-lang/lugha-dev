---
title: Variants as functions
---

A variant that carries data is a function value too: `Shape.Circle` takes an `f64` and gives back a `Shape`, so it's a `fun(f64): Shape`.
`apply_all` on line 6 takes such a function as `make`, and line 9 calls it on each size.
Lines 15 and 16 pass `Shape.Circle` and `Shape.Square` to it without calling them.
`Some`, `Ok` and `Err` are function values the same way, once a written function type says what they hold, as `wrap`'s type does on line 17.
Press Run.

Line 15 prints the two circles `apply_all` made, line 16 the one square, and line 18 `Some(2.0)`, from calling `Some` through `wrap`.
A struct's associated function, such as `Point.new`, is a value the same way.
