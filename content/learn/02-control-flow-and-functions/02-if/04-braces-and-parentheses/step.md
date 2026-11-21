---
title: Braces and parentheses
start_error: E0201
error_note: The code after an `if`'s condition always goes in a block in braces. Line 3 has none, so `lughac` expected a `{` where `console` starts.
---

Line 3 puts the condition in parentheses and leaves out the braces around the code that runs.
Press Run.

The program doesn't run: E0201 says "expected `{`, found identifier `console`", pointing at `console` on line 3.
Parentheses around a condition are optional, so `if (unread > 0)` means the same as `if unread > 0`.
Braces are not: the code after the condition is always a block in braces, even when it holds one line.
So is the code after `else`, unless it's another `if`.
Put line 3's `console.println` in braces and run again, or press Solve.
