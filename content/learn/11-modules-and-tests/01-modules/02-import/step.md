---
title: import
start_error: E0305
error_note: `shapes.Square` names a type in the module `shapes`, but this file has no `import shapes;`, so the name `shapes` means nothing here.
---

`src/main.la` is the same as before without its `import` line, and `src/shapes.la` hasn't changed.
Press Run.

This time the program doesn't run.
Having `shapes.la` in the project isn't enough: without the `import`, nothing in `main.la` binds the name `shapes`.
E0305 comes first: it can't find the type `shapes.Square` on line 2.
The two E0301 errors say the same about `shapes` in the calls on lines 3 and 4: nothing in scope is called `shapes`.
Add `import shapes;` as a new line 1 of `src/main.la`, with an empty line after it, and run again, or press Solve.
