---
title: Closures
start_error: E0412
error_note: A closure's parameter needs a type, either written or taken from where the closure is passed. Line 5 stores the closure in a variable, so nothing says what `x` is.
---

A closure is a function written in place, without a name.
Line 4 passes the closure `fun(x) = x * 2`, which doubles its argument, to `apply`.
Line 5 stores a second closure, `fun(x) = x + 10`, in the variable `add_ten`.
Press Run.

The program doesn't run.
On line 4, `x` takes its type from `apply`'s parameter, a `fun(i64): i64`, but on line 5 nothing says what `x` is.
E0412 says so: it "can't infer the type of parameter `x`".
Its help gives both ways out: write the type, `x: i64`, or pass the closure where a function type is expected, as line 4 does.
The return type can be written too, as in a named function.
A longer body goes in braces, as in `fun(n: i64): string { … }`, and a closure that uses `return` needs its return type written, unless it's passed where a function type is expected.
Make line 5's closure `fun(x: i64): i64 = x + 10` and run again, or press Solve.
