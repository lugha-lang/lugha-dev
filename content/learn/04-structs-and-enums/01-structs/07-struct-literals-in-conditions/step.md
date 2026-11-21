---
title: Struct literals in conditions
start_error: E0205
---

Line 5 checks with `==` whether `p` is the origin.
Press Run.

It doesn't compile: the `{` after `Point` could start the literal or the `if`'s block, so `lughac` gives E0205, "struct literal in a condition must be in parentheses".
Parentheses around the literal end the doubt.
Put the literal on line 5 in parentheses, or press Solve.
