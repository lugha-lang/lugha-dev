---
title: Type bounds
start_error: E0404
---

`first` only passed its `T` along, which any type allows, but `count_of` compares two `T`s with `==` on line 4.
Press Run.

`lughac` stops at line 4 with E0404, "cannot apply `==` to T", and its help gives the fix: declare `T: Eq`.
A bound is an interface `T` must implement: `Eq` for `==`, `Ord` for `<` and `sort`, `Key` for map keys, or one of your own, like `T: Shape`.
Add `: Eq` after `T` on line 1, or press Solve.
Several bounds join with `+`, as in `T: Ord + Key`.
Calling a bounded function with a struct or enum of your own that misses one is E0422 at the call: `count_of` on a `Point` without `with Eq` says "`Point` doesn't implement `Eq`".
