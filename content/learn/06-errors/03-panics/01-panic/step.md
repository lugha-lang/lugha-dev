---
title: panic
---

`panic` stops the program with a message, as integer overflow and an out-of-bounds index did.
`check_age` on line 1 panics on line 3 when it's given a negative age.
Line 9 passes it `30`, and line 10 passes it `-1`.
Press Run.

Line 9 prints `30`.
Then the panic prints its message and where it happened, `src/main.la:3:9`.
`(stderr)` marks that line as written to stderr, the program's error output.
A panic isn't a value like an `Err` that the caller can match on: it ends the program, so line 11 never prints `done`.
The program exits with code 101.
