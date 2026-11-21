---
title: Associated functions and Self
---

A function in an `impl` block without `self` is an associated function, and it's called on the type's name, as `Point.new(3, 4)` on line 10.
`new` is an ordinary name, chosen by whoever writes the type, and here it builds a `Point` from its two fields.
Inside the `impl`, `Self` stands for `Point`, both as a type and before a struct literal, as on line 4.
`origin` on line 6 calls `new` the same way, as `Self.new(0, 0)`.
Press Run.

Line 10 prints `Point { x: 3, y: 4 }`, and line 11 prints `Point { x: 0, y: 0 }`, the point `origin` builds.
