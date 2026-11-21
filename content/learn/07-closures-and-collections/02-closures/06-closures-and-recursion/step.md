---
title: Closures and recursion
start_error: E0301
---

Line 2 stores a closure in `fact`.
For `n` above `1`, the closure multiplies `n` by `fact(n - 1)`, calling `fact` again.
Press Run.

The program doesn't run.
A closure has no name of its own, so it can't call itself.
`fact` is only the variable that will hold the closure, so the `fact(n - 1)` inside it refers to nothing yet.
E0301 says so: "cannot find `fact` in this scope", pointing at that call on line 2.
A named function can call itself, so write `fact` as one.
Move line 2 above `main` as `fun fact(n: i64): i64 = if n <= 1 { 1 } else { n * fact(n - 1) };`, or press Solve.
