---
title: Passing a value to its own mut method
start_error: E0508
---

`add` on line 4 adds another point to `self`, and line 12 tries to add `p` to itself.
Press Run.

`lughac` refuses it with E0508: a value can't be passed to a `mut self` method called on that same value.
`let w = p;` makes a separate copy of `p`, as the help says.
Put it on a line before the call and pass `w` on line 12, or press Solve.
