---
title: Mixed operands
---

`Add` alone means `Add<Vec2>`, a `Vec2` on both sides; `Mul<f64>` says the right-hand operand is an `f64`.
A type can have one block for each right-hand type: `Mul<f64>` on line 3 scales the vector, and `Mul<Vec2>` on line 7 gives a number.
For a number before `*`, `impl Mul<Vec2> for f64` on line 11 makes `2.0 * v` work too, and its `mul` on line 12 turns the operands round and uses line 3's block.
`Mul` and `f64` both come with the language, but a block like this may also be written where its right-hand type is declared, and `Vec2` is declared here.
`v.mul(2.0)` on line 20 calls the method by name, and picks the same block as `v * 2.0`.
Press Run.

The right-hand operand picks a block by its exact type: `v * 2` would be E0404, "no `impl Mul` of `Vec2` takes this operand", since `2` is an integer.
