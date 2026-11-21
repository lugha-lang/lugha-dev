---
title: Indexing
start_error: E0501
---

Line 2 declares `scores` with plain `let`.
Line 3 sets `scores[1]`, the element at index 1, to `88`: indexes count from `0`, so that's the second element.
Line 4 prints the first, `scores[0]`.
Press Run.

The program doesn't run.
E0501 says "cannot assign to `scores`: it is not mutable", at line 3.
Changing one element changes the array, so the array needs `let mut`, like any variable that changes, and the help shows it: `let mut scores`.
Add `mut` after `let` on line 2 and run again, or press Solve.
