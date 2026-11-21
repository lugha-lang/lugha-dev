---
title: Interfaces extending interfaces
start_error: E0415
error_note: `Dog` has no `name` method: `impl Pet for Dog` gives it `sound`, but `name` belongs to `Named`, and nothing implements `Named` for `Dog` yet.
---

`Pet` on line 5 extends `Named`: `interface Pet: Named` means every `Pet` is a `Named` too.
Line 11 implements `Pet` for `Dog`, and line 17 calls both `name` and `sound`.
Press Run.

The program doesn't run.
Implementing `Pet` doesn't implement `Named` for you, so `Dog` has `sound` but no `name`.
E0415 says so first, at the call on line 17: "no method `name` on `Dog`".
E0422 gives the cause, on line 11: "`Dog` implements `Pet` but not `Named`, which `Pet` extends".
Each interface gets its own block: `name` written inside `impl Pet for Dog` is E0422, "`name` isn't an item of `Pet`".
The help's first way, `with Named`, is E0462 here: `with` asks for an interface built from derive blocks, as `Eq` is, and `Named` has none.
The second way, an `impl Named for Dog` block, is the fix.
Above line 11, add an `impl Named for Dog` block with `fun name(self): string = "dog";` in it, and run again, or press Solve.
