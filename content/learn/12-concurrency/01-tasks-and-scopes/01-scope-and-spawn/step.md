---
title: scope and spawn
---

A task is a function call that runs at the same time as the rest of the program, and it starts in a scope.
A scope is a block, `scope s { … }` on lines 4 to 7, and its tasks start through its handle `s`, as `s.spawn(square(7))` on line 5.
Line 6 waits for the task's answer with `join`.
A scope is an expression: its value is a `Result`, `Ok` with what its body gives, which line 8 prints.
Press Run.
