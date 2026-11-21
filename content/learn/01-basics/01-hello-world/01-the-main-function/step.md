---
title: The main function
start_error: E0471
---

A Lugha program starts at `main`, and this one has a single line meant to print `Hello, world`.
Line 1 is a doc comment, `/** … */`, which editors show beside the item that follows it.
Press Run.

`lughac` gives E0471: `println` needs a `Console`.
When the program starts, `main` is given the console as a parameter, `console: Console`, and printing goes through it, as `console.println`.

Write `console: Console` between the parentheses on line 2 and `console.println` on line 3, or press Solve.
The output ends with the exit code, 0: this `main` returns nothing, so the program ends with 0 when it reaches the end of `main`.
