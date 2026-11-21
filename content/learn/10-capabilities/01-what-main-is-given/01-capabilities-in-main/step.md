---
title: Capabilities in main
---

Every program so far has taken `console: Console` and printed its output through it.
Files, the clock, environment variables, randomness, other programs and the network are reached the same way: through a value `main` is given, called a capability.
`debug` and `panic` write to standard error without one.
`main` takes the ones it needs as parameters, matched by type, with any names, in any order: `Console`, `Fs`, `Clock`, `Env`, `Entropy`, `Proc` and `Net`, and `string[]` for the program's arguments.
Line 1 takes a `Clock`, then the `Console`.
Line 2 reads the clock with `monotonic_ms()`, a time for measuring how long something takes, and line 4 reads it again.
Press Run.

`hello` prints from line 3.
Then `true`: the second reading, on line 4, is no earlier than the first.
