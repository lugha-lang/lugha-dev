---
title: defer
---

`defer` sets a statement aside to run when the block it's in is left.
Line 3 defers a `console.println` that reads `n`, and line 4 changes `n` after it.
Press Run.

The deferred line prints `2`.
It runs when `main` ends, after line 5, and reads `n` as it is then.
