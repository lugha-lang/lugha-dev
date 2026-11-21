---
title: Integer literals
---

However a whole number is written, it prints in plain decimal.
Line 2 groups its digits with `_`, and lines 3 to 5 write hex with `0x`, binary with `0b` and octal with `0o`.
Line 6 writes `017`, with a leading zero.
Press Run.

Warning W0107 comes first: a leading zero doesn't make a number octal, so `017` is seventeen.
Its location line points at line 6, and its help line suggests `0o17` for octal, or plain `17`.
A warning doesn't stop the program, so the numbers print after it.
Lines 2 to 5 give `1000000`, `255`, `10` and `15`, and line 6 gives `17`.
