---
title: Interface conversion
start_error: E0403
error_note: `total` needs a `Shape[]`, and `circles` is a `Circle[]`. Each `Circle` can become a `Shape`, but an array of them can't, so give the array its type where it's built.
---

An interface value converts only to an interface its own extends: with the last lesson's `Pet: Named`, a `Pet` converts to a `Named`, but converting it to another interface `Dog` implements is E0422.
`total` on line 16 takes a `Shape[]`, and line 20 passes `circles`, a `Circle[]`.
Press Run.

The program doesn't run.
A value becomes a `Shape` one at a time, never as an array or an `Option` around it.
E0403 says so at the call on line 20: "expected Shape[], found Circle[]".
An array's type is fixed where it's built, so make `circles` a `Shape[]` there.
Add `: Shape[]` after `circles` on line 19 and run again, or press Solve.
