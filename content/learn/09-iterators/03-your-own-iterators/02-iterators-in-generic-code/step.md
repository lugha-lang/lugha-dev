---
title: Iterators in generic code
---

`Iter<i64>` is an interface, so it can be a bound, as in Generic functions.
`total` on line 13 takes any `I: Iter<i64>` and adds up what its loop gives.
Line 22 passes a `Countdown`, line 23 a `range`, and line 24 a `map` over an array's iterator: three different iterators, each an `Iter<i64>`.
Press Run.
