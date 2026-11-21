---
title: impl Iter
start_error: E0411
---

A type becomes an iterator by implementing `Iter<T>`, where the one method to write is `fun next(mut self): Option<T>`: `Some` with the next value, or `None` when it's done.
The `next` on lines 4 to 10 makes `Countdown` count down from `n`, in a plain `impl Countdown`.
Line 14 loops over a `Countdown`, and line 17 filters one.
Press Run.

E0411 on line 14: "cannot iterate over `Countdown`", and its help says why: it has a method `next`, but a loop needs `impl Iter<T> for Countdown`.
As with operators in Operator overloading, the name alone isn't enough, and without the `impl` there's no `filter` either, E0415 on line 17.
Change `impl Countdown` on line 3 to `impl Iter<i64> for Countdown`, or press Solve.
Then `for … of` calls `next` until it gives `None`, and the helpers from Iterators and Using up an iterator work on it.
A struct literal after `of` keeps its parentheses, as on line 14: without them it's E0205, as in Struct literals in conditions.
