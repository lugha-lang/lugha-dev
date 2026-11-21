---
title: while loops
---

Where an `if` runs its block once, `while` checks its condition, runs its block if it's true, then checks again, until the condition is false.
`seconds` starts at `3`, and line 5 takes one off each time round.
`seconds -= 1` is short for `seconds = seconds - 1`, and `+=`, `*=` and the rest work the same way.
Press Run.

The loop on lines 3 to 6 runs three times, and line 4 prints `3`, `2` and `1`.
Then `seconds` is `0`, so `seconds > 0` is false, the loop ends, and line 7 prints `go`.
