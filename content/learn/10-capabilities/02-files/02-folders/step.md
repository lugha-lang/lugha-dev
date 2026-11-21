---
title: Folders
---

Folders are made and removed through a `Dir` too, and every method that can fail gives a `Result`, so `tidy` on line 1 uses `?` from The ? operator.
`make_dirs` on line 2 makes `out` and `out/logs` at once, and line 3 writes a file in it.
`list` on line 4 gives the names in a folder, `exists` on line 5 a `bool`.
Lines 6 and 7 remove the file and then the folder, which must be empty, and line 8 lists `out` again.
Press Run.
