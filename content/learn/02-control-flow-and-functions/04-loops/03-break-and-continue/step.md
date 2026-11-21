---
title: break and continue
---

Both kinds of loop can be cut short from inside.
`continue` skips the rest of the block and goes on to the next turn, and `break` ends the loop.
Line 3 checks whether `i` is a multiple of 3, using `%` for the remainder and `==`, which checks that two values are equal, and if it is, line 4 skips it.
Line 7 ends the loop once `i` is over 7, though the range goes up to 9.
Press Run.

It prints `1`, `2`, `4`, `5` and `7`: `continue` skipped `3` and `6`.
When `i` reaches 8, `break` ends the loop before line 9 can print it.
