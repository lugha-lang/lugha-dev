---
title: Deferred values
start_error: E0456
---

`close` on line 1 is cleanup that can fail, so it gives back a `Result`, and line 7 defers it.
Press Run.

The program doesn't run.
A deferred statement's value would go nowhere, so it must have type `()`, and `close` gives a `Result<(), string>`.
E0456 says so, and its help says to handle the error inside it or discard it on purpose, with an example of a block holding a `let _ =`.
A block with only `close(console, "notes");` in it wouldn't do: that's a `Result` used as a statement, E0467.
Make line 7 `defer { let _ = close(console, "notes"); }`, which drops the `Result` on purpose, and run again, or press Solve.
