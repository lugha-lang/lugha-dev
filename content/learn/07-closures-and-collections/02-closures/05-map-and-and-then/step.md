---
title: map and and_then
---

`map` on an `Option` gives a new `Some` holding what the closure returns, and leaves a `None` as it is, as lines 2 and 3 show.
On a `Result`, `map` works on an `Ok` and leaves an `Err` as it is, on lines 6 and 7, as `map_err` did the other way.
`and_then` takes a closure that returns an `Option` or a `Result` itself, so the closure decides whether the answer is a success or a failure; lines 8 and 9 try it on `-3` and on `good`.
Line 9 writes its closure's return type: without it, `lughac` can't infer the `Result`'s error type, and stops with E0412.
Press Run.
