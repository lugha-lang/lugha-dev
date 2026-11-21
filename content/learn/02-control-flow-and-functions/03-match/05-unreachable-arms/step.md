---
title: Unreachable arms
start_output: another day\n
---

The arms from step 1 are here, with `_` moved to the top, as line 4, and `day` is still `3`.
Press Run.

Three W0102 warnings come first, "unreachable match arm", for lines 5, 6 and 7.
Arms are tried from the top, and `_` matches every number, so no value ever reaches the arms after it.
A warning doesn't stop the program, so it runs and prints `another day`, from line 4, though `day` is `3`.
Move the `_` arm from line 4 back to the end and run again, or press Solve.
