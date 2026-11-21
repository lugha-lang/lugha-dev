---
title: while let
---

`while let` repeats for as long as its pattern matches.
Line 3 pops from `stack` before each pass, and while `pop` gives a `Some`, `top` takes the element inside it.
Once the array is empty, `pop` gives `None` and the loop ends.
Press Run.

The loop prints `3`, `2` and `1`, from the last element to the first.
Line 6 then prints the array, `[]`, empty now.
