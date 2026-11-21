---
title: Narrowing conversions
start_error: E0469
---

`total` is `300`, an `i64`, and lines 3 and 4 convert it with `as` to a `u8` and an `f64`.
Lines 5 and 6 use methods, functions called on a value after a `.`.
Press Run.

The program doesn't run, and E0469 shows for each `as`.
`as` goes by the types, not the value: an `i64` can be too big for a `u8`, and some `i64` values are too large for an `f64` to hold exactly.
The help lines name methods that convert instead, with the target type in `<…>`, each named for what it does when a number doesn't fit.
`truncate<u8>()` keeps the lowest 8 bits, so `300` becomes `44`, and `round<f64>()` takes the nearest `f64`.
Line 5's `saturate<u8>()` stops at the largest `u8`, and line 6's `try_into<u8>()` gives an `Option`, a value that may be missing, and `is_some()` says whether it has one.
Put `total.truncate<u8>()` in place of `total as u8` on line 3 and `total.round<f64>()` in place of `total as f64` on line 4, or press Solve.
