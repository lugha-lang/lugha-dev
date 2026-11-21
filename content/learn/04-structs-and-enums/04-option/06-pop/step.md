---
title: pop
---

`pop` removes the last element of an array and gives it back in a `Some`, or gives `None` when the array is empty.
Like `push`, `pop` changes the array, so line 2 declares `stack` with `let mut`.
`stack` holds two numbers, and lines 3 to 5 pop three times.
Press Run.

Lines 3 and 4 print `Some(2)` and `Some(1)`, the last element first.
The third `pop` finds the array empty and prints `None`: popping an empty array isn't an error.
Line 6 prints the array, `[]`, empty now.
