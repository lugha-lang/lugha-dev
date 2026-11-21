---
title: mut parameters
---

`bump` on line 3 has a `mut` parameter, `c`.
A parameter without `mut` is a copy of what the caller passed, but through a `mut` parameter the function changes the caller's own variable.
Line 4 adds `by` to `c.n`.
Lines 9 and 10 call `bump`, and each writes `mut c` for that parameter.
`main`'s `c` goes to `bump`'s `c` because it's the first argument, not because the names match.
Press Run.

Line 11 prints `5`: each call changed `c` in `main`, the first adding `2` and the second `3`.
