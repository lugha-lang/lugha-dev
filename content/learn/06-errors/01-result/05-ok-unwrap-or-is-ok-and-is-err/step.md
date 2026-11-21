---
title: ok, unwrap_or, is_ok and is_err
---

Line 9's division works, and line 10's fails.
`ok()` on lines 11 and 12 turns a `Result` into an `Option`, dropping the error.
`unwrap_or` on lines 13 and 14 gives the answer, or `0` when the division failed.
`is_ok()` and `is_err()` on lines 15 and 16 tell whether a division worked or failed.
Press Run.

Lines 11 and 12 print `Some(5)` and `None`, and lines 13 and 14 print `5` and `0`.
Lines 15 and 16 both print `true`, since `good` worked and `bad` failed.
