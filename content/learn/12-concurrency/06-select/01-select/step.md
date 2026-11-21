---
title: select
---

With two channels, a `recv` on one would wait there while the other already has a value.
`select` on line 18 waits on both and takes whichever is ready first.
Each arm names a channel operation, then `=>` and what to do, as a `match` arm does.
On line 19, `f` is the `Option` that `fruit.recv()` gave, in scope only in that arm.
`send_late` on line 3 waits `first` milliseconds, then sends a word every 200, so `apple` comes at 100, `saw` at 200, `pear` at 300 and `drill` at 400.
Press Run.

Each pass of the loop takes the word that's ready, so the four words print in the order they were sent, and the last line is the scope's `Ok(())`.
When both channels have a value ready at once, `select` picks one of them, so a program shouldn't depend on which; the sleeps here keep the words apart.
