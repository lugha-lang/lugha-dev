---
title: Capabilities are interfaces
start_error: E0422
---

Each capability is an interface, so a type of your own can implement it, as in Interfaces.
`FixedClock` on line 1 is a clock that always says the same time, and `impl Clock for FixedClock` on lines 3 to 6 gives it `now_ms` and `monotonic_ms`.
Line 11 puts one in a `Clock`, an interface value, as in Interface values.
Press Run.

E0422 on line 3, and its help names what's missing: Clock, Env and Entropy showed two of `Clock`'s methods, and it has a third, `local_offset`, the time zone's offset from UTC at a moment, in seconds east.
An `impl` has to write every method the interface doesn't give a default for, as in Interfaces.
After line 5, add `fun local_offset(self, ms: i64): Result<i64, string> = Ok(0);`, an offset of 0, or press Solve.
