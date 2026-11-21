---
title: Laziness
---

On an array, `map` runs its closure at once and makes a new array, as in Array helpers.
Line 2 calls `map` on `[1, 2, 3].iter()` instead, with a closure that prints each number it doubles.
Line 6 prints `made the iterator`, and line 7 takes two values.
Press Run.

No `doubling` line comes before `made the iterator`: `map` on an iterator runs nothing yet.
The closure runs only when line 7 pulls values, and `take(2)` pulls two, so `3` is never doubled.
That's why line 8 can start from a range up to a billion: `skip(1)` passes over the first multiple of 7, and `take(3)` stops pulling once it has three.
