---
title: Capabilities in main
---

Every program so far has taken `console: Console` and printed its output through it.
Files, the clock, environment variables, randomness, other programs and the network are reached the same way: through a value `main` is given, called a capability.
`debug` and `panic` write to standard error without one.
`main` takes the ones it needs as parameters, matched by type, with any names, in any order: `Console`, `Fs`, `Clock`, `Env`, `Entropy`, `Proc` and `Net`, and `string[]` for the program's arguments.
`main` on line 1 takes a `Clock` and then the `Console`, and line 2 reads the clock.
Press Run.

`monotonic_ms()` is a time for measuring how long something took; the rest of `Clock` is in Clock, Env and Entropy.
