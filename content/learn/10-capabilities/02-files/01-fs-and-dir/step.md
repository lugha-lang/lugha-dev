---
title: Fs and Dir
---

`main` on line 1 takes `fs: Fs`, the capability for files.
`fs.cwd()` on line 2 gives the folder the program runs in, as a `Dir`, a value whose methods work on the files in it.
Line 3 reads `notes.txt` with `read_file`, which gives a `Result<string, string>`: the file's text, or an error message.
Line 4 prints the text with `console.print`, which adds no line break of its own, and line 5 prints the error.
Each run starts without a `notes.txt`.
Line 7 writes the file with `write_file`, replacing anything already in it, and line 8 adds to its end with `append_file`.
Lines 9 to 12 read and print it again.
Press Run.

The first line comes from line 5: line 3 got an `Err`, holding the system's own message for the missing file.
`Ok(5)` twice comes from lines 7 and 8: each gives `Ok` with the number of bytes written, a word and its line break.
Then the file's text, `milk` and `eggs`, from line 10.
