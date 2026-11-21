---
title: derive.all and derive.fold
---

`Gauge` on line 1 has two items, and the struct block on line 15 writes both.
Line 7 writes `i64` where the interface says `Self`, since the block is for `i64`; line 16, in the struct block, keeps `Self`.
`derive.all(self, other, near)` on line 16 calls `near` on each pair of matching fields and is `true` when every call is, stopping at the first `false`.
`near` gets the field's name and the two values; there is no `ctx`.
`derive.fold(self, 0, add_up)` on line 17 starts from `0` and passes the running result through `add_up` once per field, as `sum`.
`Reading` on line 20 asks with `with Gauge`.
Press Run.
