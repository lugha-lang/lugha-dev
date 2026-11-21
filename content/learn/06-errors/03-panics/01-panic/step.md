---
title: panic
---

`panic` stops the program with a message, as integer overflow and an out-of-bounds index did.
`check_age` on line 1 panics on line 3 when it's given a negative age, and line 10 passes it `-1`.
Press Run.

The panic prints its message and where it happened, `src/main.la:3:9`, and the program exits with code 101.
A panic isn't a value like an `Err` that the caller can match on.
Here it ends the program, so line 11 never prints `done`.
