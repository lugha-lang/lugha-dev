---
title: Sets
---

A set holds distinct values, written `Set { a, b }`, without colons, and keeps them in the order they were added.
`has` on line 3 asks whether a value is in it, and `insert` on lines 4 and 5 returns `true` only when the value is new.
`remove` on line 6 returns `true` when there was something to remove.
Maps have `remove` too, giving back the removed value as an `Option` on line 9, and both have `clear`, which empties them, as line 10 does for `ages`.
Press Run.
