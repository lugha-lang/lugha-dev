---
title: String concatenation
start_error: E0404
error_note: `+` joins two strings, and `points` is a number, which `+` won't turn into text. Put it inside the string in braces instead.
---

`+` also joins two strings into a new one.
Line 4 tries to build a sentence with it, from `name`, `" has "` and `points`, which is an `i64`.
Press Run.

The program doesn't run.
E0404 says "cannot apply `+` to string and i64", at line 4.
`+` joins only strings, and a number never turns into a string by itself.
Braces in a string do turn it into text, so the number can go inside the string instead.
On line 4, drop `+ points` and change `" has "` to `" has {points}"`, then run again, or press Solve.
