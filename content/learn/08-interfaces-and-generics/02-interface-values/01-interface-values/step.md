---
title: Interface values
start_error: E0403
error_note: An array takes its type from its first element, so line 17's array is a `Circle[]`, and a `Square` doesn't fit. Written as a `Shape[]`, it turns each element into a `Shape`.
---

An interface is also a type, and a `Shape` value can hold a value of any type that implements `Shape`.
Line 17 puts a circle and a square in one array, and line 18 prints it.
Press Run.

The program doesn't run.
An array takes its type from its first element, so this one is a `Circle[]`, and a `Square` can't go in it.
E0403 says so at the square on line 17: "expected Circle, found Square".
A value becomes a `Shape` only where a `Shape` is expected, so write the array's type.
Line 18 will then print each `Shape` through its debug form, which is the value inside it.
Add `: Shape[]` after `shapes` on line 17 and run again, or press Solve.
