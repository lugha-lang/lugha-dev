---
title: Mutable variables
start_error: E0501
error_note: `count` was declared with `let`, so it keeps the `0` it was given, and line 3 can't give it a new value. A variable that changes is declared with `let mut`.
---

Line 2 declares `count` as `0`, and line 3 tries to give it a new value, `count + 1`, with `=`.
Giving a variable a new value is called assigning.
Press Run.

The program doesn't run: E0501 says "cannot assign to `count`: it is not mutable", at line 3.
A variable keeps the value it was given unless it's declared `let mut`, which makes it mutable, able to change.
The help line under the error says the same: `let mut count`.
Add `mut` after `let` on line 2 and run again, or press Solve.
