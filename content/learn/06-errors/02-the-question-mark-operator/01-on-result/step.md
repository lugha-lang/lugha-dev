---
title: ? on Result
---

`?` after a `Result` gives the value inside an `Ok`, or returns the `Err` from the function at once.
`average` on line 8 divides with `divide(total, count)?` on line 9, so `avg` is a plain `i64`, not a `Result`.
Line 10 prints what it divided, and line 11 wraps the answer back in `Ok`.
Lines 15 and 16 call `average` with a count of `2`, then `0`.
Press Run.

For the count of `2`, line 10 prints `divided 10 by 2`, and line 15 prints `Ok(5)`.
For `0`, the failed division returns its `Err` from `average` at line 9, so line 10 doesn't run, and line 16 prints the `Err`.
