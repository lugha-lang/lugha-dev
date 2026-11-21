---
title: Typing None
start_error: E0412
error_note: A bare `None` says nothing about what a `Some` would hold, and `lughac` won't work it out from line 5, so the type has to be written.
---

`first_big` on line 2 starts as `None`, because no number over 6 has been found yet.
Line 5 sets it to `Some(n)` when the loop finds one.
Press Run.

The program doesn't run.
A bare `None` doesn't say what type a `Some` would hold, and, as with an empty array, `lughac` doesn't look ahead to line 5 for it.
E0412 says "cannot infer the type of `None`", at line 2.
The help shows the type written after a colon: `let x: Option<i64> = None;`.
Add `: Option<i64>` after `first_big` on line 2 and run again, or press Solve.
