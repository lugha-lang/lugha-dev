---
title: Struct update syntax
---

Another way to get a changed point is to build a new one from the old.
Line 5 writes `x` and ends with `..p`, which takes every field not written, here `y`, from `p`.
Press Run.

Line 6 prints the new point, and line 7 prints `p` as it was: `..p` copies from `p` and leaves it alone.
`..p` has to come last, after the fields you write.
