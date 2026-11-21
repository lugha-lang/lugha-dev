---
title: impl Eq and impl Key
start_error: E0422
---

A type can decide what equal means for itself by writing `Eq` by hand.
`impl Eq for User` on lines 3 to 5 counts two users as equal when their `id`s are, whatever their names.
Line 10 compares two of them, and line 11 puts both in a set.
Press Run.

E0422 on line 11: "`User` doesn't implement `Key`", which a set value needs.
`with Key` would hash every field, `name` too, so two users equal by `id` would hash differently, and equal values must hash the same.
So `Key` is written by hand as well: its `hash` adds to `h`, a `Hasher`, the same fields `eq` compares, here `h.add(self.id);`.
After line 5, add an `impl Key for User` block with `fun hash(self, mut h: Hasher) { h.add(self.id); }` in it, or press Solve.
