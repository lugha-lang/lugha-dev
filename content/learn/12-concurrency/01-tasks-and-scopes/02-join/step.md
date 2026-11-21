---
title: join
---

Lines 11 and 12 start two tasks, which run at the same time.
`t.join()` waits for a task to finish and gives `Ok` with what it returned, once it has finished normally, which lines 13 and 14 print.
A task can be joined more than once: line 15 joins both again and adds their answers up as the body's value.
Line 17 prints the scope's value, `Ok` with that sum.
Press Run.
