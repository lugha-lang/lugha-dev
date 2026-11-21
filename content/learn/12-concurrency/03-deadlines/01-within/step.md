---
title: within
---

`within 500` after a scope's name, as on lines 9 and 14, gives it a deadline: 500 milliseconds from when it starts.
If the scope is still running then, its body and tasks are cancelled, and its value is an `Err` whose `f.kind` is `.Deadline`, unless a task failed first.
The first scope's task takes 100 milliseconds, and the second's would take three seconds.
Line 13 prints the first scope's value, and the `match` on lines 18 to 25 prints a line for each way the second can end.
For a deadline, `f.task` names the scope, by its handle `s`, not a task.
Press Run.

The first scope finishes in time, so line 13 prints `Ok` with the text its task gave back.
The second is cut off at 500 milliseconds, so line 21 prints `s ran out of time`.
