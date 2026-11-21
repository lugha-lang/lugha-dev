---
title: Generic structs
start_error: E0418
---

A struct can take a type parameter as a function does: `Pair<T>` on line 1 holds two values of one type, `T`.
Line 6 builds a pair of numbers and line 7 a pair of strings, and `T` comes from the fields, as it came from a function's arguments.
In a type, though, a generic struct is written with its argument, as in `Pair<i64>`.
Line 3 writes a bare `Pair` as a type twice, for `p` and for what `swap_pair` gives back.
Press Run.

Both of line 3's `Pair`s are E0418, "`Pair` takes 1 type argument but 0 were given".
`swap_pair` is called with both pairs, so it has to be generic itself.
On line 3, add `<T>` after `swap_pair` and write `Pair<T>` for the parameter's type and the return type, or press Solve.
The `Pair { … }` after `=` stays as it is: it takes `T` from its fields, as line 6 does.
