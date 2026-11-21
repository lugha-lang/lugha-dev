---
title: A fresh folder
---

A test can take capabilities as parameters too, matched by type: `Console`, `Dir`, `Clock`, `Env`, `Entropy` and `Net`, but not `Fs`, which a test takes as `dir: Dir` instead.
`counts_lines_in_a_fresh_folder` on line 11 takes one, a folder made for it alone, which line 12 checks is empty.
Line 13 writes a file there, and lines 14 and 15 check `count_lines` on it and on a file that isn't there.
Press Test.

The test passes: its folder held nothing until line 13, and the program's own files aren't in it.
With no `lugha.toml` of its own, a program on this site is the package `playground`, so its tests' names start `playground.main.`.
Tests in `test/` are named by their path instead, as in Tests.
