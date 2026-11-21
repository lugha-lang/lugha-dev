---
title: Bytes
---

Indexing a string counts in bytes too, like `.len`.
Line 3 prints `word[0]`, the first byte of `"hi"`.
Press Run.

It prints `104`, the byte for `h`, because `word[0]` is a `u8`.
A `for … of` loop over a string, as on line 4, goes through its bytes the same way.
