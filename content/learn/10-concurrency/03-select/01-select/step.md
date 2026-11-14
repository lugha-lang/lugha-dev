---
title: select
---

In 10.2 `main` read from one channel, but with two, a `recv` on one would wait there while the other already has a value.
`select` on line 13 waits on both and takes whichever is ready first.
Each arm names a channel operation, then `=>` and what to do, as a `match` arm does.
On line 14, `f` is the `Option` that `fruit.recv()` gave, in scope only in that arm.
Press Run.

When both channels have a value ready, `select` picks one of them.
The pick looks random but comes out the same on every run, and it gives each arm its turn, so one busy channel can't shut out the other.
