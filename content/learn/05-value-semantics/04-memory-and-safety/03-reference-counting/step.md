---
title: Reference counting
---

An array can outlive the function that made it, as in step 1, so its memory isn't freed when that function ends.
Instead, Lugha counts what holds it.
Every variable, field or element that holds an array, a string or a box counts as one of its holders, and when the last one lets go, its memory is freed.
Line 4 makes a new array of 100 numbers on every pass of the loop, a hundred thousand in all, and only `row` holds it.
`row` is last used on line 5, at the end of the pass, so each array is freed there, before the next is made.
Press Run.

It prints `10000000`, the lengths of all the arrays added up.
The program never had to say which arrays it was done with: the compiler puts in the counting.
