---
title: Return values
start_error: E0503
---

`area`'s body is a block, so what it gives back is its last expression, as in Blocks and scopes.
Line 2 now ends with a `;`.
Press Run.

This time the `;` is an error, E0503, because line 1 promises an `i64` and the body no longer gives one.
Its help says to remove the semicolon: remove the `;` on line 2 and run again, or press Solve.
