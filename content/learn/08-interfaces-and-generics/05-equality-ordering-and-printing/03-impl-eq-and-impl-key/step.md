---
title: impl Eq and impl Key
start_error: E0422
---

A type can decide what equal means for itself by writing `Eq` by hand.
`impl Eq for User` on lines 3 to 5 counts two users as equal when their `id`s are, whatever their names.
Line 10 compares two of them, and line 11 puts both in a set.
Press Run.

The program doesn't run.
A set value must be `Key`, and `User` is only `Eq`.
E0422 says so at the set on line 11: "`User` doesn't implement `Key`".
Its help offers `with Key`, but that would hash every field, `name` too, so two users equal by `id` would hash differently, and equal values must hash the same.
So `Key` is written by hand as well.
Its one method, `hash`, gets `h`, a `Hasher` that works out the hash.
`hash` adds to `h` the same fields `eq` compares: here `h.add(self.id);`.
After line 5, add an `impl Key for User` block with `fun hash(self, mut h: Hasher) { h.add(self.id); }` in it, and run again, or press Solve.
