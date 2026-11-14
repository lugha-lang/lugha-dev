---
title: spawn
---

Until now each program has run one line of work, from the top of `main` down.
A green thread is another line of work in the same program, with its own stack of calls, and the program switches between them.
All of a program's green threads share its one OS thread and take turns on it.
`spawn` before a call starts the call in a new green thread, and `join` waits for one to finish.
Lines 11 and 12 spawn two, and `main` goes straight on to print "both started".
Press Run.

The two threads get their turns when `main` waits in `join` on line 14.
`task.yield_now()` on line 6, from `std.task`, hands over its turn, so their lines alternate.
