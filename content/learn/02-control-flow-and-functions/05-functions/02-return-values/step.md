---
title: Return values
start_error: E0503
error_note: Line 1 says `area` gives back an `i64`, but the `;` on line 2 throws `width * height` away, so the body ends with no value to give back.
---

`area`'s body is a block, so what it gives back is its last expression.
Line 2 now ends with a `;`.
Press Run.

The program doesn't run: E0503 says "`area` may end without returning a value of type i64", pointing at the name `area` on line 1.
Returning a value means giving it back.
Line 1 promises an `i64`, but the `;` makes `width * height` a statement, which throws its value away, so the body no longer gives one.
The help line says the same, "remove this semicolon to make it the result", though its location points at `area`: the semicolon is the one on line 2.
Remove the `;` on line 2 and run again, or press Solve.
