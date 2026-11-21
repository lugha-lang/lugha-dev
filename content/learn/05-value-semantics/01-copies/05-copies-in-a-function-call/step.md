---
title: Copies in a function call
---

This is `add_one` again, and line 9 now keeps what it returns, as `zs`.
Line 10 prints `xs` and line 11 prints `zs`.
Press Run.

Line 10 prints `[5, 6]`, since `add_one` changed only its own copy, and line 11 prints `[5, 6, 1]`, the array it returned.
