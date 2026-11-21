---
title: Import aliases
start_error: E0305
---

The name an import binds can be changed: `import shapes as geo;` on line 1 binds the module as `geo`, and lets two modules with the same last name be told apart in one file.
Line 4 still writes `shapes.Square`.
Press Run.

That's E0305: with `as geo`, only `geo` is bound in this file, and `shapes` isn't.
Change `shapes.Square` to `geo.Square` on line 4, or press Solve.
