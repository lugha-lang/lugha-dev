---
title: Using a fake
---

`greeting` on line 9 takes a `Clock`, works out the hour in UTC from `now_ms()` on line 10, and picks a greeting on line 11.
It only calls `now_ms()`, so any `Clock` will do.
Lines 15 and 16 give it a `FixedClock` at 08:00 and at 14:00 UTC on 1 January 2026, and line 17 the real clock `main` was given.
Press Run.

The fake at 08:00 gives `good morning`, and the one at 14:00 `good afternoon`.
The real clock's answer depends on when the program runs, so line 18 prints only whether it's one of the two, and it is: `true`.
