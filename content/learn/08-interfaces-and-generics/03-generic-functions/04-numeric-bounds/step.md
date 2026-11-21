---
title: Numeric bounds
start_error: E0401
---

Arithmetic on a `T` needs a bound too: `T: Num` allows it, along with `==`, `<`, and an integer literal where a `T` goes.
So `total` starts its sum from `0` on line 2 and adds up `i64`s and `f64`s alike.
`half` on line 9 multiplies by `0.5`, a float literal, but a `Num` can be an integer type too.
Press Run.

`lughac` stops at line 9 with E0401, "float literal where T expected".
`T: Float` is met only by `f32` and `f64`, and allows everything `Num` does as well as float literals.
Change `Num` to `Float` on line 9, or press Solve.
