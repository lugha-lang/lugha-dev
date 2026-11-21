---
title: import
start_error: E0305
---

`main.la` has lost its `import`, though `shapes.la` is still there.
Press Run.

`lughac` stops with E0305 for the type on line 2, "cannot find type `shapes.Square`", and E0301 for the names on lines 3 and 4.
Having `shapes.la` in the project isn't enough: `main.la` needs the `import`, and that binds the name `shapes`.
Every item from the module is then written with `shapes.` in front, as `main` already does.
Add `import shapes;` as a new line 1, with an empty line after it, or press Solve.
