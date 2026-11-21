---
title: Struct literals
start_error: E0413
---

`Point { x: 3, y: 4 }` is a struct literal: the type's name, then a value for each field, in braces.
Line 4 now writes one with only `x`.
Press Run.

The program doesn't run.
A field has no default value, so a struct literal has to give every field one, in any order.
E0413 says "missing field `y` in `Point`", at line 4.
Add `, y: 0` after `x: 3` on line 4 and run again, or press Solve.
