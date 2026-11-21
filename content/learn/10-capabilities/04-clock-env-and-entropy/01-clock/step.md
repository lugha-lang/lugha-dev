---
title: Clock
---

A `Clock` tells the time two ways.
`now_ms()` on line 2 is the current time, in milliseconds since the start of 1970 (UTC).
`monotonic_ms()` on lines 4 and 9 counts from no particular moment but never goes back, so the difference between two readings is how long the loop on lines 6 to 8 took.
Line 10 prints the loop's total.
Press Run.

The first `true` is line 3: the current time is past mid-November 2023.
`2999997` is the loop's total.
The last `true` is line 11.
How long the loop took changes from run to run, so line 11 prints only whether it's at least 0.
