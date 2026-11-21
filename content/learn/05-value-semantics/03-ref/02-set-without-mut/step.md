---
title: set without mut
---

In the last step, `b.set(5)` worked on a plain `let b`, though `push` on an array needs `let mut`.
`set` changes the box, and `b` still names the same box.
`let mut` is needed only to point a name at another box.
`count` on line 2 is a plain `let` too, and line 3 calls `set(3)` on it.
Press Run.
