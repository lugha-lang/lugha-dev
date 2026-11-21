---
title: Returning from a loop
start_error: E0503
---

A loop can hide the same problem.
`first_over` doubles `n` on line 4 until it passes `limit`, and returns it on line 6, from inside a `while true` loop.
The condition is always true, so the loop can only end at the `return`.
Press Run.

The program doesn't run: E0503 again, "`first_over` may end without returning a value of type i64".
`lughac` never counts a `while` loop as returning, even `while true`: as with the two `if`s in step 2, it doesn't look at the condition.
The help line names the way out: a `loop` that no `break` leaves does count, since the only way out is the `return`.
Its "spec §6" is the section of the Lugha specification that sets this rule.
Write `loop` in place of `while true` on line 3 and run again, or press Solve.
