---
title: scope and spawn
start_error: E0474
---

A task is a function call that runs at the same time as the rest of the program.
Line 4 starts `square(7)` as a task with `spawn`, and line 5 waits for its answer with `join`.
Press Run.

E0474: "a task starts in a scope".
A scope is a block, `scope s { … }`, and its tasks start through its handle `s`, as `s.spawn(square(7))`.
A scope is an expression: its value is a `Result`, `Ok` with what its body gives.
Replace lines 4 and 5 with `let r = scope s {`, then `let t = s.spawn(square(7));` and `t.join().unwrap()` inside it, a closing `};`, and `console.println(r.debug());`, or press Solve.
