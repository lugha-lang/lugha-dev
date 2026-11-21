---
title: Copying arrays
---

Arrays follow the same rule.
`ys` on line 3 starts as a copy of `xs`, and line 4 pushes onto `ys`.
Press Run.

Line 5 prints `[5, 6]`, because `let mut ys = xs` gave `ys` an array of its own, not a second name for the one in `xs`.
