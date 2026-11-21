---
title: Returning from a loop
start_error: E0503
---

A loop can hide the same problem.
`first_over` doubles `n` until it passes `limit`, and returns it from inside a `while true` loop.
The condition is always true, so the loop can only end at the `return`.
Press Run.

`lughac` still gives E0503, because it never counts a `while` loop as returning, even `while true`.
As with the two `if`s in step 2, `lughac` doesn't look at the condition.
A `loop` that no `break` leaves does count, since the only way out is the `return`.
Write `loop` in place of `while true` on line 3, or press Solve.
