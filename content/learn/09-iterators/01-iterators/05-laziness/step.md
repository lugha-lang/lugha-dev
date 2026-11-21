---
title: Laziness
---

On an array, `map` runs its closure at once and makes a new array.
Line 2 calls `map` on `[1, 2, 3].iter()` instead, with a closure that prints `doubling` and the number before doubling it.
Line 6 prints `made the iterator`.
Line 7 takes two values from `doubled` with `take(2)` and collects them.
Line 8 starts from a range of numbers up to a billion, keeps the multiples of 7, passes over one with `skip(1)` and takes three with `take(3)`.
Press Run.

`made the iterator` comes first: `map` on an iterator runs nothing yet.
The closure runs only when line 7 pulls values, so `doubling 1` and `doubling 2` come next, then `[2, 4]`.
`take(2)` pulls only two, so `3` is never doubled.
The last line is `[21, 28, 35]`: `skip(1)` passed over 14, the first multiple of 7, and `take(3)` stopped pulling once it had three.
That's why line 8 can start from a range up to a billion.
