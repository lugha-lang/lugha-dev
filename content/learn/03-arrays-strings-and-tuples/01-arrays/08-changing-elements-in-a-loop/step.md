---
title: Changing elements in a loop
start_error: E0501
---

Line 4 tries to add 5 to every score as the loop goes through them, and `scores` is `let mut`.
Press Run.

The loop variable is the problem: E0501, "cannot assign to `score`: it is not mutable".
The help suggests a copy in a `let mut`, which would change only the copy.
To change the array itself, loop over it with `of mut`: then `score` is each element itself, and adding to it adds to that element.
Add `mut` after `of` on line 3, or press Solve.
Inside a `for … of mut` the array can't grow or shrink, and `scores.push(1)` there is E0507.
