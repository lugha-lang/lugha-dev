---
title: Sets
---

A set holds distinct values, written `Set { a, b }`, without colons, and keeps them in the order they were added.
`has` on line 3 asks whether a value is in it, and `insert` on lines 4 and 5 returns `true` only when the value is new.
`remove` on line 6 returns `true` when there was something to remove.
Maps have `remove` too, giving back the removed value as an `Option` on line 9, and both have `clear`, which empties them, as line 10 does for `ages`.
Press Run.

Line 3 prints `true` for `"red"`.
Line 4 prints `true`, since `"green"` is new, and line 5 `false`, since `"red"` was already there.
Line 6 prints `true` for removing `"blue"`, and line 7 shows what's left, in the order it was added.
Line 9 prints `Some(40)`, the value `"bo"` had, and line 11 the emptied map.
