---
title: Deferred values
start_error: E0456
---

`close` on line 1 is cleanup that can fail, so it gives back a `Result`, and line 7 defers it.
Press Run.

E0456: a deferred statement must have type `()`, and `close` gives a `Result<(), string>`.
Make line 7 `defer { let _ = close(console, "notes"); }`, which drops the `Result` on purpose, or press Solve.
A block with only `close(console, "notes");` in it is E0467, as in Results can't be ignored.
