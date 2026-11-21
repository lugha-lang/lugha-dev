---
title: Folders
---

Folders are made and removed through a `Dir` too, and every method that can fail gives a `Result`, so `tidy` on line 1 returns one and uses `?` after each call.
`make_dirs` on line 2 makes `out` and `out/logs` at once, and line 3 writes a file in `out/logs`.
`list` on line 4 gives the names in a folder, and `exists` on line 5 a `bool`.
Lines 6 and 7 remove the file and then the folder, which must be empty, and line 8 lists `out` again.
Press Run.

The first line is the names in `out`, `["logs"]`, in an `Ok`.
`true` says the file was there.
After the two removals, `out` is empty: `Ok([])`.
