---
title: cancel
---

`t.cancel(why)` stops one task, with a reason.
Line 11 starts `wait_long`, which would sleep five seconds and defers a line on line 4.
Line 13 cancels it a tenth of a second later, and line 14 joins it.
Press Run.

`stopped waiting` comes first: the task stops in its sleep and runs its `defer`.
The join on line 14 gives `Err(Cancelled(Requested("no longer needed")))`: the task was cancelled on request, with the reason given on line 13.
Cancelling one task doesn't fail the scope, so its value, on the last line, is `Ok(())`.
