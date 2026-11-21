---
title: Tuple patterns
---

A `match` can look inside a tuple too.
Line 2 puts `x` and `y` into one, so that a single `match` checks both.
Each arm's pattern is a tuple of patterns, and `_` inside one matches anything in that position: `(0, _)` on line 4 matches any point whose `x` is `0`, the origin included.
Arms are tried from the top, so `(0, 0)` on line 3 comes first, or the origin would land in the y-axis arm.
The `_` on line 6 covers every other case, as a `match` must.
Press Run.

Line 11's `describe(0, 4)` matches `(0, _)`, so it prints `on the y axis`.
Line 12's `describe(2, 3)` matches none of the first three arms and lands in `_`, so it prints `somewhere else`.
