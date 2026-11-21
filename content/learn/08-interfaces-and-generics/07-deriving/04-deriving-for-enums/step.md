---
title: Deriving for enums
---

`derive Describe for enum` on line 15 covers every enum that asks, as `Shape` does on line 22.
`derive.variant(self, (), part)` on line 17 gives a tuple: the variant's name, and an array of what `part` returns for each payload.
Each payload has no name of its own, so `part` gets the variant's name, unused here.
`Dot` has no payloads, so its array is empty.
`derive.index(self)` on line 18 is the variant's position in the enum, counting from 0.
Press Run.
