---
title: Closing a channel
start_output: 
---

`for v of rx` on line 12 receives every value until the channel is closed and empty, and line 13 adds them up.
This `produce` sends five squares and doesn't close the channel.
A channel stays open until a sender closes it, even after `produce` returns.
Press Run.

`55` never prints.
After the fifth value, `main` waits for another, but `produce` has finished and nothing will send again.
That's a deadlock, a wait that can never end, and the program stops with a panic on standard error: `panic: deadlock: every green thread is waiting`, a green thread being one of the program's tasks, `main` included.
The line under it names who waits and where: `main`, to receive on the channel made at line 8, column 20.
The panic ends the program with exit code 101.
Once the channel is closed, the loop ends after the last value.
Add `out.close();` after line 4, at the end of `produce`, and run again, or press Solve.
