---
title: Interfaces extending interfaces
start_error: E0415
---

`Pet` on line 5 extends `Named`: `interface Pet: Named` means every `Pet` is a `Named` too.
Line 11 implements `Pet` for `Dog`, and line 17 calls both `name` and `sound`.
Press Run.

E0422 on line 11: "`Dog` implements `Pet` but not `Named`, which `Pet` extends".
Implementing `Pet` doesn't implement `Named` for you, and E0415 on line 17 follows: `Dog` has no `name`.
Above line 11, add an `impl Named for Dog` block with `fun name(self): string = "dog";` in it, or press Solve.
Each interface gets its own block: `name` written inside `impl Pet for Dog` is E0422, "`name` isn't an item of `Pet`", and the help's `with Named` is E0462 here, since `with` needs derive blocks, which come in Deriving.
