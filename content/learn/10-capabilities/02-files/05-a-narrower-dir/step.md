---
title: A narrower Dir
---

Line 9 makes the folder `data`, and `here.dir("data")` on line 10 opens it as a `Dir` of its own, confined to that folder.
`save` on line 1 gets only `data`: line 2 writes a file in it, and line 3 writes `../escape.txt`, in its parent.
Lines 14 and 15 check from `here` which files were written.
Press Run.

`Ok(())` is line 9 making `data`.
Then `save` gives the same `Err` as in step 3: `../escape.txt` would land in `here`, but from `data` it climbs out of the folder, so `save` stops at line 3's `?`.
`true` and `false` come from lines 14 and 15: `count.txt` was written, and `escape.txt` never was.
