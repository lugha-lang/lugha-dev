---
title: select with default
---

An `after` arm still waits up to its limit.
A `default` arm runs when no other arm can go on at once, so a `select` with one never waits.
Arms can send too: `tx.send(i)` on line 5 goes on when the channel has room.
Press Run.

The channel holds one value, so the first send goes through and prints `queued 1`.
Nothing receives in the loop, so the channel stays full, and the next two sends fall to `default` on line 6, which prints `full, dropped 2` and `full, dropped 3`.
Line 9 then receives the one value that went through, `Some(1)`.
