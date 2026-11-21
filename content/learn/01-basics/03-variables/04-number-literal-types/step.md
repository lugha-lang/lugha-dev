---
title: Number literal types
start_error: E0402
error_note: `300` is multiplied by `height`, a `u8`, so it has to be a `u8` too, and a `u8` holds only 0 to 255.
---

A number written in the code, called a literal, takes its type from what's around it.
Nothing decides for line 2's `7`, so it gets `i64`, the default for a whole number; a number with a `.` gets `f64`.
Line 3 declares `height` as a `u8`, a whole number from 0 to 255, and line 4 multiplies it by `300`.
Press Run.

The program doesn't run: E0402 says "integer literal out of range for u8", pointing at line 4's `300`.
The `300` takes its type from `height` on the other side of the `*`, so it has to be a `u8`, which holds 0 to 255, as the help line says.
Arithmetic on two `u8`s gives a `u8`, so `scaled` is a `u8` too, and the result has to fit as well.
Change `300` to `30`, making 210, and run again, or press Solve.
