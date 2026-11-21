---
title: Struct literals
start_error: E0413
---

`Point { x: 3, y: 4 }` is a struct literal, and line 4 now writes one with only `x`.
Press Run.

There's no default: `lughac` gives E0413, "missing field `y` in `Point`".
A struct literal gives every field a value, in any order.
Add `, y: 0` after `x: 3` on line 4, or press Solve.
