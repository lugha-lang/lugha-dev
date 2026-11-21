---
title: Re-exports
start_error: E0313
error_note: `shapes.la` imports `Square` and `area` on line 1, but an import's names stay private to the module that imports them, so `main.la` can't reach them through `shapes`.
---

A module in a folder is named with a dot: `src/geo/square.la` is the module `geo.square`, and it declares `Square` and `area`, both `public`.
Line 1 of `src/shapes.la` imports both, with no keyword in front of `import`.
`src/main.la` imports only `shapes`, and uses the two as `shapes.Square` on line 4 and `shapes.area` on lines 5 and 6.
Press Run.

The program doesn't run.
The names an import brings in are private to the module that imports them, here `shapes`, so each use in `main.la` is an E0313, on lines 4, 5 and 6.
Each help names the fix: `public import` in `shapes.la` passes the names on.
`public` in front of the import makes the two part of `shapes`, visible to every package, as if `shapes` declared them `public`.
Add `public ` at the start of line 1 of `shapes.la` and run again, or press Solve.
