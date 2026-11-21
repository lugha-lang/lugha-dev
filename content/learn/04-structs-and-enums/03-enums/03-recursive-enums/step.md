---
title: Recursive enums
---

A variant's data can be the enum itself.
`List` on lines 1 to 4 is either `Nil`, the end, or `Cons`, a number followed by the rest of the list.
`Cons` on line 3 has `List` as its second type, written the same way as `i64`.
Line 14 builds `1`, `2`, `3` by nesting: the innermost value is `List.Nil`, and each `Cons` puts one number in front of it.
`sum` on lines 6 to 11 adds each number to the sum of the rest, calling itself until it reaches `.Nil`, which gives 0.
Press Run.
