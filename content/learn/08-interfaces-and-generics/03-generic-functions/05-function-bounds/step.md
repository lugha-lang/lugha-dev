---
title: Function bounds
---

A function type can be a bound too: `F: fun(i64): i64` on line 3 takes any function of that signature.
`twice` calls `f` two times, and line 6 passes it the named function `double`, line 7 a closure.
A named function or a closure written in the call gets a version of `twice` of its own, which calls that function directly.
A bound doesn't give a closure its parameter types the way `apply`'s function type did in Closures, so line 7 writes `n: i64`: `fun(n) = n + 1` there is E0412.
Press Run.
