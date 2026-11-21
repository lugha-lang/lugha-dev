---
title: Parsing numbers
start_error: E0404
error_note: `n` is an `Option<i64>`, not a number, so `+` can't add `1` to it. Take the number out first, with `unwrap_or`.
---

`parse_i64` reads a string that is only a whole number, with an optional `-` in front.
Its result is an `Option<i64>`: `Some` with the number, or `None` for text such as `"4.5"` or `"nine"`.
Line 3 parses `"41"`, and line 4 adds `1` to what it gave back.
Press Run.

The program doesn't run.
E0404 says "cannot apply `+` to `Option<i64>` and i64", at line 4: the number is still inside the `Option`.
`unwrap_or(0)` takes it out, with `0` standing in when the text isn't a number.
Add `.unwrap_or(0)` after `parse_i64(typed)` on line 3 and run again, or press Solve.
