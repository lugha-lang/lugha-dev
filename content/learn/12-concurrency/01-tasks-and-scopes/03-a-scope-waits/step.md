---
title: A scope waits
---

`slow` on line 3 sleeps for 200 milliseconds with `task.sleep`, then prints.
Outside a test, it really sleeps: virtual time is only for tests.
Line 10 starts `slow` as a task and never joins it, and line 11 prints at once, at the end of the scope's body.
Line 13 prints after the scope.
Line 9 keeps the scope's value in `r` without using it: a scope gives a `Result`, and a `Result` used as a statement is E0467.
Press Run.

`the body is done` comes first, from line 11, while the task is still asleep.
The scope doesn't end with its body: it waits for every task it started, so `the task is done` comes next.
Only then does the scope end, and line 13 prints `the scope is done`.
