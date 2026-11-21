---
title: No overloading
start_error: E0302
---

Lines 1 and 3 both declare a function called `area`, one with two parameters and one with one, and line 7 calls `area` with a single number.
Press Run.

It gives E0302, "`area` is defined more than once", and E0405 for line 7, which says the call gives one argument to an `area` that takes two.
Two functions can't share a name, whatever their parameters, and a parameter can't have a default value either, so each way of calling needs its own function.
Rename the second one `square_area` on lines 3 and 7, or press Solve.
