---
title: defer
---

`defer` sets a statement aside to run when the block it's in is left.
Line 3 defers a `console.println` that reads `n`, and line 4 changes `n` after it.
Press Run.

Line 5 prints first, `end of main: n is 2`.
The deferred line runs when `main` ends, after line 5, and reads `n` as it is then, so it prints `2` too.
