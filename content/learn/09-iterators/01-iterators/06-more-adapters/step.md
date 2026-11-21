---
title: More adapters
---

A few more helpers give back an iterator, like `map` and `filter`.
`take_while` on line 3 takes values while its closure holds, and stops at the first that fails, the `9`.
`skip_while` on line 4 skips values while its closure holds.
`flat_map` on line 6 turns each value into an iterator of its own and gives their values in turn, here each word's characters.
`flat_map`'s characters print with their quotes, since a `char` keeps them in a debug form, as a string does.
`bytes()` on line 7, from the first step, gives `u8` numbers.
Press Run.

Once `9` fails, `skip_while` stops checking, so `4` comes through too.
Arrays don't have these, or `take` and `skip`: `xs.take(2)` is E0415, "no method `take` on `i64[]`", so `.iter()` comes first.
