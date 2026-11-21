---
title: Indexing
start_error: E0501
---

Line 3 tries to change the second element of an array declared with plain `let`.
Line 4 reads the first, `scores[0]`, because indexes count from `0`.
Press Run.

E0501 says "cannot assign to `scores`: it is not mutable".
Changing one element changes the array, so the array needs `let mut`, like any variable you change.
Add `mut` after `let` on line 2, or press Solve.
