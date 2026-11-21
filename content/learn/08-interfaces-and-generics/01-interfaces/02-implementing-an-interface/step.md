---
title: Implementing an interface
start_error: E0422
---

`describe` on line 13 takes any `Shape`, and line 16 passes it a `Circle`.
This time `Circle`'s methods on lines 8 to 11 are in a plain `impl Circle`, with the same names and signatures as `Shape`'s.
Press Run.

E0422: "`Circle` doesn't implement `Shape`".
Having methods with the right names isn't enough: a type implements an interface only through an `impl Shape for …` block.
Change `impl Circle` on line 8 to `impl Shape for Circle`, or press Solve.
An `impl Shape for Circle` that leaves a method out is E0422 too, at the block, and its help names the missing method.
