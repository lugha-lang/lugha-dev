---
title: Generic impl blocks
---

Methods for a generic type go in an `impl` block that names its parameter after `impl`, as `impl<T> Stack<T>` on line 3 does.
There `T` stands for the element type, and `Self` for `Stack<T>`.
Line 23's `Stack<i64>` fills in `T` for `Stack.new()`, as `: string[]` did for `empty`.
A second block, `impl<T: Num> Stack<T>` on line 18, adds a bound, so `total` exists only for stacks of numbers.
Press Run.

`total`'s `0` is a `T`, as `Num` allows, and calling `total` on `words` would be E0419, "`string` doesn't satisfy `Num`", the code for a built-in type that misses a bound.
