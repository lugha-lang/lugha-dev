---
title: Copy-on-write
---

Copying an array takes the same time however long it is, because at first the copy shares the original's memory.
Line 3 copies `big`, a million numbers, that way.
Line 4 writes to `copy`, so line 4 is where `copy` gets a million numbers of its own.
This is called copy-on-write, and no program can tell it from a full copy.
Press Run.

Line 5 still prints `0`.
