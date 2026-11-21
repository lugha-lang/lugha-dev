---
title: Variable initialization
start_error: E0201
error_note: A `let` has to give its variable a value with `=`, and line 2 ends after the type, so `lughac` found `;` where the `=` should be.
---

`total` on line 2 has a type but no value, and the loop on lines 3 to 5 adds each number to it.
Press Run.

The program doesn't run.
A `let` always gives its variable a value, so no line can read one that was never set.
E0201 stops at line 2: it expected `=` and found `;`.
Add `= 0` after `i64` on line 2 and run again, or press Solve.
