---
title: Passing capabilities on
---

`timed` on line 1 takes a `Console` and a `Clock` as ordinary parameters.
`main` on line 8 is given both, and passes them on to `timed` on line 9.
There are no global `println`, clock or file functions: a function reaches these only through a capability it's given.
Press Run.

`timed` prints `working on the report` through the console it was given.
Then `true`: `took`, the time it measured with the clock, isn't below 0.
