---
title: pop
---

`pop` removes the last element of an array and returns it as `Some`, or `None` when the array is empty.
Like `push`, `pop` changes the array, so `stack` on line 2 needs `let mut`.
It holds two numbers, and lines 3 to 5 pop three times.
Press Run.

The third `pop` prints `None`: popping an empty array isn't an error, and line 6 goes on to print the array, empty now.
