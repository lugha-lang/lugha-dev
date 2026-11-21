---
title: Field assignment
start_error: E0501
---

Line 5 changes one field, `p.x = 5`, and `p` was declared with plain `let`.
Press Run.

E0501 names `p` itself: "cannot assign to `p`: it is not mutable".
A field has no `mut` of its own, so changing one changes the struct, and the variable that holds it needs `let mut`.
Add `mut` after `let` on line 4, or press Solve.
