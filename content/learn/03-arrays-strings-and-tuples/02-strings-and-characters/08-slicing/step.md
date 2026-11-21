---
title: Slicing
---

`slice(from, to)` gives the part of a string from byte `from` up to, but not including, byte `to`, counted like `.len`.
In `Zoë`, `Z` and `o` are bytes 0 and 1, and `ë` takes bytes 2 and 3.
Line 5 cuts at byte 3, inside `ë`, and prints only the `.len` of what it gets.
Press Run.

Line 3 prints `Zo`, and line 4 prints `ë`.
Line 5 prints `3`: `slice` panics only when the offsets are out of order or past `.len`, so the cut goes through and gives `Z`, `o` and half of `ë`.
Those 3 bytes end inside `ë` and aren't valid UTF-8.
The site can't show output that isn't valid UTF-8, so line 5 prints their length instead of the text.
