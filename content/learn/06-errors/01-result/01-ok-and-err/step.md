---
title: Ok and Err
---

A function whose work can fail can return a `Result`, so its caller can tell whether it worked.
`divide` on line 1 returns a `Result<i64, string>`: an `i64` answer, or a `string` saying why there isn't one.
Line 3 returns that string in an `Err` when the divisor is zero, and line 5 wraps the answer in `Ok`.
Like `Some`, `Ok` and `Err` can be written without the enum's name in front.
`Ok(a / b)` on line 5 doesn't say what the error type is, and it doesn't need to: the return type on line 1 says it's `string`.
Lines 9 and 10 print a division that works and one that fails, through `.debug()`, as an `Option` prints.
Press Run.

Line 9 prints `Ok(5)`, and line 10 prints the `Err` with its message.
