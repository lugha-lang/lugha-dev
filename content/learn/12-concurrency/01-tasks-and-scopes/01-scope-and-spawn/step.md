---
title: scope and spawn
---

A task is a function call that runs at the same time as the rest of the program, and it starts in a scope.
A scope is a block, `scope s { … }` on lines 4 to 7, and `s` is its handle, the name its tasks are started through.
Line 5 starts a task with `s.spawn(square(7))`, and line 6 waits for the task's answer with `join`.
`join` gives `Ok` with the answer, and `unwrap` takes it out.
A scope is an expression: its value is a `Result`, `Ok` with what its body gives, which line 8 prints.
Press Run.

The output panel shows `Ok(49)`: the task worked out `square(7)`, line 6 unwrapped it as the body's value, and the scope gave that back in `Ok`.
