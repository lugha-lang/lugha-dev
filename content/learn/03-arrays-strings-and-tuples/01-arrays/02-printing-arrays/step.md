---
title: Printing arrays
start_error: E0422
error_note: `console.println` prints only values with a text form of their own, and an array has none. `.debug()` turns the array into a string that shows its elements.
---

Lines 4 and 5 now give `console.println` the arrays themselves.
Press Run.

This time the program doesn't run.
`console.println` prints only values that have a text form of their own, and an array has none.
The first E0422 says so for `scores` on line 4: `i64[]` doesn't implement `Display`, the text form `console.println` needs.
The second says the same for `zeros` on line 5.
Each help names the way out: `.debug()` gives an array's debug form, a string that shows its elements the way a programmer reads them, and `console.println` can print that.
Add `.debug()` after `scores` on line 4 and after `zeros` on line 5, then run again, or press Solve.
