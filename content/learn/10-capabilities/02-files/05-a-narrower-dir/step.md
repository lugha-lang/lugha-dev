---
title: A narrower Dir
---

Line 9 makes the folder `data`, and `here.dir("data")` on line 10 opens it as a `Dir` of its own, confined to that folder in turn.
`save` on line 1 gets only `data`, and line 2 writes in it, line 3 into its parent.
Lines 14 and 15 check from `here` which files were written.
Press Run.

Line 3's `../escape.txt` would land in `here`, but from `data` it climbs out of the folder, so it's the same `Err` as in step 3: `save` stops there, and `escape.txt` was never written.
