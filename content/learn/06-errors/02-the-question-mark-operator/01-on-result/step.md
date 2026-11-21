---
title: ? on Result
---

`?` after a `Result` gives the value inside an `Ok`, or returns the `Err` from the function at once.
`average` on line 8 divides with `divide(total, count)?` on line 9, so `avg` is a plain `i64`.
Line 10 prints what it divided, and line 11 wraps the answer back in `Ok`.
Lines 15 and 16 call `average` with a count of `2`, then `0`.
Press Run.

Line 10 prints only for the count of `2`: the failed division returns its `Err` at line 9, and nothing after the `?` runs.
