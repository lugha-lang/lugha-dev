---
title: within
---

`within 500` after a scope's name, as on lines 9 and 14, gives it a deadline: 500 milliseconds from when it starts.
If the scope is still running then, its body and tasks are cancelled, and its value is an `Err` whose `f.kind` is `.Deadline`, unless a task failed first.
The first scope's task takes 100 milliseconds, and the second's would take three seconds.
The `match` on lines 18 to 25 is like `report`'s in Failure and cancellation, with `.Ok(text)` printing the text.
For a deadline, `f.task` names the scope, by its handle `s`, not a task.
Press Run.

The first scope finishes in time, with `Ok`, and the second is cut off at 500 milliseconds.
