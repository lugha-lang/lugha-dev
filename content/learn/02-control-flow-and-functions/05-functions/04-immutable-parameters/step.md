---
title: Immutable parameters
start_error: E0501
error_note: `price` is a parameter, and a parameter can't be given a new value, as a `let` without `mut` can't. Declare a mutable copy first with `let mut price = price;`.
---

`with_tax` takes a `price`, and line 2 tries to add a tenth to it.
Press Run.

The program doesn't run: E0501 says "cannot assign to `price`: it is not mutable", at line 2.
A parameter is like a variable declared with `let` and no `mut`: it can't be given a new value.
The help line suggests shadowing, from the Variables lesson.
`let mut price = price;` declares a new, mutable `price` from the parameter, and from the next line on, `price` means the new one.
Add `let mut price = price;` as a new line 2 and run again, or press Solve.
