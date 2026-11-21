---
title: Own methods and interface items
---

A type can have a method of its own and an interface's item with the same name.
`Circle` has its own `area` on line 8, in a plain `impl Circle`, and `Shape`'s `area` on line 12, in `impl Shape for Circle`.
Line 17 calls `c.area()`, and line 18 calls `Shape.area(c)`, naming the interface.
Press Run.

Line 17 prints `1.0`: `c.area()` runs the type's own method, `self.r * self.r`.
Line 18 prints `3.0`: `Shape.area(c)` runs the interface's item.
A `Shape` value holding `c`, such as `s` after `let s: Shape = c;`, runs the interface's item too: `s.area()` gives `3.0`.
