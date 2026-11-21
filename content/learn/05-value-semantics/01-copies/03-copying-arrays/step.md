---
title: Copying arrays
---

`xs` on line 2 is an array, and line 3 assigns it to `ys`.
Arrays follow the same rule as structs: `ys` starts as an array of its own, a copy of `xs`, not a second name for the same one.
Line 4 pushes `1` onto `ys`.
Press Run.

Line 5 prints `xs` as it was, `[5, 6]`, and line 6 prints `ys` with the `1` on its end.
