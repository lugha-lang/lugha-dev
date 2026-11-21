---
title: defer and early returns
---

A defer runs on every way out of its block, a `return` or a `?` included.
`average` prints `starting` on line 9 and defers `finished` on line 10, before line 11 divides with `?`.
For a count of `0`, the `?` on line 11 returns the `Err` at once, after line 10's `defer` was reached.
Press Run.

Each call prints `finished`, the failed one too, right before its result.
So cleanup written as a `defer` near the top of a function also runs when a later `?` returns early.
