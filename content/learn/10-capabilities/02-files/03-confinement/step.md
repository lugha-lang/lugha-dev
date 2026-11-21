---
title: Confinement
---

Line 3 reads `../secret.txt`, which climbs out of `dir`'s folder, and line 4 an absolute path, `/etc/hostname`.
Line 5's `src/../lugha.toml` goes into `src` and back, and stays inside.
`fs.dir` on line 6 opens another folder, by any path, as a `Dir` of its own.
Press Run.

Lines 3 and 4 are `Err("path leads outside the folder")`, without the file being read.
Line 7 writes into `/tmp` through the `Dir` that `fs.dir` opened: reaching outside a `Dir` takes the `Fs` itself.
