---
title: Braces and parentheses
start_error: E0201
---

Line 3 puts the condition in parentheses and leaves out the braces.
Press Run.

`lughac` gives E0201, "expected `{`, found identifier `console`": the braces are what's missing.
Parentheses around a condition are optional, so `if (unread > 0)` means the same as `if unread > 0`.
The code after the condition is always a block in braces, even when it holds one line.
So is the code after `else`, unless it's another `if`.
Put line 3's `console.println` in braces and run again, or press Solve.
