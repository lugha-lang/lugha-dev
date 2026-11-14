---
title: A type's own item
---

`Author` on line 21 is a struct, so the block on line 15 would cover it.
It has its own `describe` on line 24 instead, with exactly the interface's signature, and that one is used.
This is how `eq` and `hash` worked in Equality, ordering and printing.
With any other signature, such as `fun describe(self): i64`, `lughac` gives E0422 at line 33.
Press Run.
