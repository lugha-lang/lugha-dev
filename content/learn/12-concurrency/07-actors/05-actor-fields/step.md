---
title: Actor fields
start_error: E0475
---

`Tally` on line 1 keeps its total in a `Ref` box, declared on line 2.
`add` on line 4 takes plain `self` and changes the number in the box, and line 13 starts the actor with `Ref.new(0)`.
Press Run.

The program doesn't run.
An actor's fields, and its methods' parameters and results, must be `Sendable`, and a `Ref` isn't.
So E0475 points at the field's type on line 2: `Tally` "can't hold or exchange a `Ref<i64>`".
The help's first way is already followed: the state is in an actor, and only the box has to go.
An actor's own methods can change its fields with `mut self`, as `add` did in step 1, so the box isn't needed.
Make line 13's `Ref.new(0)` a plain `0`.
Make line 8 `fun get(self): i64 = self.total;`.
Make line 5 `self.total += n;` and line 4 `fun add(mut self, n: i64) {`.
Make line 2 `total: i64,`.
Or press Solve.
