---
title: Clock
---

A `Clock` tells the time two ways.
`now_ms()` on line 2 is the current time, as milliseconds since the start of 1970 (UTC), and line 3 checks it's past mid-November 2023.
`monotonic_ms()` on lines 4 and 9 counts from no particular moment, but never goes back, so the difference between two readings is how long the loop on lines 6 to 8 took.
Line 10 prints the loop's total, so the loop has real work to do.
How long it took changes from run to run, so line 11 prints only whether it's at least 0.
Press Run.
