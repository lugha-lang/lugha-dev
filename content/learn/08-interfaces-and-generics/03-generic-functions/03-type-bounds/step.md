---
title: Type bounds
start_error: E0404
---

`first` only passed its `T` along, which any type allows.
`count_of` counts how often `wanted` is in `xs`, and compares two `T`s with `==` on line 4.
Press Run.

The program doesn't run.
Not every type has `==`, so a `T` has none until the function says it needs one.
E0404 says so on line 4, "cannot apply `==` to T", and its help gives the fix: declare `T: Eq`.
That's a bound, an interface `T` must implement: `Eq` for `==`, `Ord` for `<` and `sort`, `Key` for map keys, or one of your own, like `T: Shape`.
Several bounds join with `+`, as in `T: Ord + Key`.
Calling a bounded function with a struct or enum of your own that misses one is E0422 at the call: `count_of` on a `Point` without `with Eq` says "`Point` doesn't implement `Eq`".
Add `: Eq` after `T` on line 1 and run again, or press Solve.
