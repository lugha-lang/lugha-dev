---
title: push and clear
---

An array can grow and shrink.
`push` on line 3 adds `"bread"` at the end of `list`, and `clear` on line 6 removes every element.
Both change `list`, so line 2 declares it with `let mut`.
Press Run.

Line 4 prints `["milk", "bread"]`: inside a debug form, a string keeps its quotes.
Line 5 prints `2`, the length after the `push`, and line 7 prints `0`, the length after the `clear`.
