---
title: Import aliases
start_error: E0305
error_note: With `import shapes as geo;`, this file knows the module only as `geo`, so `shapes.Square` names nothing here.
---

The name an import binds can be changed with `as`: line 1 of `src/main.la`, `import shapes as geo;`, binds the module as `geo`.
That's how one file can use two modules that would otherwise bind the same name.
Line 5 calls `geo.area`, but line 4 still writes `shapes.Square`.
Press Run.

The program doesn't run.
With `as geo`, only `geo` is bound in this file, and `shapes` isn't, so E0305 can't find the type `shapes.Square` on line 4.
Change `shapes.Square` to `geo.Square` on line 4 and run again, or press Solve.
