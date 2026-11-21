---
title: Overlapping blocks
start_error: E0452
---

A block can take type parameters, as line 9 does: it covers `T[]` for every `T` that has `Describe`.
Line 13 adds a block for `i64[]`.
Line 20's `[1, 2, 3]` is an `i64[]`.
Line 21's `[[1], [2]]` is an `i64[][]`, an array of `i64[]`s, so line 9 covers it with `i64[]` as its `T`.
A block must also be in the module that declares its interface: `derive Display for i64` in this file would be E0452 too, as `impl Display for bool` is E0459.
Press Run.

The program doesn't run.
Each type gets its items from exactly one block, and lines 9 and 13 both cover `i64[]`.
E0452 says so on line 13: "two `derive Describe` blocks cover `i64[]`".
Its help says to remove or narrow one of them.
Remove lines 13 to 15 and run again, or press Solve.
