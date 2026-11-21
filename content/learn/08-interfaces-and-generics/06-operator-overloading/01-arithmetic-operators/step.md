---
title: Arithmetic operators
start_error: E0404
---

An operator on a type of your own goes through an interface: `+` through `Add`, whose one method is `add`.
`-`, `*`, `/` and `%` go through `Sub`, `Mul`, `Div` and `Rem` the same way, and a leading `-` through `Neg`.
`Vec2` has an `add` of its own, in a plain `impl Vec2` on lines 3 to 5, and line 10 adds two `Vec2`s.
Press Run.

E0404 on line 10, "cannot apply `+` to Vec2", and on line 11, "cannot apply `+=` to Vec2".
As in Interfaces, a method with the right name isn't enough: `+` needs the `impl`.
Change `impl Vec2` on line 3 to `impl Add for Vec2`, or press Solve.
`b += a` on line 11 then works too, as `b = b + a`.
