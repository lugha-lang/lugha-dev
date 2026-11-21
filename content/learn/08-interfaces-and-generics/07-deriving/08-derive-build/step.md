---
title: derive.build
---

An interface item can take no `self`, as `parse` on line 2 does, and it's called on a type, as `T.parse(s)` on line 26.
`derive.build(s.split(","), field)` on line 21 builds a struct one field at a time, calling `field` on line 13 once per field with `F` set to that field's type: `string` for `title` and `i64` for `pages`.
`field` gets the split parts as `ctx`, then the field's name, its position from 0, and the number of fields.
Line 17 parses one part with `F`'s own `parse`, so each field is read at its own type.
The first `Err` stops it and is the result; otherwise it's `Ok` with the struct.
Press Run.

`"Dune,412"` parses into a `Book`.
`"Dune,many"` stops at `pages`, with the `i64` block's `Err`.
`"Dune"` splits into one part, so `field` gives back its own `Err`.
