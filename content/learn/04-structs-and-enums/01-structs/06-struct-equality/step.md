---
title: Struct equality
start_error: E0422
error_note: `==` works on a struct only when its declaration asks for it, and `Point`'s doesn't. `with Eq` after the declaration lets two points be compared, field by field.
---

Line 6 compares two points with `==`.
Press Run.

The program doesn't run.
`==` and `!=` need a type that implements `Eq`, and E0422 says `Point` doesn't, at line 6.
The help's first way out is `with Eq` after `Point`'s declaration.
That gives `Point` both `==` and `!=`, and `==` then compares two points field by field.
Add `with Eq` after the `}` on line 1 and run again, or press Solve.
