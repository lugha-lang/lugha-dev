---
title: Branch types
start_error: E0403
---

This `if` has two branches: line 4 gives a string, and line 6, in the `else`, gives `0`, a number.
Press Run.

`lughac` refuses it with E0403, "`if` and `else` have different types", and its notes say "this is string" for line 4 and "this is i64" for the `else`.
`advice` gets the type of the `if`, and an `if` has one type, so every branch has to give a value of it.
`lughac` checks both branches before the program runs, even the one that won't be taken.
Change line 6 to a string, such as `"go out"`, and run again, or press Solve.
