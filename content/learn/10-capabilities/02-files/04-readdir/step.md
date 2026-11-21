---
title: ReadDir
start_error: E0415
error_note: A `ReadDir` has only reading methods, so it has no `write_file`, and line 3 tries to write through one.
---

`count_lines` on line 1 takes a `ReadDir`, a folder that can only be read, and line 10 passes it `dir.read_only()`.
A `ReadDir` has `read_file`, `list`, `exists` and the other reading methods, and none that writes, makes, renames or removes anything.
Line 3 writes a file through it.
Press Run.

The program doesn't run: this is caught before it starts, while step 3's paths were an `Err` as it ran.
E0415 on line 3 says there's "no method `write_file` on `ReadDir`", and its help says "a `ReadDir` only reads; take a `Dir` to write".
So a `ReadDir` parameter shows that `count_lines` only reads.
Remove line 3 and run again, or press Solve.
