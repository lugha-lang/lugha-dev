---
title: independent
---

`independent` after the scope's name, as on line 13, lets each task fail alone: when one fails, the others run on and the scope stays `Ok`.
Line 14 starts `crash`, which panics at once, and line 15 starts `slow`, which takes 200 milliseconds.
Lines 16 and 17 join each, and a join gives `Err` with why the task stopped, here `Panicked` with its message.
Press Run.

`slow` finishes and gives `Ok(7)` though `crash` failed first, and the scope's value is `Ok(())`.
The panic's message also goes to standard error, as ``task `crash` panicked: …``.
