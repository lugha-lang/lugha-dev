---
title: Fakes in tests
start_failing: afternoon
---

`greeting`, on lines 1 to 4, says `good morning` before 12:00 UTC and `good afternoon` after.
`FixedClock`, on lines 6 to 12, is a `Clock` whose time is whatever its `at` field holds.
The test on line 19 takes the test's `Clock` and expects `greeting` to say `good afternoon`.
Press Test.

`afternoon` is `FAILED`: the test's `Clock` is the fixed stand-in, at midnight UTC on 1 January 2000, so `greeting` says `good morning`.
The panic under it shows both values, left "good morning" and right "good afternoon", from `assert_eq` on line 20.
To test the afternoon, give `greeting` a `FixedClock` set to an afternoon hour: `1767276000000` is 14:00 UTC on 1 January 2026.
Make line 19 `fun afternoon() {`, with no parameter, and line 20 `assert_eq(greeting(FixedClock { at: 1767276000000 }), "good afternoon");`, and press Test again, or press Solve.
