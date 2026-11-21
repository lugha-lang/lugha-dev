---
title: get returns a copy
---

Line 4 puts a `Point` in a box, line 5 takes it out with `get` into `p`, and line 6 changes `p.x`.
Line 7 prints what's in the box.
Press Run.

It prints `Point { x: 1, y: 2 }`, with `x` still `1`.
`get` gives a copy of what's in the box, so changing `p` never reaches the box.
To change the box, put a value back with `set`.
