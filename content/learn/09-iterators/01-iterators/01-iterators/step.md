---
title: Iterators
---

Besides arrays, `for … of` steps through iterators: an iterator hands out its values one at a time.
Line 2 loops over `range(1, 4)`, an iterator over the same numbers as the range `1..4`.
Line 5 loops over `"hé".chars()`, the string's characters, and line 8 over `"hé".bytes()`, its bytes.
Line 11 makes an iterator over an array's items with `iter()`, and line 12 loops over it.
Press Run.

The first loop prints `1` to `3`.
The second prints the two characters, `h` and `é`.
The third prints three bytes: `104` is the `h`, and `195` and `169` are the `é`, one character but two bytes.
The last loop prints the array's items, `10` and `20`.
