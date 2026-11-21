---
title: Iterating a map
start_error: E0442
---

A map can be looped over like an array: each entry is a tuple of key and value, in the order the keys were added.
Line 3 loops with `mut`, meaning to double each price where it is.
Press Run.

`lughac` stops at line 3 with E0442: `for … of mut` can't change a map in place, and the E0501 on line 4 follows from it.
As the help says, loop over `prices.keys()` instead, and assign each `prices[item]`.
Make line 3 `for item of prices.keys() {` and line 4 `prices[item] *= 2;`, or press Solve.
Lines 6 to 8 then read each entry with a plain `for (item, price) of prices`, and line 9 prints `values()`, an array of the values in the same order.
