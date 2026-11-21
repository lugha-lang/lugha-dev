---
title: Fs and Dir
---

`main` takes `fs: Fs` for files, and `fs.cwd()` on line 2 gives the folder the program runs in, as a `Dir`.
Line 3 reads `notes.txt` from it with `read_file`, which gives a `Result<string, string>`.
Each run starts without a `notes.txt`.
`write_file` on line 7 writes a file, replacing anything already in it, and `append_file` on line 8 adds to the end.
Each gives `Ok` with the number of bytes written.
Line 9 reads the file again.
Press Run.

The first `Err` holds the system's own message for the missing file.
