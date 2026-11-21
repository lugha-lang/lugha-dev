---
title: The root scope
---

`main` can also take `root: Scope`, by type like a capability, as on line 8.
It's a scope as long as the program, and the program waits for its tasks before it ends.
Line 9 starts `later` in it, and line 10 is `main`'s last line.
Press Run.

`main returns` comes first: `main` reaches its end while `later` is still asleep.
The program doesn't end there: `the task finishes` comes next, and "Exited with code 0" only after it.
