---
title: mut self methods
start_error: E0501
error_note: `shift` takes `mut self`, so calling it on `p` changes `p`, and `p` was declared with plain `let`. A value a method changes needs `let mut`, like one you assign to.
---

`self` can't change, like any parameter, so a method that changes the value it's called on takes `mut self` instead, as `shift` does on line 4.
Line 11 calls `shift` on `p`, and line 10 declares `p` with plain `let`.
Press Run.

The program doesn't run.
E0501 says "cannot call `mut self` method `shift` on `p`: it is not mutable", at line 11.
A `mut self` method changes the value it's called on, so `p` needs `let mut`, as it does when one of its fields is assigned.
Add `mut` after `let` on line 10 and run again, or press Solve.
