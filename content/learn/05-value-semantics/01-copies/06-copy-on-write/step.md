---
title: Copy-on-write
---

Line 2 makes `big`, an array of a million zeros, and line 3 copies it into `copy`.
That copy takes the same time however long the array is, because at first `copy` shares `big`'s memory.
Line 4 writes to `copy`, and that's where `copy` gets a million numbers of its own.
This is called copy-on-write, and no program can tell it from a full copy.
Press Run.

Line 5 prints `big[0]`, still `0`, and line 6 prints `copy[0]`, now `1`.
