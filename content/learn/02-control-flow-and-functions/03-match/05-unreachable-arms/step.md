---
title: Unreachable arms
start_output: another day\n
---

The arms from step 1 are here, with `_` moved to the top, and `day` is still `3`.
Press Run.

It prints `another day`, and `lughac` warns with W0102, "unreachable match arm", for lines 5, 6 and 7.
Arms are tried from the top, and `_` matches every number, so no value ever reaches the arms after it.
Move the `_` arm from line 4 back to the end, or press Solve.
