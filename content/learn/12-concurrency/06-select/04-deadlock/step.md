---
title: Deadlock
start_output: 
---

A `select` without `after` or `default` can wait forever, as a plain `recv` can, and this program waits with plain `recv`s.
`ping` on line 1 waits for a message, then sends one to `pong`, and `pong` on line 7 does the same the other way round.
Press Run.

Each waits for the other first, so neither goes on: when every task is waiting, the program panics with a deadlock and exits with code 101.
The report names each waiting task and where the channel it waits on was made: `pong` on the channel from line 15, and `ping` on the one from line 14.
Something has to send first: after line 15, add `to_ping.send("start");`, or press Solve.
