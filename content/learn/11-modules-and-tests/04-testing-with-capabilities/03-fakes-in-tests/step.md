---
title: Fakes in tests
start_failing: afternoon
---

`greeting` and `FixedClock` on lines 1 to 12 are the ones from Faking a capability.
The test on line 19 takes the test's `Clock` and expects `greeting` to say `good afternoon`.
Press Test.

The test's clock is the fixed one from Fixed stand-ins, midnight UTC on 1 January 2000, so `greeting` says `good morning`.
To test the afternoon, give `greeting` a `FixedClock` at an afternoon hour instead.
Make line 19 `fun afternoon() {`, with no parameter, and line 20 `assert_eq(greeting(FixedClock { at: 1767276000000 }), "good afternoon");`, 14:00 UTC on 1 January 2026, or press Solve.
