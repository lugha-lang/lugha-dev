---
title: Memory safety
---

`numbers` on line 1 makes an array on line 2 and returns it.
Line 7 keeps that array in `kept`, after `numbers` has finished.
Press Run.

It prints `[1, 2, 3]`.
The array is still there after `numbers` has finished, because its memory is freed only once nothing holds it.
While `kept` holds it, it stays, so `kept` never points at freed memory.
Lugha also has no null, and reading past the end of an array stops the program.
