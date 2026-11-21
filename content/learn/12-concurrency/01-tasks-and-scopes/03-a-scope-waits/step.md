---
title: A scope waits
---

`slow` on line 3 sleeps for 200 milliseconds, with `task.sleep` from Testing with capabilities (outside a test it really sleeps: virtual time is only for tests), then prints.
Line 10 starts it and never joins it, and line 11 prints at once, at the end of the scope's body.
Line 13 prints after the scope.
Line 9 keeps the scope's value in `r` because a scope is a `Result`, and one used as a statement is E0467, as in Result.
Press Run.

The scope doesn't end with its body: it waits for every task it started, so `the task is done` comes before `the scope is done`.
