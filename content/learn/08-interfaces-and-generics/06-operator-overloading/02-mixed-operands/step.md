---
title: Mixed operands
---

`Add` alone means `Add<Vec2>`, with a `Vec2` on both sides; `Mul<f64>` says the right-hand operand is an `f64`.
A type can have one block for each right-hand type: `Mul<f64>` on line 3 scales the vector, and `Mul<Vec2>` on line 7 gives a number.
For a number before `*`, `impl Mul<Vec2> for f64` on line 11 makes `2.0 * v` work too: its `mul` on line 12 turns the operands round and uses line 3's block.
`Mul` and `f64` both come with the language, yet line 11's block is allowed, since a block like this may also live where its right-hand type, `Vec2`, is declared.
Press Run.

Lines 17 and 18 print the same scaled vector.
Line 19 prints `5.0`, from line 7's block.
Line 20 calls `mul` by name, which picks the same block as `v * 2.0`.
The right-hand operand picks a block by its exact type: `v * 2` would be E0404, "no `impl Mul` of `Vec2` takes this operand", since `2` is an integer.
