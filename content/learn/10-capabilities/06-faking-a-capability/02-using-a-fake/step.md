---
title: Using a fake
---

`greeting` on line 9 takes a `Clock` and works out the hour from `now_ms()`, in UTC.
It only calls `now_ms()`, so any `Clock` will do: lines 15 and 16 give it a `FixedClock` at 08:00 and at 14:00 UTC on 1 January 2026, and line 17 the real clock `main` was given.
Press Run.

The real clock's answer depends on when the program runs, so line 18 prints only whether it's one of the two.
