---
title: Typing None
start_error: E0412
---

`first_big` on line 2 starts as `None`, because no number over 6 has been found yet.
Line 5 sets it to `Some(n)` when the loop finds one.
Press Run.

`lughac` stops at line 2 with E0412, "cannot infer the type of `None`".
As with an empty array, the type has to be known where `None` is written, and `lughac` doesn't look ahead to line 5 for it.
Add `: Option<i64>` after `first_big` on line 2, or press Solve.
