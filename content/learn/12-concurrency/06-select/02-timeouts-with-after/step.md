---
title: Timeouts with after
---

The `select` in step 1 waits as long as it takes, and an `after` arm puts a limit on that.
Here `slow` sleeps for half a second before it sends.
`after(200)` on line 19 runs if no other arm could go on within 200 milliseconds.
Each pass of the loop is a new `select`, so the 200 milliseconds start again, and the loop either gets the message or prints `still waiting`.
Press Run.

Two waits of 200 milliseconds end before the message arrives, so `still waiting` prints twice.
