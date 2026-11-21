---
title: Interface conversion
start_error: E0403
---

`total` on line 16 takes a `Shape[]`, and line 20 passes `circles`, a `Circle[]`.
Press Run.

The call on line 20 is E0403, "expected Shape[], found Circle[]".
The conversion from the first step happens to a single value, never to an array or an `Option` around it.
An array's type is fixed where it's built, so make `circles` a `Shape[]` there: add `: Shape[]` after `circles` on line 19, or press Solve.
An interface value converts to another interface only if its own extends it: a `Pet` from Interfaces converts to a `Named`, but converting it to an interface `Loud` that `Dog` implements and `Pet` doesn't extend is E0422.
