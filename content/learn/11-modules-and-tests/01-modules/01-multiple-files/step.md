---
title: Multiple files
---

A program can be split across several files, and each file is a module named by its path from `main.la`'s folder, without `.la`.
`src/shapes.la`, in the file list, is the module `shapes`: it declares `Square` and two functions.
Line 1 of `main.la`, `import shapes;`, loads it, and the rest of `main` uses what `shapes.la` declares.
Nothing in `shapes.la` needs marking for this: an item with no marking can be used by every file of the same program, as Visibility shows.
Press Run.

The standard library's modules are imported the same way, with `std.` in front, and an import binds the last part of the name: `import std.random;` in Clock, Env and Entropy bound `random`.
