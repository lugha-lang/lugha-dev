---
title: Tasks stay put
start_error: E0472
---

`s.spawn` gives back a `Task`, a handle on the task it started.
Line 5 keeps two tasks in an array, and line 6 joins them from it.
Press Run.

The program doesn't run.
A `Task` or a `Scope` is kept in a local or passed as an argument, and nothing else: it isn't returned, or put in an array, a field or a closure.
So each place this code holds a task in a value is an E0472, "a scope or task handle can't be stored in a value": the array on line 5, then `ts[0]` and `ts[1]` on line 6.
Each help says the same: keep the handle a local, and finish the tasks inside the scope that started them.
Replace line 5 with `let a = s.spawn(square(2));` and `let b = s.spawn(square(3));`, and line 6 with `a.join().unwrap() + b.join().unwrap()`, and run again, or press Solve.
