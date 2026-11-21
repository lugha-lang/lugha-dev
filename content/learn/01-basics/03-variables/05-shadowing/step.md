---
title: Shadowing
---

There's another way to give a name a new value without `mut`: declare it again with `let`.
Line 3 declares `score` a second time, as the old `score` plus 5.
Line 5 declares it a third time, as a string.
Press Run.

Line 4 prints `15`.
The second `let` made a new variable that hides the first, which is called shadowing.
The new `score` exists from the end of its `let` line on, so `score + 5` on line 3 still reads the old one.
Line 6 prints `fifteen`: line 5 made a new variable again, so it can have a different type.
`let mut` can't do that, since assigning changes a variable's value but never its type.
