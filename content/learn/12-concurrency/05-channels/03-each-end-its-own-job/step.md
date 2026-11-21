---
title: Each end its own job
start_error: E0415
error_note: `rx` is the `Receiver` end of the channel, and a `Receiver` has no `send` method: only the `Sender` end, `tx`, can send.
---

Line 2 makes a channel and its two ends, `tx` and `rx`, and line 3 sends through `rx`.
Press Run.

The program doesn't run.
E0415 says there's "no method `send` on `Receiver<string>`", on line 3, and its help says why: only a `Sender` can `send`, and `rx` is the `Receiver` end.
Each end has only its own methods, so a function given a `Receiver` can only receive, and one given a `Sender` can only send and close.
Change `rx.send` to `tx.send` on line 3 and run again, or press Solve.
