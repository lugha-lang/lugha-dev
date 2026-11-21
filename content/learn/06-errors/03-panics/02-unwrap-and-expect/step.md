---
title: unwrap and expect
---

`unwrap` takes the value out of a `Some` or an `Ok`, and panics when there isn't one.
`expect` does the same, but panics with a message you give it.
Line 2 unwraps `parse_i64("42")`, which is `Some(42)`, so `n` is `42`.
Line 4 calls `expect` on `parse_i64("forty")`, which is `None`.
Press Run.

Line 3 prints `42`.
Then `expect` panics with its message, and the place the panic names, `src/main.la:4:32`, is line 4, where `expect` was called, so the place to look is in your own code.
`unwrap` would have panicked there too, with `unwrap on None`, and on an `Err` its message includes the error, such as `unwrap on Err: "division by zero"`.
