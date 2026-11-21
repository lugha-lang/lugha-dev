---
title: Function types
---

A function is a value too.
Its type is its signature without the names: `double` on line 1 is a `fun(i64): i64`, a function that takes an `i64` and gives back an `i64`.
Line 6 stores `double` in `f` without calling it, since there are no parentheses after it.
`apply` on line 3 takes a function, `f`, as its first parameter and calls it on `x`.
Press Run.

`10` comes from line 7, which calls `double` through `f`.
`42` comes from line 8, which passes `double` to `apply` by name, and `apply` calls it on `21`.
`<fun>` comes from line 9, which prints `f` itself through `.debug()`: that's a function's debug form.
Without `.debug()`, `console.println(f)` is E0422, as for an array.
Function values have no `==` either: `f == double` is E0404.
