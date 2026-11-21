---
title: Integer overflow
---

`level` is a `u8` holding 250.
Line 3 adds 5, which makes 255, the largest `u8`, and line 4 adds 10.
Press Run.

Line 3 prints `255`.
Line 4's sum, 260, doesn't fit in a `u8`, so the program stops there: it panics.
The panic's message, `integer overflow at src/main.la:4:27`, goes to stderr, the program's error output, and points at the `+` on line 4.
"Exited with code 101" is the code a panic exits with.
Whole-number arithmetic never keeps only the lowest bits the way `truncate` does, which would have turned 260 into 4: it stops instead.
Dividing a whole number by zero panics the same way.
