---
title: cancel
---

`t.cancel(why)` stops one task, with a reason.
Line 11 starts `wait_long`, which would sleep five seconds, and line 13 cancels it a tenth of a second later.
Line 14 joins it, and the join gives `Err` with why the task stopped, as in step 3.
Press Run.

The task stops in its sleep and runs its `defer`, and its join is `Err(Cancelled(Requested("no longer needed")))`, the reason given on line 13.
Cancelling one task doesn't fail the scope: its value is `Ok(())`.
