---
title: Field assignment
start_error: E0501
---

Line 5 changes one field with `p.x = 5`, and line 4 declares `p` with plain `let`.
Press Run.

The program doesn't run.
E0501 names `p` itself, not the field: "cannot assign to `p`: it is not mutable".
A field has no `mut` of its own, so changing a field changes the struct, and the variable that holds it needs `let mut`, as the help shows.
Add `mut` after `let` on line 4 and run again, or press Solve.
