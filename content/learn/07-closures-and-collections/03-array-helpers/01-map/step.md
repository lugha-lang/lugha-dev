---
title: map
---

Arrays have their own `map`, like the one on `Option` in Closures, and it takes a closure too.
It calls the closure on each element and gives back a new array of the results.
Line 3 doubles each price, and line 4 turns each one into a string, so `labels` is a `string[]`.
Line 7 prints `prices` after both.
Press Run.

Neither `map` changed `prices`: line 7 prints it as it was.
