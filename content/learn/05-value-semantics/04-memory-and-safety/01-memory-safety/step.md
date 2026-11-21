---
title: Memory safety
---

`numbers` on line 1 builds an array on line 2 and returns it, and line 7 keeps it in `kept` after `numbers` has finished.
The array stays as long as `kept` holds it.
Press Run.

It prints `[1, 2, 3]`: the array's memory is given back only once nothing holds it, so `kept` doesn't reach memory that was freed.
Option showed that there's no null, and Bounds checking that reading past the end of an array stops the program.
