---
title: Mutable copies
start_error: E0501
---

This time `a` is declared `let mut`, and its copy `b` on line 5 has no `mut`.
Line 6 changes `b.x`.
Press Run.

E0501 says `b` is not mutable: it doesn't take its `mut` from `a`.
`mut` belongs to a variable, and `b` is a variable of its own, so it needs its own `mut` whatever `a` has.
Add `mut` after `let` on line 5, or press Solve.
