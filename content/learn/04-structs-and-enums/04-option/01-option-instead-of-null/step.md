---
title: Option instead of null
---

A value that may be missing has the type `Option`: either `Some` with the value inside, or `None`.
There's no null in Lugha, so an `Option` is how a missing value is written.
`find` on line 1 gives back a name's position, and there is none when the name isn't in the array, so its return type is `Option<i64>`.
Line 4 returns `Some(i)` when the name is found, and line 7 gives `None` once the loop ends without it.
Unlike `Shape`'s variants, `Some` and `None` can be written without the enum's name in front.
Press Run.

An `Option` prints through `.debug()`, as `Shape` did.
