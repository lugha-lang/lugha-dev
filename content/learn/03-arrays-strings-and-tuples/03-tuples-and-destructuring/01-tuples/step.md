---
title: Tuples
---

A tuple groups a fixed number of values, and each can have its own type.
Line 2 makes one from a string and a number, in parentheses.
Like an array, a tuple has no text form of its own, so line 3 prints it through `.debug()`, and `console.println(item)` alone would be E0422.
Lines 4 and 5 read its elements by position, with `.0` and `.1`.
Press Run.

Line 3 prints `("milk", 2)`: in the debug form, the string keeps its quotes.
Line 4 prints `milk` without them, since `item.0` is the string itself.
Line 5 prints `2`.
