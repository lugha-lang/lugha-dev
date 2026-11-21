---
title: Closing a channel
start_output: 
---

`for v of rx` on line 12 receives every value until the channel is closed and empty, and adds them up.
This `produce` sends five squares and doesn't close the channel.
A channel stays open until a sender closes it, even after `produce` returns.
Press Run.

`55` never prints: after the fifth value, `main` waits for another, but `produce` has finished and nothing will send again, so the program ends with a deadlock, which select covers.
Once the channel is closed, the loop ends after the last value.
Add `out.close();` after line 4, at the end of `produce`, or press Solve.
