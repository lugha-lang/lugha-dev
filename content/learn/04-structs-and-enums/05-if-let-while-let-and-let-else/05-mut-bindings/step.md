---
title: mut bindings
start_error: E0501
---

Line 5 adds 1 to `n`, the number inside `count`.
Press Run.

E0501 says `n` is not mutable: names in a pattern are read-only, like parameters.
The help suggests copying `n` into a `let mut`.
`mut` before the name in the pattern does that in one step, giving the arm its own copy to change.
`count` itself stays `Some(4)`, as line 10 shows.
Change `.Some(n)` on line 4 to `.Some(mut n)`, or press Solve.
