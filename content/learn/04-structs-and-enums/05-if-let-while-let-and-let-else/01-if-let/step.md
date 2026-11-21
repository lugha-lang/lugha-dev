---
title: if let
---

A `match` with only one case worth handling can be written as an `if let`.
Line 3 tests one pattern, `.Some(n)`, against what `parse_i64` gives back for `typed`.
When it matches, the block on line 4 runs with `n` in scope, and otherwise the `else` block on lines 5 to 7 runs.
There's no `.None` arm to write, because an `if let` doesn't have to cover every case.
The `else` is optional, and without it nothing runs when the pattern doesn't match.
Press Run.

For `"12"` the pattern matches, and line 4 prints `12 doubled is 24`.
For `"twelve"`, `parse_i64` gives `None`, so line 6 prints `twelve isn't a number`.
