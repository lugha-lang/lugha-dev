---
title: mut self methods
start_error: E0501
---

`self` is read-only, like any parameter, so a method that changes the value it's called on takes `mut self` instead, as `shift` does on line 4.
Line 11 calls `shift` on `p`, and `p` has no `mut`.
Press Run.

E0501: "cannot call `mut self` method `shift` on `p`: it is not mutable".
A `mut self` method changes the caller's own value, so `p` needs `let mut`, as it did for field assignment.
Add `mut` after `let` on line 10, or press Solve.
