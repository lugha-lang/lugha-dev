---
title: Fixed stand-ins
---

A test's `Clock`, `Env` and `Entropy` are stand-ins too.
Its `Clock`, on line 6, is fixed: `now_ms()` is `946684800000`, midnight UTC on 1 January 2000, and `monotonic_ms()` is `0`.
Its `Env`, on line 12, is empty, so even `PATH` is `None`.
Its `Entropy`, on line 17, is seeded, so it gives the same bytes on every run: line 18 checks the four this test gets.
Press Test.
