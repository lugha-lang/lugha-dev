---
title: Tasks stay put
start_error: E0472
---

Line 5 keeps two tasks in an array, and line 6 joins them from it.
Press Run.

E0472: "a scope or task handle can't be stored in a value".
A `Task` or a `Scope` is kept in a local or passed as an argument, and nothing else: it isn't returned, or put in an array, a field or a closure.
To collect the answers of many tasks, each can send its answer on a channel, as Channels shows.
Replace line 5 with `let a = s.spawn(square(2));` and `let b = s.spawn(square(3));`, and line 6 with `a.join().unwrap() + b.join().unwrap()`, or press Solve.
