---
title: Function types
---

A function is a value too, and its type is its signature without the names: `double` on line 1 is a `fun(i64): i64`.
Line 6 stores `double` in `f` without calling it, and line 7 calls it through `f`.
`apply` on line 3 takes a function as a parameter, and line 8 passes it `double` by name, as `update` took `add_one` in Ref.
Line 9 prints `f` itself, through `.debug()`.
Press Run.

A function's debug form is `<fun>`, and `console.println(f)` without `.debug()` is E0422, as for an array.
Function values have no `==`: `f == double` is E0404.
