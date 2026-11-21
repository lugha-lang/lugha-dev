---
title: zip
---

`zip` walks two iterators side by side and gives a tuple for each pair of values.
Line 4 zips `names` with `ages`, and the loop takes each tuple apart into `name` and `age`.
`names` has three names, but `ages` has only two numbers.
Press Run.

Two lines print, one for `Ann` and one for `Ben`.
`Cy` isn't printed: `zip` stops at the end of the shorter one.
