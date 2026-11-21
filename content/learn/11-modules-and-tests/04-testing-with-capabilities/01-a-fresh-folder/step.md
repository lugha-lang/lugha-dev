---
title: A fresh folder
---

A test can take capabilities as parameters too, matched by type: `Console`, `Dir`, `Clock`, `Env`, `Entropy` and `Net`.
It can't take `Fs`: it takes `dir: Dir` instead, a folder made for that test alone.
`counts_lines_in_a_fresh_folder`, on line 11, takes one, and line 12 checks that it's empty.
Line 13 writes a file there, and lines 14 and 15 check `count_lines` on it and on a file that isn't there.
Press Test.

The Tests tab shows the test `ok`: its folder held nothing until line 13, and the program's own files aren't in it.
Tests in `src` are named by package and module, and tests in `test/` by their path.
With no `lugha.toml` of its own, a program on this site is the package `playground`, so this test's name starts `playground.main.`.
