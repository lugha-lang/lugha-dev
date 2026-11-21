---
title: Reference counting
---

Step 1's array outlived `numbers`, so something has to give its memory back once nothing needs it.
Every variable, field or element that holds an array, a string or a box counts as one of its holders, and when the last one lets go, its memory is freed.
Line 4 makes a new array of 100 numbers on every pass, a hundred thousand in all, and only `row` holds it.
`row` is last used on line 5, at the end of the pass, so each array is freed there, before the next is made.
Press Run.

It prints `10000000`, and the program never had to say which arrays it was done with: the compiler puts in the counting.
