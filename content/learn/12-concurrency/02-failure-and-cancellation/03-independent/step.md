---
title: independent
---

`independent` after the scope's name, as on line 13, lets each task fail alone: when one fails, the others run on and the scope stays `Ok`.
Line 14 starts `crash`, which panics at once, and line 15 starts `slow`, which takes 200 milliseconds.
Lines 16 and 17 join each.
A join gives `Err` when the task didn't finish normally, with why it stopped.
Press Run.

The first line, from line 16, is `crash`'s join: `Err` with `Panicked` and the panic's message.
The second, from line 17, is `Ok(7)`: `slow` finished though `crash` failed first.
The third is the scope's value, `Ok(())`.
The line marked `(stderr)` is the panic's message again, as ``task `crash` panicked: …``.
In step 2, a scope that wasn't `independent` reported the failure in its value; an `independent` scope stays `Ok`, so it prints each failure to standard error instead, once the task has stopped.
