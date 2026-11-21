---
title: Method calls on interface values
---

`s.area()` on a `Shape` runs the `area` of the type inside it.
The loop on lines 19 to 21 adds up `s.area()` for a circle and a square, each with its own `area`.
A `Shape` has only its methods, though: `shapes[0].r` would be E0410, "no field `r` on `Shape`", and its help says to use a type pattern to reach the value inside.
Press Run.

`7.0` is the circle's area, `3.0`, plus the square's, `4.0`.
