---
title: Writing an item by hand
start_error: E0463
---

A type can write an interface by hand instead of deriving it, as in Interfaces.
`Author` on line 21 asks for `Describe` with `with`, and `impl Describe for Author` on lines 23 to 25 writes its own.
Press Run.

E0463: "`Author` both derives and implements `Describe`".
A type gets each interface one way, from the blocks or by hand, never both.
Remove `with Describe` from line 21, or press Solve: the `impl` then replaces the blocks for `Author`, and `Book` keeps them.
