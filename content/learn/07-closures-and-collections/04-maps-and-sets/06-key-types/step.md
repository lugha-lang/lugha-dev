---
title: Key types
start_error: E0422
error_note: A map's keys must be `Key`, so the map can find each one again by its hash and `==`. `Point` isn't, and `with Key` after its declaration makes it one.
---

Keys can be integers, strings, `bool`s and `char`s.
A map or set finds each key by its hash, a number worked out from the key, and by `==`.
`grid` on line 4 is a map with `Point`s as keys, for the cells of a grid, and lines 5 to 7 use `Point`s to set and read cells.
Press Run.

The program doesn't run.
A key's type must be `Key`, which gives it the hash and the `==`, and `Point` isn't.
E0422 says so at each line that uses a `Point` as a key, lines 4 to 7: "`Point` doesn't implement `Key`".
Each help offers `with Key` after `Point`'s declaration, which gives it what a key needs, as `with Eq` gives a struct `==`.
A float is never a key: `Map { 0.25: "small" }` is E0451, whose help gives the reason, "`NaN != NaN`, so a float key could never be found again".
Add `with Key` after the `}` on line 1 and run again, or press Solve.
