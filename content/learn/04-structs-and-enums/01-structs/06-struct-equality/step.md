---
title: Struct equality
start_error: E0422
---

Line 6 compares two points with `==`.
Press Run.

E0422 says `Point` doesn't implement `Eq`, which `==` and `!=` need.
Writing `with Eq` after the declaration gives `Point` both, and `==` then compares the two field by field.
Add `with Eq` after the `}` on line 1, or press Solve.
