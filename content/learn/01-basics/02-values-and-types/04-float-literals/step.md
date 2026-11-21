---
title: Float literals
start_error: E0107
error_note: A number with an exponent is a float, and a float has to be written with a `.` and a digit after it. `2e5` has no `.`, so it's refused, and `2.0e5` is the float it was meant to be.
---

Line 2 writes two hundred thousand with an exponent, as `2e5`: 2 times 10 to the 5th.
Press Run.

The program doesn't run.
`lughac` refuses `2e5` with E0107, "float literal needs a fractional part".
A number with an exponent is a float, and a float has to be written with a `.` and a digit after it, so `2e5` has to be `2.0e5`, as the help line says.
Write `2.0e5` on line 2 and run again, or press Solve.
