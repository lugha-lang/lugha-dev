---
title: Iterators in generic code
---

`Iter<i64>` is an interface, so it can be a bound on a type parameter.
`total` on line 13 takes any `I` that is an `Iter<i64>`, and its loop on lines 15 to 17 adds up the values.
Line 22 passes it a `Countdown` from 4, line 23 a `range` from 1 to 4, and line 24 a `map` over an array's iterator: three different iterators, each an `Iter<i64>`.
Press Run.

The `Countdown` gives 4, 3, 2 and 1, which add up to `10`.
The range gives 1 to 4, also `10`.
The `map` gives `20` and `30`, so the last line is `50`.
