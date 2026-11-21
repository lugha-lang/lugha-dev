---
title: No overloading
start_error: E0302
error_note: Line 1 already declares a function called `area`, so line 3 can't declare another, even with different parameters. Each function in a file needs its own name.
---

Lines 1 and 3 both declare a function called `area`, one with two parameters and one with one.
Line 6 calls `area` with two numbers, and line 7 calls it with one.
Press Run.

The program doesn't run, and there are two errors.
E0302 says "`area` is defined more than once", at line 3: two functions can't share a name, whatever their parameters.
E0405 says "`area` takes 2 arguments but 1 was given", at line 7.
An argument is a value passed in a call, and line 7 reached the `area` on line 1, which takes two.
A parameter can't have a default value either, so each way of calling needs its own function.
Rename the second one `square_area` on lines 3 and 7 and run again, or press Solve.
