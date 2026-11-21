---
title: Function bounds
---

A function type can be a bound too: `F: fun(i64): i64` on line 3 takes any function of that signature.
`twice` calls `f` two times, and line 6 passes it the named function `double`, line 7 a closure.
A bound doesn't give a closure its parameter types, the way a parameter of a function type does, so line 7 writes `n: i64`: `fun(n) = n + 1` there is E0412.
Press Run.

Line 6 prints `20`, `5` doubled twice, and line 7 prints `7`, `5` plus one twice.
