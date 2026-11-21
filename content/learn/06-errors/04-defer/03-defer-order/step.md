---
title: Defer order
---

When a block has several defers, they run last first.
Lines 2 and 3 defer two lines in `main`.
Line 5's defer is inside the loop's body, so it belongs to the body, not to `main`, and runs at the end of each pass.
Press Run.

Each pass prints `pass {i}` from line 6, then `end of pass {i}` from its defer as the pass ends.
Then line 8 prints `end of main`, and as `main` ends its defers run last first: line 3's `second defer`, then line 2's `first defer`.
