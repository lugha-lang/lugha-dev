---
title: derive.build
---

An interface item can take no `self`, as `parse` on line 2 does.
It is called on a type, as `T.parse(s)` on line 26.
`derive.build(s.split(","), field)` on line 21 builds a struct one field at a time.
For each field it calls the function `field` on line 13.
`field` gets the split parts as `ctx`, then the field's name, its position from 0, and the number of fields.
Line 17 parses one part with `F`'s own `parse`, so each field is read at its own type.
The first `Err` stops it and is the result; otherwise it is `Ok` with the struct.
Press Run.
