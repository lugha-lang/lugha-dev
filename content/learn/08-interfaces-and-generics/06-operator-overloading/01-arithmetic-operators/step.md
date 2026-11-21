---
title: Arithmetic operators
start_error: E0404
error_note: `+` on a type of your own needs an `impl Add` block. `Vec2` has an `add` method, but in a plain `impl Vec2`, which doesn't count.
---

An operator on a type of your own goes through an interface: `+` through `Add`, whose one method is `add`.
`-`, `*`, `/` and `%` go through `Sub`, `Mul`, `Div` and `Rem` the same way, and a leading `-` through `Neg`.
`Vec2` has an `add` of its own, in a plain `impl Vec2` on lines 3 to 5, and line 10 adds two `Vec2`s.
Press Run.

The program doesn't run.
As for any interface, a method with the right name isn't enough: `+` needs an `impl Add` block.
E0404 says so on line 10, "cannot apply `+` to Vec2", and on line 11, "cannot apply `+=` to Vec2".
Both helps name the block to write, `impl Add<…> for Vec2`; `Add` alone means a `Vec2` on both sides, which is what's needed here.
With it, `b += a` on line 11 works too, as `b = b + a`.
Change `impl Vec2` on line 3 to `impl Add for Vec2` and run again, or press Solve.
