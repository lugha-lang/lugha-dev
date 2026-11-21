---
title: Generic enums
---

Enums take type parameters in the same place.
`List<T>` on lines 1 to 4 is a recursive enum, a list that can hold any type: a `Cons` holds one element and the rest of the list, and `Nil` ends it.
Line 14 builds a list of strings, and `size` on line 6, generic itself as `swap_pair` was, counts it.
`Option<T>` is declared this way too.
Press Run.

Line 15 prints the list through its debug form, and line 16 its size, `2`.
