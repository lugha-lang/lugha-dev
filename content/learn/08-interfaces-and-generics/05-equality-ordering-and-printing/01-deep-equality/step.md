---
title: Deep equality
---

`==` reaches into a value's parts, so line 4 compares two `Point`s field by field, which `with Eq` on line 1 allows.
Arrays compare element by element, as on lines 5 and 6, and `Some(a)` equals `Some(b)` when `a` equals `b`.
Line 7 divides zero by zero, which gives a float that isn't a number, `NaN`, and line 8 compares it with itself.
A `Ref` box, a function and an interface value have no `==`, and nor does an array or an `Option` that holds one.
Press Run.

Lines 4 to 6 print `true`: the parts match on lines 4 and 5, and `[3]` and `[4]` differ on line 6, which uses `!=`.
Line 8 prints `false`: `NaN` is equal to nothing, itself included.
`==` works on a value only when each of its parts has `Eq`: comparing two arrays of `Point`s, with no `with Eq` on `Point`, is E0422, naming `Point`.
