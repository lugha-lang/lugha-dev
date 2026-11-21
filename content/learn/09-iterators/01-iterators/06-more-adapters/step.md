---
title: More adapters
---

A few more helpers give back an iterator, like `map` and `filter`.
Arrays don't have `take_while`, `skip_while` or `flat_map`, or `take` and `skip` (`xs.take(2)` is E0415, "no method `take` on `i64[]`"), so lines 3, 4 and 6 call `.iter()` first.
On line 3, `take_while` takes values while its closure holds, and stops at the first that fails.
On line 4, `skip_while` skips values while its closure holds.
On line 6, `flat_map` turns each word into an iterator over its characters, and gives their values in turn.
Line 7 collects `"hi".bytes()`, the bytes of a string.
Press Run.

The first line is `[3, 5]`: `take_while` stops at the `9`.
The second is `[9, 4, 8]`: once `9` fails, `skip_while` stops checking, so `4` comes through too.
The third is each word's characters, with their quotes: a `char` keeps them in its debug form, as a string does.
The last is the bytes of `hi`, as `u8` numbers.
