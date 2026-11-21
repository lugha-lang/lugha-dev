---
title: Assignment
start_error: E0204
error_note: An assignment such as `b = 0` gives `b` a value but has no value of its own, so `a = b = 0` leaves nothing for `a` to take. Each assignment is a statement of its own.
---

Both `a` and `b` are `let mut` this time, and line 4 tries to set both to `0` in one go, with `a = b = 0`.
Press Run.

The program doesn't run: E0204 says "assignment is a statement, not an expression".
An expression gives a value, as `a + b` does, while a statement only does something.
An assignment is always a statement, so `b = 0` has no value for `a` to take.
The help line, "use `==` to compare", is for a different slip, `=` written by mistake for `==`, which compares two values; it doesn't apply here.
Split line 4 into two assignments, `a = 0;` and `b = 0;`, one per line, or press Solve.
