---
title: Copies in a function call
---

Line 9 passes `xs` to `add_one` and names what comes back `zs`.
Lines 10 and 11 print both.
Press Run.

Line 10 prints `xs` as it was, since `add_one` changed only its own copy, and line 11 prints `zs`, with the `1` pushed on.
