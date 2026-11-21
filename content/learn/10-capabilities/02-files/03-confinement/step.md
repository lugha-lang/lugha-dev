---
title: Confinement
---

Line 3 reads `../secret.txt`, which climbs out of `dir`'s folder, and line 4 an absolute path, `/etc/hostname`.
Line 5's `src/../lugha.toml` goes into `src` and back, so it stays inside.
`fs.dir` on line 6 opens another folder, by any path, as a `Dir` of its own, and line 7 writes a file in it.
Press Run.

The first two lines are `Err("path leads outside the folder")`: lines 3 and 4 were refused, without the file being read.
`true` is line 5's read, which worked.
`Ok(2)` is line 7 writing two bytes into `/tmp`, through the `Dir` that `fs.dir` opened: reaching outside a `Dir` takes the `Fs` itself.
