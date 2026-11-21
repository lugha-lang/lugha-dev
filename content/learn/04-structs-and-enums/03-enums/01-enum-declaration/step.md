---
title: Enum declaration
start_error: E0207
---

An enum is a type whose value is one of a list of variants.
`Shape` on lines 1 to 5 is a circle with a radius, a rectangle with a width and height, or empty.
Each variant lists the types of the data it carries, if any.
Line 8 builds a circle with `Shape::Circle(2.0)`.
Press Run.

`lughac` stops at E0207, "`::` is not Lugha syntax".
A variant is built through its enum's name and a dot, as `Shape.Rect` is on line 9.
A variant with no data, like `Shape.Empty` on line 12, has no parentheses.
Change `::` to `.` on line 8, or press Solve.
A variant's debug form is its name and its data, without the enum's name.
