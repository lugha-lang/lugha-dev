---
title: map
---

Arrays have a `map` too, and it takes a closure, as `Option`'s does.
It calls the closure on each element and gives back a new array of the results.
Line 3 doubles each price, and line 4 turns each one into a string, so `labels` is a `string[]`.
Line 7 prints `prices` after both.
Press Run.

Lines 5 and 6 print the two new arrays.
Neither `map` changed `prices`: line 7 prints it as it was.
