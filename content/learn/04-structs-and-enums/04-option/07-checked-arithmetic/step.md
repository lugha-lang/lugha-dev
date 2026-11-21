---
title: Checked arithmetic
start_output: 255\n
---

This is the program from Integer overflow, where `level + 10` stopped the program because 260 doesn't fit in a `u8`.
`checked_add` does the same addition and gives an `Option`: `Some` with the sum, or `None` where `+` would panic.
Press Run to see the panic again.

With `checked_add`, an overflow gives `None` instead of stopping the program.
On lines 3 and 4, write `level.checked_add(5).debug()` and `level.checked_add(10).debug()` in place of the sums, or press Solve.
