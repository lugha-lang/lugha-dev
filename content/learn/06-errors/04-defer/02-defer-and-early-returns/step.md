---
title: defer and early returns
---

A defer runs on every way out of its block, a `return` or a `?` included.
`average` prints `starting` on line 9 and defers a line printing `finished` on line 10, before line 11 divides with `?`.
Lines 16 and 17 call it with a count of `2`, then `0`.
Press Run.

For the count of `2`, `average` prints `starting`, then `finished` as it ends, and line 16 prints `Ok(5)`.
For `0`, the `?` on line 11 returns the `Err` at once, but line 10's `defer` was already reached, so `finished` still prints before line 17 prints the `Err`.
So cleanup written as a `defer` near the top of a function also runs when a later `?` returns early.
