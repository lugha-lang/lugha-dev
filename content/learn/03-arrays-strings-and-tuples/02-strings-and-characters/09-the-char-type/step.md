---
title: The char type
---

A single character has its own type, `char`, and `grade < 'c'` on line 3 compares their Unicode numbers.
Methods such as `is_digit()` and `to_upper()` work on it.
Press Run.

`to_upper()` works only within ASCII and Latin-1, so `'é'` on line 6 becomes `'É'` and the Cyrillic `'ж'` on line 8 comes back unchanged.
`'ß'` on line 7 is in Latin-1 but keeps its case too, because its capital, `ẞ`, is outside Latin-1.
