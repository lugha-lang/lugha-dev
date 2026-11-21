---
title: if expressions
---

Like a block, an `if` has a value: the value of whichever branch ran.
Lines 3 to 9 are one `if` that puts one of three strings into `advice`.
Line 3 checks `temperature > 30`, `else if` on line 5 checks a second condition when the first is false, and `else` on line 7 takes what's left.
Press Run.

It prints `stay inside`.
`temperature` is 31, so `temperature > 30` is true, line 4's string goes into `advice`, and the other branches are skipped.
Change `31` on line 2 to `25` or `10` and run again to see the other two.
