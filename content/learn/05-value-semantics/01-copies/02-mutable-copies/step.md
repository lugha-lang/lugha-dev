---
title: Mutable copies
start_error: E0501
error_note: `b` is a variable of its own, declared with a plain `let`, so line 6 can't change it. It doesn't take its `mut` from `a`, even though `b` started as a copy of `a`.
---

This time `a` on line 4 is declared `let mut`, and its copy `b` on line 5 is a plain `let`.
Line 6 changes `b.x`.
Press Run.

The program doesn't run.
`mut` belongs to a variable, not to its value, so `b` doesn't take its `mut` from `a`: it's a variable of its own and needs its own `mut`.
E0501 says so for line 6: `b` is not mutable, and its help suggests `let mut b`.
Add `mut` after `let` on line 5 and run again, or press Solve.
