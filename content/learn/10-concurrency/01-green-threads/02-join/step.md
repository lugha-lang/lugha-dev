---
title: join
---

Each `spawn` gives back a handle to its thread.
`spawn square(3)` gives a `Task<i64>`, where `i64` is what the call returns; a call that returns nothing, like `count` in step 1, gives a plain `Task`.
`a.join()` waits for the thread to finish and gives a copy of its result, so line 6 adds 9 and 16 and prints 25.
Joining again, on line 7, gives another copy at once.
`spawn` also takes a closure followed by `()`, as on line 10, and it captures `k` by copy, as any closure does.
Press Run.

That copy is why `spawn xs.push(1)` is E0438: the new thread would push to its own copy of `xs`, and nobody would see it.
