---
title: Statements and ()
start_error: E0422
---

Now line 5 ends with a `;`.
Press Run.

It doesn't compile: W0106 warns that `total` holds `()`, and E0422 on line 7 is the error, because `()` can't be printed.
A `;` turns an expression into a statement and throws its value away, so the block has no last expression.
A block like that gives `()`, the value that means nothing was given back.
The help's `.debug()` would print it; it comes in Arrays.
Remove the `;` on line 5 and run again, or press Solve.
