---
title: Interface values
start_error: E0403
---

An interface is also a type, and a `Shape` value can hold a value of any type that implements `Shape`.
`describe` in Interfaces took one as a parameter.
Line 17 puts a circle and a square in one array.
Press Run.

`lughac` stops at line 17 with E0403, "expected Circle, found Square": the array takes its type from its first element.
A value becomes a `Shape` only where a `Shape` is expected, so write the array's type: add `: Shape[]` after `shapes` on line 17, or press Solve.
The debug form of a `Shape` is the value inside it.
