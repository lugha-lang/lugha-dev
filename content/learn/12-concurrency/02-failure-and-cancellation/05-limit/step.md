---
title: limit
---

`limit 2` after the scope's name, as on line 10, lets at most two of its tasks run at once: a third `s.spawn`, on line 13, waits until one of them has finished.
Lines 11 to 14 start four `job`s, each 200 milliseconds long.
Line 9 reads the clock before the scope and line 17 after it, and line 19 prints whether the scope took at least 400 milliseconds.
Press Run.

`Ok(100)` is the scope's value, the four answers added up.
Two at a time, four jobs take at least two rounds of 200 milliseconds, so line 19 prints `true`.
Without `limit 2` all four run at once, in about 200 milliseconds, and it prints `false`.
