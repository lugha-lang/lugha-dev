---
title: Nested patterns
---

`describe` on line 7 takes an `Option<Shape>`, an `Option` that may hold a shape.
In `.Some(.Circle(r))` on line 9, the data inside the `Some` is matched with a pattern of its own, with its own dot.
That arm matches only a `Some` holding a circle, and names its radius `r`.
Lines 9 to 11 cover each shape inside a `Some`, and line 12 covers `.None`.
Line 18 pops the one circle from `shapes`, and line 19 pops again from the array, empty by then.
Press Run.

Line 18 prints `a circle of radius 1.5`, from the arm on line 9.
Line 19's `pop` gives `None`, so it prints `nothing`.
