---
title: Multiple return values
---

A function can give back more than one value by returning a tuple.
`divmod` on line 1 gives back the quotient and the remainder of `a / b` together, so its return type is the tuple type `(i64, i64)`.
A tuple type lists each element's type, so step 1's `item` has the type `(string, i64)`.
Line 4 calls `divmod`, and `result` holds both values.
Press Run.

Line 5 prints `(3, 2)`: 17 divided by 5 is 3, with 2 left over.
