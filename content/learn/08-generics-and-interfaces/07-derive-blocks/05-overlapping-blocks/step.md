---
title: Overlapping blocks
start_error: E0452
---

A block can take type parameters, as line 9 does: it covers `T[]` for every `T` that meets `Describe`.
Line 13 adds a block for `i64[]`.
Line 23's array of arrays is covered by line 9 too, since `i64[]` meets `Describe` through it.
Press Run.

`lughac` gives E0452 on line 13: both blocks cover `i64[]`, and each type gets its items from one block.
Remove lines 13 to 15; Solve does it for you.

E0452 has a second cause: a block must be in the module that declares its interface.
A file is a module, as Modules will show, and `Display` is declared in the prelude.
So `derive Display for i64` in this file is E0452 as well.
