---
title: Multiple return values
---

A function can give back more than one value by returning a tuple.
`divmod` on line 1 gives back the quotient and the remainder together, so its return type is the tuple type `(i64, i64)`.
A tuple type lists each element's type, so step 1's `item` has the type `(string, i64)`.
Press Run.

The caller gets both at once, and the next step names them.
