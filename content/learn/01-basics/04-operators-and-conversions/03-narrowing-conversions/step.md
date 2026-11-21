---
title: Narrowing conversions
start_error: E0469
---

Lines 3 and 4 convert `total`, an `i64`, to a `u8` and an `f64` with `as`.
Press Run.

`lughac` gives E0469 for both.
`as` goes by the types, not the value: an `i64` can be too big for a `u8`, or too large for an `f64` to hold exactly.
Methods do these conversions instead, with the target type in `<…>`, each named for what it does when a number doesn't fit.
`truncate<u8>()` keeps the lowest 8 bits, so `300` becomes `44`, and `round<f64>()` takes the nearest `f64`.
Lines 5 and 6 already use two more: `saturate<u8>()` stops at the largest `u8`, and `try_into<u8>()` gives a value only when it fits, which `is_some()` checks.
Write `total.truncate<u8>()` on line 3 and `total.round<f64>() / 7.0` on line 4, or press Solve.
