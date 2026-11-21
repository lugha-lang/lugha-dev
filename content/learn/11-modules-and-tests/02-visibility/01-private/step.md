---
title: private
start_error: E0313
error_note: `square` is marked `private` in `shapes.la`, so only code in that file can call it, and `main.la` is a different module.
---

`private` in front of an item keeps it inside its own module.
In `src/shapes.la`, line 7 declares `square` as `private`, and `area` on line 3 calls it from inside the module.
Line 6 of `src/main.la` calls `shapes.square` directly.
Press Run.

The program doesn't run.
`main.la` is another module, so it can't reach `square`: E0313 says "`square` is private to module `shapes`", at line 6 of `src/main.la`.
Its help says only `shapes` can use it, and that removing `private` would share it.
There's no need here: `main.la` can call `area`, which calls `square` from inside `shapes`.
Change line 6 of `src/main.la` to print `shapes.area(s)` and run again, or press Solve.
