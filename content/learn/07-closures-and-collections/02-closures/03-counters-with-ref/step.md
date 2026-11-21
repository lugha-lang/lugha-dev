---
title: Counters with Ref
start_error: E0511
---

A closure can't assign a variable it copied.
`tick` on line 3 tries to add `1` to `count`.
Press Run.

Line 3 is E0511, "can't change `count`: closures capture by copy", and its help says to return a new value instead.
Returning a new value works when only the closure needs the result.
Here `main` must see the count too, so make it a `Ref`: the closure copies the handle, and the closure and `main` reach the same box, as in Ref.
Make line 2 `let count = Ref.new(0);`, line 3's body `count.set(count.get() + 1);`, and line 6 print `count.get()`, or press Solve.
