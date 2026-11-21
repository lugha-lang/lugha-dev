---
title: Exit codes
start_output: checking the input\n
---

`main` can also return an `i32`, which becomes the program's exit code.
Here line 3, `1`, has no `;` because it isn't a statement: the last expression in a body, written without a `;`, is the value the body gives back.
Press Run, and the program exits with code 1, which whatever ran it reads as a failure.

Change line 3 to `0` and run again, or press Solve.
There is no `exit` to call: a program ends with a code by returning it from `main`.
`main` returns nothing or an `i32`, and `lughac` refuses anything else with E0304.
