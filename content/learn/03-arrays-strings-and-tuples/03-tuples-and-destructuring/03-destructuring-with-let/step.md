---
title: Destructuring with let
start_error: E0201
error_note: After `let mut`, `lughac` expects a variable name, so the `(` doesn't fit there. To make one of the names in parentheses changeable, put `mut` before that name, inside them.
---

Instead of `.0` and `.1`, a `let` can give each element of a tuple a name of its own.
Line 4 tries to name both parts of `divmod(17, 7)` with `let mut (weeks, days)`, so that line 5 can add a day.
Press Run.

The program doesn't run.
E0201 says "expected variable name, found `(`" at line 4, column 13, the `(` right after `mut`.
`mut` can't go before the parentheses: it goes inside them, before each name that will change, and here only `days` changes.
Change the start of line 4 to `let (weeks, mut days)` and run again, or press Solve.
