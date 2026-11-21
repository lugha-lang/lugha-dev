---
title: Multiple files
---

A program can be split across several files, and each file is a module.
`src/shapes.la`, in the file list, is the module `shapes`: a module's name is the file's path from the folder `main.la` is in, without `.la`.
It declares the struct `Square` on line 1 and two functions on lines 3 and 5.
Line 1 of `src/main.la`, `import shapes;`, loads that module and binds the name `shapes`, and lines 4 to 6 reach its items through that name, with `shapes.` in front.
Nothing in `shapes.la` needs marking for this: an item with no marking can be used by every file of the same program.
Press Run.

The output panel shows `a square of side 3.0`, from `shapes.describe` on line 5, then `9.0`, the area from `shapes.area` on line 6.
