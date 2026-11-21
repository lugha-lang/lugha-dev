---
title: Destructuring with let
start_error: E0201
---

Instead of `.0` and `.1`, a `let` can give each element a name of its own.
Line 4 names both parts of `divmod(17, 7)` with `let mut (weeks, days)`, because line 5 adds a day.
Press Run.

`lughac` gives E0201, "expected variable name, found `(`": `mut` can't go before the parentheses.
It goes inside them, before each name that will change, and here only `days` does.
Make line 4 `let (weeks, mut days)`, or press Solve.
