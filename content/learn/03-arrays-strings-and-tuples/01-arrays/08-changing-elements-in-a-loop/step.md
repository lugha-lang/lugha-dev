---
title: Changing elements in a loop
start_error: E0501
error_note: `score` holds each element in turn, and in a plain `for … of` loop it can't be changed. With `of mut`, `score` is each element itself, and changing it changes the array.
---

Line 2 declares `scores` with `let mut`, and line 4 tries to add 5 to each score as the loop goes through them.
Press Run.

The program doesn't run.
E0501 points at `score` on line 4, not at `scores`: "cannot assign to `score`: it is not mutable".
`score` is the loop variable, and a loop variable can't change.
The help suggests copying it into a `let mut`, but adding to a copy would leave the array as it was.
To change the elements, loop with `of mut`: then `score` is each element itself, so adding to it changes the array.
While a `for … of mut` loop runs, the array can't grow or shrink, and `scores.push(1)` inside it is E0507.
Add `mut` after `of` on line 3 and run again, or press Solve.
