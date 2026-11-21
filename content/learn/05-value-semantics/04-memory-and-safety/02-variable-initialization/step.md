---
title: Variable initialization
start_error: E0201
---

`total` on line 2 has a type but no value, and the loop adds each number to it.
Press Run.

`lughac` stops at line 2 with E0201, "expected `=`, found `;`".
A `let` always gives its variable a value, so no line can read one that was never set.
Add `= 0` after `i64` on line 2, or press Solve.
