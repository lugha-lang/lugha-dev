---
title: Bytes
---

Indexing a string counts in bytes too, like `.len`.
Line 3 prints `word[0]`, the first byte of `"hi"`, and the loop on lines 4 to 6 goes through `word` with `for … of`.
Press Run.

Line 3 prints `104`, not `h`: `word[0]` is a `u8`, a byte, and `104` is the byte that stands for `h`.
The loop gives the bytes in turn, so it prints `104` for `h` and `105` for `i`.
