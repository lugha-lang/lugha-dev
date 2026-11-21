---
title: Mutable places only
start_error: E0501
---

Line 8 declares `c` with plain `let`, and line 9 passes it as `mut`.
Press Run.

E0501: "cannot pass `c` as `mut`: it is not mutable".
A `mut` argument is changed by the call, so it must be mutable, like a variable declared `let mut` or a field or element of one.
Add `mut` after `let` on line 8, or press Solve.
An element works the same way: `bump(mut counters[1], 5)` changes the second counter in a `let mut` array.
