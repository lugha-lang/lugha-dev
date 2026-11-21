---
title: Each end its own job
start_error: E0415
---

Line 3 sends through `rx`.
Press Run.

E0415: "no method `send` on `Receiver<string>`", and the help says why: only a `Sender` can `send`.
Each end has only its own methods, so a function given a `Receiver` can only receive, and one given a `Sender` only send and close.
Change `rx.send` to `tx.send` on line 3, or press Solve.
