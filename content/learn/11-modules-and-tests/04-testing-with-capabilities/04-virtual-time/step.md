---
title: Virtual time
---

`task.sleep(ms)`, from the module `std.task` that line 1 imports, pauses for that many milliseconds.
On this site each test has 5 seconds to run, and the test on line 8 sleeps for 10 seconds on line 9.
Press Test.

The test is `ok` at once.
A test runs on virtual time, where sleeping takes no real time, so the 10 seconds pass without any waiting.
