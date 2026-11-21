---
title: Iterating a map
start_error: E0442
---

A map can be looped over like an array: each entry is a tuple of key and value, in the order the keys were added.
Line 3 loops with `of mut`, and line 4 means to double each price where it is.
Lines 6 to 8 print each entry, and line 9 prints `values()`, the map's values in the same order.
Press Run.

The program doesn't run.
A map isn't changed through its loop: the loop visits a copy of its entries.
E0442 says so on line 3: "`for … of mut` can't change a `Map<string, i64>` in place".
Its help says what to do: loop over the keys, with `keys()`, and assign through each one.
The E0501 on line 4, "cannot assign to `price`", follows from the first error: its help about match bindings can be ignored, since the error goes once line 3 is fixed.
Make line 3 `for item of prices.keys() {` and line 4 `prices[item] *= 2;`, then run again, or press Solve.
