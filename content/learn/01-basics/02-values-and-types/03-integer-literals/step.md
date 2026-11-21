---
title: Integer literals
---

Whole numbers print in plain decimal, however you write them.
Lines 2 to 5 use `_` between digits, then `0x`, `0b` and `0o` for hex, binary and octal.
Line 6 writes `017`.
Press Run.

It prints `17`, with warning W0107, because a leading zero changes nothing.
Octal needs `0o`, as on line 5.
