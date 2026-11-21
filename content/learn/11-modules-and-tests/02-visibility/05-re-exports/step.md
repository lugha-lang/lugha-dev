---
title: Re-exports
start_error: E0313
---

A module in a folder is named with a dot: `src/geo/square.la` is `geo.square`, and it declares `Square` and `area`.
`shapes.la` imports both on line 1, with no keyword in front of `import`, and `main.la` uses them as `shapes.Square` and `shapes.area`.
Press Run.

E0313 on lines 4 to 6 of `main.la`: the names an import brings in are private to the module that imports them, here `shapes`.
`public` in front of the import, `public import geo.square { Square, area };`, makes the two part of `shapes`, visible to every package, as if `shapes` declared them `public`.
Add `public ` at the start of line 1 of `shapes.la`, or press Solve.
