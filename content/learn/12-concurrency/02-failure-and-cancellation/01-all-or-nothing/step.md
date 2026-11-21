---
title: All or nothing
---

A task that returns a `Result` fails when it gives an `Err`, and a task that panics fails too.
Line 17 starts `worker`, which would sleep two seconds, and line 18 starts `check(-1)`, which gives an `Err` after a tenth of a second.
`worker` defers a line on line 4, as in defer, and prints another on line 6 if it gets that far.
Press Run.

By default a scope is all or nothing: when `check` fails, the scope cancels `worker`, which stops in its sleep and runs its `defer` on the way out.
`worker finished` never prints, and the scope's value is an `Err`, so line 21 prints `true`.
