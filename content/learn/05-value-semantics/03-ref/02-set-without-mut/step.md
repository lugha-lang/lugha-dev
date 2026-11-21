---
title: set without mut
---

`count` on line 2 is a box declared with a plain `let`, and line 3 calls `set(3)` on it.
An array's `push` needs `let mut`, but `set` doesn't: it changes what's in the box, and `count` still names the same box.
Press Run.

Line 4 prints `3`.
`let mut` is needed only to point a name at another box.
