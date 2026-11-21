---
title: ReadDir
start_error: E0415
---

`count_lines` on line 1 takes a `ReadDir`, a folder that can only be read, and line 10 passes it `dir.read_only()`.
Line 3 also writes a file through it.
Press Run.

E0415: "no method `write_file` on `ReadDir`", and its help: "a `ReadDir` only reads; take a `Dir` to write".
A `ReadDir` has `read_file`, `list`, `exists` and the other reading methods, and none that writes, makes, renames or removes anything, so `count_lines`'s parameter shows it only reads.
This is caught before the program runs, whereas step 3's paths were an `Err` while it ran.
Remove line 3, or press Solve.
