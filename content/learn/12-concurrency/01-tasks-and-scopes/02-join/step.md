---
title: join
---

Lines 11 and 12 start two tasks, which run at the same time, each adding up the numbers from 0 to below its `n`.
`t.join()` waits for a task to finish, and when it has finished normally, gives `Ok` with what the task returned.
Lines 13 and 14 print what `join` gives for each task.
A task can be joined more than once: line 15 joins both again and adds their answers up as the body's value.
Press Run.

The first two lines are `Ok` with each task's sum, from lines 13 and 14.
The third, from line 17, is the scope's value: `Ok` with the two sums added up.
