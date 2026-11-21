---
title: impl Debug
---

A debug form can be written by hand too, with `impl Debug for Version` and its one method, `debug`, on lines 3 to 5.
Line 9 prints a version's debug form, line 10 an array's, and line 11 an `Option`'s.
Press Run.

The hand-written form is used wherever a `Version`'s debug form is, inside the array and the `Option` too.
