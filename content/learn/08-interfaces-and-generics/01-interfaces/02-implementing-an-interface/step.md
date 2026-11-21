---
title: Implementing an interface
start_error: E0422
error_note: `describe` takes a `Shape`, and `Circle` isn't one until an `impl Shape for Circle` block says so. Methods with the same names in a plain `impl Circle` don't count.
---

`describe` on line 13 takes any `Shape`: its parameter's type is the interface, so it takes a value of any type that implements it.
Line 16 passes it a `Circle`.
This time `Circle`'s methods on lines 8 to 11 are in a plain `impl Circle`, with the same names and signatures as `Shape`'s.
Press Run.

The program doesn't run.
Having methods with the right names isn't enough: a type implements an interface only through an `impl Shape for …` block.
E0422 says so on line 16, where the `Circle` is passed: "`Circle` doesn't implement `Shape`".
Its help names the block to add.
An `impl Shape for Circle` that leaves a method out is E0422 too, at the block, and its help names the missing method.
Change `impl Circle` on line 8 to `impl Shape for Circle` and run again, or press Solve.
