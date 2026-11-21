---
title: Slicing
---

`slice(from, to)` gives the part of a string between two offsets, counted in bytes like `.len`.
In `Zoë`, `Z` and `o` are bytes 0 and 1, and `ë` takes bytes 2 and 3, so line 4's `slice(2, 4)` gives `ë`.
Press Run.

Line 5 cuts at offset 3, inside `ë`.
`slice` panics only when the offsets are out of order or past `.len`, so that cut goes through: 3 bytes, `Z`, `o` and half of `ë`.
Line 5 prints only its `.len`, because those 3 bytes end inside `ë` and aren't valid UTF-8.
