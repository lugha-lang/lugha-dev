---
title: Mutable places only
start_error: E0501
error_note: `bump` changes the variable passed to its `mut` parameter, so that variable has to be declared `let mut`, and `c` on line 8 is a plain `let`.
---

Line 9 passes `c` as `mut`, and line 8 declares `c` with a plain `let`.
Press Run.

The program doesn't run.
A `mut` argument is changed by the call, so it has to be a place that can change: a variable declared `let mut`, or a field or element of one.
E0501 says it cannot pass `c` as `mut` because `c` is not mutable, and its help suggests `let mut c`.
An element works the same way: `bump(mut counters[1], 5)` changes the second counter in a `let mut` array.
Add `mut` after `let` on line 8 and run again, or press Solve.
