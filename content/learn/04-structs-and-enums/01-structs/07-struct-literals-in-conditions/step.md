---
title: Struct literals in conditions
start_error: E0205
---

`Point` on line 1 now has `with Eq`, and line 5 checks with `==` whether `p` is the origin.
Press Run.

The program doesn't run.
In an `if` condition, the `{` after `Point` could start the struct literal or the `if`'s block.
E0205 says "struct literal in a condition must be in parentheses", at line 5.
Parentheses around the literal settle it, as the help shows: `(Point { … })`.
Put `Point { x: 0, y: 0 }` on line 5 in parentheses and run again, or press Solve.
