---
title: Struct update syntax
---

Another way to get a changed point is to build a new one from the old.
Line 5 writes `x` and ends with `..p`, which takes every field not written, here `y`, from `p`.
`..p` has to come last, after the fields that are written.
Press Run.

Line 6 prints the new point, `Point { x: 10, y: 4 }`.
Line 7 prints `p` as it was, `Point { x: 3, y: 4 }`: `..p` copies from `p` and leaves it alone.
