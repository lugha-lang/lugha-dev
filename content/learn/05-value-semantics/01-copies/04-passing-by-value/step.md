---
title: Passing by value
start_output: [5, 6]\n
---

Function arguments follow the same rule: a parameter written without `mut`, like `xs` here, is a copy of what the caller passed.
`add_one` can't change its parameter, so line 2 copies `xs` into `ys`, and it pushes onto that and returns it.
Line 9 calls `add_one` but throws away what it returns.
Press Run.

Line 10 prints `xs` as it was, `[5, 6]`.
To keep the result, assign it back: make line 9 `xs = add_one(xs);`, or press Solve.
Through a plain parameter a function can't change its caller's values, so to keep what `add_one` built, the caller assigns what it returns.
