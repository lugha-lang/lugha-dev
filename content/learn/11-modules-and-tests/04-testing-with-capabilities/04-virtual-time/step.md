---
title: Virtual time
---

`task.sleep(ms)`, from `std.task` on line 1, pauses for that many milliseconds; Concurrency uses it more.
On this site each test has 5 seconds to run, and the test on line 8 sleeps for 10 seconds on line 9.
Press Test.

It passes at once: a test runs on virtual time, where sleeping takes no real time.
