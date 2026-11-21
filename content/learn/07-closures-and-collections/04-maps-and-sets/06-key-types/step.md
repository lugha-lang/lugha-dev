---
title: Key types
start_error: E0422
---

Keys can be integers, strings, `bool`s and `char`s, and a map or set finds each one by its hash and `==`.
`grid` on line 4 uses `Point`s as keys, for the cells of a grid.
Press Run.

E0422 on lines 4 to 7: "`Point` doesn't implement `Key`".
Like `with Eq` in Structs, `with Key` after the declaration gives `Point` what a key needs.
Add `with Key` after the `}` on line 1, or press Solve.
A float is never a key: `Map { 0.25: "small" }` is E0451, whose help gives the reason, "`NaN != NaN`, so a float key could never be found again".
