---
title: Fixed stand-ins
---

A test's `Clock`, `Env` and `Entropy` are stand-ins too, not the real ones.
Its `Clock`, on line 6, is fixed: `now_ms()` is `946684800000`, midnight UTC on 1 January 2000, and `monotonic_ms()` is `0`.
Its `Env`, on line 12, is empty, so even `PATH` is `None`.
Its `Entropy`, on line 17, is seeded, which means it gives the same bytes on every run: line 18 checks the four it gives this test, and another test would get other bytes.
Press Test.

All three tests are `ok`, and the last line counts 3 passed and 0 failed.
