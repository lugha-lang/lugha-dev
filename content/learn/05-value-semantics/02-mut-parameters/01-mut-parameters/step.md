---
title: mut parameters
---

`add_one` in Copies couldn't change its caller's array, so it returned a new one.
A parameter written with `mut`, like `c` on line 3, works differently: the function changes the caller's own variable.
Line 4 adds `by` to `c.n`, and lines 9 and 10 call `bump` with `mut c`.
Press Run.

`c.n` is `5` on line 11: each call changed `c` in `main` when it returned.
Like a `mut self` method in Methods, `bump` works on the caller's own value, but here the call writes `mut` too, where `p.shift(10)` didn't.
