---
title: Recursion
---

A function can also call itself, which is called recursion.
`factorial` on line 1 multiplies `n` by `factorial(n - 1)`, a call to itself.
One path has to give a value without calling the function again, or the calls never stop: here, when `n` is `1` or less, the `if` gives `1`.
The body is one `if` expression, so it uses the `=` form from the Functions lesson.
Press Run.

It prints `120`, which is 5 × 4 × 3 × 2 × 1.
`factorial(5)` calls `factorial(4)`, and so on down to `factorial(1)`, which gives `1` and makes no more calls.
