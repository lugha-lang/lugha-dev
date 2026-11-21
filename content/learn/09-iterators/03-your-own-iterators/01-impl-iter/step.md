---
title: impl Iter
start_error: E0411
error_note: A loop needs a type that implements `Iter<T>`. `Countdown` has a `next` of its own but no `impl Iter<i64> for Countdown`, so line 14 can't loop over it.
---

A type becomes an iterator by implementing the interface `Iter<T>`, whose one method is `fun next(mut self): Option<T>`, giving `Some` with the next value or `None` at the end.
A `for … of` calls `next` until it gets `None`.
Here `Countdown`'s `next`, on lines 4 to 10, is in a plain `impl Countdown`.
Line 14 loops over a `Countdown` (a struct literal after `of` needs its parentheses), and line 17 filters one.
Press Run.

The program doesn't run: a method named `next` isn't enough.
E0411 on line 14 says it "cannot iterate over `Countdown`", and its help names what a loop needs: `impl Iter<T> for Countdown`.
Without that `impl`, `Countdown` has no `filter` either: E0415 on line 17.
E0412 follows from it: with no `filter`, nothing says what type the closure's `n` is.
Change `impl Countdown` on line 3 to `impl Iter<i64> for Countdown` and run again, or press Solve.
