---
title: Iterators
---

Besides arrays, `for … of` steps through iterators, which hand out their values one at a time.
`range(1, 4)` on line 2 is an iterator over the same numbers as the range `1..4` in Loops, `1` to `3`.
`chars()` on line 5 gives a string's characters, and `bytes()` on line 8 its bytes, as a plain `for … of` over a string does in Bytes.
`iter()` on line 11 makes an iterator over an array's items.
Press Run.

`é` is one character but two bytes, `195` and `169`.
