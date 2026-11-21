---
title: Printing structs
start_error: E0422
---

Line 5 prints `p` itself.
Press Run.

E0422 says `Point` doesn't implement `Display`, the same error an array gave in Arrays.
The help offers `impl Display`, which comes in chapter 8, or `.debug()`, which works now.
Add `.debug()` after `p` on line 5, or press Solve.
A struct's debug form is its name, then each field and its value in braces, in the order `Point` declares them.
