---
title: Writing an item by hand
start_error: E0463
---

A type can write an interface by hand, with an `impl` block, instead of deriving it.
`Author` on line 21 asks for `Describe` with `with`, and `impl Describe for Author` on lines 23 to 25 writes its own.
Press Run.

The program doesn't run.
A type gets each interface one way, from the blocks or by hand, never both.
E0463 says so on line 21: "`Author` both derives and implements `Describe`".
Its help says to keep one.
Keep the `impl`: it then replaces the blocks for `Author`, and `Book` keeps them.
Remove `with Describe` from line 21 and run again, or press Solve.
