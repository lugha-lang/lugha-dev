---
title: Overlapping blocks
start_error: E0452
---

A block can take type parameters, as line 9 does: it covers `T[]` for every `T` that has `Describe`.
Line 13 adds a block for `i64[]`.
Line 20's `[1, 2, 3]` is an `i64[]`, and line 21's `[[1], [2]]` is an `i64[][]`, which line 9 covers because `i64[]` has `Describe` through it.
Press Run.

E0452 on line 13: "two `derive Describe` blocks cover `i64[]`": each type gets its items from exactly one block, and lines 9 and 13 both cover `i64[]`.
Remove lines 13 to 15, or press Solve.
E0452 has a second cause: a block must be in the module that declares its interface, so `derive Display for i64` in this file is E0452 as well, as `impl Display for bool` was E0459 in Interfaces.
