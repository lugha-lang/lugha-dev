---
title: Actor fields
start_error: E0475
---

`Tally` on line 1 keeps its total in a `Ref` box, as Counters with Ref did for a closure.
Press Run.

E0475 on line 2: an actor's fields, and its methods' parameters and results, must be `Sendable`, and a `Ref` isn't.
An actor's own methods can change its fields with `mut self`, as `add` did in step 1, so the box isn't needed.
Make line 13's `Ref.new(0)` a plain `0`.
Make line 8 `fun get(self): i64 = self.total;`.
Make line 5 `self.total += n;` and line 4 `fun add(mut self, n: i64) {`.
Make line 2 `total: i64,`.
Or press Solve.
