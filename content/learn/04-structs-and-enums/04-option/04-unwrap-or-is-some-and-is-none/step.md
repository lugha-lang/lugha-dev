---
title: unwrap_or, is_some and is_none
---

`is_none()` on line 12 and `is_some()` on line 13 say which variant an `Option` is, as a `bool`, without a `match`.
`unwrap_or(-1)` gives the value inside a `Some`, or `-1` for a `None`.
Press Run.

Line 12 prints `true`, since `"Dee"` isn't found, and line 13 prints `true`, since `"Ben"` is.
Line 14 prints `1`, the value inside `Some(1)`, and line 15 prints `-1` for the missing name.
