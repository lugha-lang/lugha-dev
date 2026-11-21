---
title: Deadlock
start_output: 
---

This program waits on plain `recv`s, which can wait forever, as a `select` without `after` or `default` can.
`ping` on line 1 waits for a message, then sends one to `pong`, and `pong` on line 7 does the same the other way round.
Press Run.

Only the panic prints.
Each waits for the other first, so neither goes on, and when every task is waiting, the program panics with a deadlock, on standard error.
The report under it names each waiting task and where the channel it waits on was made: `pong` on the channel from line 15, and `ping` on the one from line 14.
The panic ends the program with exit code 101.
Something has to send first: after line 15, add `to_ping.send("start");` and run again, or press Solve.
