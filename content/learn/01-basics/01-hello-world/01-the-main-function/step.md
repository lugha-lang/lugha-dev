---
title: The main function
---

A Lugha program starts at `main`, and this one prints `Hello, world`.
Line 1 is a doc comment, `/** … */`, which editors show beside the item that follows it.
When the program starts, `main` is given the console as a parameter, `console: Console` on line 2, and printing goes through it, as `console.println` on line 3.
Press Run.

The output ends with the exit code, 0: this `main` returns nothing, so the program ends with 0 when it reaches the end of `main`.
