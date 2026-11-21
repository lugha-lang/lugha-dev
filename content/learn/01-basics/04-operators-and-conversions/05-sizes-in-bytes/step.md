---
title: Sizes in bytes
---

Whole numbers have methods for sizes in bytes: `kb()` multiplies by 1024, `mb()` by 1024 twice, and `gb()` by 1024 three times.
Line 5 calls `kb()` on `pages`, a `u32`.
Press Run.

Line 2 prints `8192`, eight times 1024.
Line 3 prints `67108864`, 64 times 1024 times 1024.
Line 5 prints `3072`, and it's a `u32`, since the result keeps the type of the number the method is called on.
