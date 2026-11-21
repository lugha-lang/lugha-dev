---
title: Struct declaration
---

A struct is a type you declare yourself, made of named fields.
Line 1 declares `Point`, a struct with two fields, `x` and `y`, each with its type.
It's declared at the top level, outside `main`, and it can be used as a type, like `i64`.
Line 4 builds a `Point`, giving each field a value by name, and `p.x` on line 5 reads the field `x`.
Press Run.

Line 5 prints `3`, the value of `p.x`, and line 6 prints `4`, the value of `p.y`.
