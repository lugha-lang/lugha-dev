---
title: Printing arrays
start_error: E0422
---

Lines 4 and 5 now print the arrays themselves.
Press Run.

`lughac` gives E0422 for both: an array has no text of its own to print.
`.debug()` gives an array's debug form, the way a programmer reads it, as a string `console.println` can print.
Add `.debug()` after `scores` on line 4 and after `zeros` on line 5, or press Solve.
