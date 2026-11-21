---
title: Branch types
start_error: E0403
error_note: Each branch of an `if` can give its value, so both have to give the same type. Line 4 gives a string and line 6 gives a number, and Lugha never turns one type into another on its own.
---

This `if` has two branches: line 4 gives a string, and line 6, in the `else`, gives `0`, a number.
Press Run.

The program doesn't run: E0403 says "`if` and `else` have different types", pointing at the `if` on line 3.
`advice` gets the type of the `if`, and an `if` has one type, so every branch has to give a value of that type.
`lughac` checks both branches before the program runs, even the one that won't be taken.
Change line 6 to a string, such as `"go out"`, and run again, or press Solve.
