---
title: Enum declaration
---

An enum is a type whose value is one of a list of variants.
`Shape` on lines 1 to 5 is a circle with a radius, a rectangle with a width and height, or empty.
Each variant lists the types of the data it carries, if any.
A variant is built through its enum's name and a dot, as `Shape.Circle(2.0)` on line 8 and `Shape.Rect(1.0, 2.0)` on line 9.
A variant with no data, like `Shape.Empty` on line 12, has no parentheses.
Press Run.

A variant's debug form is its name and its data, without the enum's name.
