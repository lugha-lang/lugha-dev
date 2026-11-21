---
title: Exit codes
start_output: checking the input\n
---

`main` can also give back a number: the program's exit code.
`: i32` on line 1 says so; `i32` is a type of whole number.
Line 3, `1`, has no `;`: the last line of a function's body, between its `{` and `}`, can be a value without a `;`, and that value is what the function gives back.
Press Run.

The output panel shows `checking the input`, then "Exited with code 1".
An exit code tells whatever started the program, such as a script, whether it worked: 0 means it did, and anything else means it failed.
Change line 3 to `0` and run again, or press Solve.
