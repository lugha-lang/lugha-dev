---
title: Capabilities are interfaces
start_error: E0422
error_note: `impl Clock for FixedClock` has to write every method of `Clock`, and `Clock` has three. Lines 4 and 5 write `now_ms` and `monotonic_ms`, but nothing writes `local_offset`.
---

Each capability is an interface, so a type of your own can implement it.
`FixedClock` on line 1 is a clock that always says the same time, and `impl Clock for FixedClock` on lines 3 to 6 gives it `now_ms` and `monotonic_ms`.
Line 11 puts one in a variable of type `Clock`, an interface value.
Press Run.

The program doesn't run.
E0422 on line 3 says the `impl` "doesn't match `Clock`", and its help names what's missing: "no method `local_offset`".
Besides the two methods shown earlier, `Clock` has a third, `local_offset`: the local time's offset from UTC at a moment, in seconds.
An `impl` has to write every method the interface doesn't give a default for.
After line 5, add `fun local_offset(self, ms: i64): Result<i64, string> = Ok(0);`, an offset of 0, and run again, or press Solve.
