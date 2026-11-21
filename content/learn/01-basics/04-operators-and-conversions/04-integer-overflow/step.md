---
title: Integer overflow
---

Arithmetic on whole numbers never wraps around the way `truncate` does: when a result won't fit, the program stops.
`level` is a `u8` holding 250, so line 3 prints `255`, its largest value, and line 4 adds 10.
Press Run.

After `255`, the program panics with `integer overflow`, names the line and column, and exits with code 101.
Dividing a whole number by zero stops a program the same way, while a float divided by zero doesn't stop it: `1.0 / 0.0` gives `inf`.
