---
title: Passing by value
start_output: [5, 6]\n
---

`add_one` on line 1 takes an array, `xs`, and returns a new one with `1` pushed on.
A parameter written without `mut`, like `xs`, is a copy of what the caller passed, and the function can't change it.
So line 2 copies it into `ys`, line 3 pushes onto `ys`, and line 4 returns `ys`.
Line 9 calls `add_one`, and nothing keeps what it returns.
Press Run.

Line 10 prints `xs` as it was, `[5, 6]`: `add_one` changed only its own copy, and the array it returned was thrown away.
Through a plain parameter a function can't change its caller's values, so the caller keeps what it builds by assigning what it returns.
Make line 9 `xs = add_one(xs);` and run again, or press Solve.
