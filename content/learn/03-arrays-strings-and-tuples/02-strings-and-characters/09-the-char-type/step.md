---
title: The char type
---

A single character has its own type, `char`, written in single quotes, as `'b'` on line 2.
`grade < 'c'` on line 3 compares two characters by their Unicode numbers.
Lines 4 to 8 call two of `char`'s methods, `is_digit()` and `to_upper()`.
Press Run.

Line 3 prints `true`, since `b` comes before `c`, and line 4 prints `true`, since `'7'` is a digit.
Line 5 prints `B`.
`to_upper()` works only within ASCII and Latin-1, so line 6 turns `'é'` into `É`.
Line 7's `'ß'` is in Latin-1 but stays `ß`, because its capital, `ẞ`, is outside Latin-1.
Line 8's Cyrillic `'ж'` is outside both, so it comes back unchanged.
