---
title: Methods
---

A method is a function that belongs to a type, declared inside an `impl` block for it, as on lines 3 to 5.
Its first parameter is `self`, the value the method is called on, written without a type.
Line 9 calls it with a dot, `p.length_squared()`, so inside the method `self` is `p`.
Press Run.

It prints `25`, which is `3 * 3 + 4 * 4`.
