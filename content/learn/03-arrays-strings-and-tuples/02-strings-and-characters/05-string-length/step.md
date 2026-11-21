---
title: String length
---

A string's `.len` is read without parentheses, like an array's, and line 3 prints it for `Zoë`, a name of three letters.
Line 4 calls `char_count()`, a method, so it has parentheses.
Press Run.

Line 3 prints `4`, because `.len` counts bytes: a string's text is stored as UTF-8, where `Z` and `o` take one byte each and `ë` takes two.
Line 4 prints `3`, because `char_count()` counts characters.
