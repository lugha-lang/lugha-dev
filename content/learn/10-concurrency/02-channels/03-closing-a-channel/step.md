---
title: Closing a channel
---

So far `main` knew to stop after three values, and `c.close()` on line 5 lets the sender say when it's done instead.
After it, `recv` gives `None` once the values already sent have been taken, so `while let` on line 11 runs until then.
Press Run.

A closed channel's `recv` keeps giving `None`, as line 15 shows.
Sending on a closed channel panics with "send on a closed channel", and closing it again panics with "close of a closed channel".
So the thread that sends is the one to close the channel, once it has sent everything.
