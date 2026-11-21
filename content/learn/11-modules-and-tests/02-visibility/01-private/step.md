---
title: private
start_error: E0313
---

`private` in front of an item keeps it inside its own module.
In `shapes.la`, line 7 declares `square` as `private`, and `area` on line 3 uses it there.
Line 6 of `main.la` calls `shapes.square`.
Press Run.

That's E0313, "`square` is private to module `shapes`".
`main.la` is another module, so it can't reach `square`, but it can call `area`, which calls `square` from inside `shapes`.
Change line 6 of `main.la` to print `shapes.area(s)`, or press Solve.
