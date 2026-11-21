---
title: String interpolation
---

A string can hold values: line 4 puts `name` and `points` inside it, each in braces.
Each pair of braces is replaced by the value of what's inside it, written the way `console.println` would print it.
The braces can hold any expression, such as `points * 2` on line 5.
Press Run.

Line 4 prints `Amina has 7 points`, and line 5 prints `doubled: 14`.
A value with no text form of its own, such as an array, needs its `.debug()` inside the braces, as it does in `console.println`.
