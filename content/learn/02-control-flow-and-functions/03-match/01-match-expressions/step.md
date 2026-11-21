---
title: match expressions
---

A `match` compares a value with a list of patterns.
Each arm, as on lines 4 to 7, is a pattern, then `=>`, then the value the `match` gives when that pattern matches.
The `_` on line 7 matches anything, so it catches every number the other arms don't.
Press Run.

It prints `Wednesday`.
`day` is `3`, so the arm on line 6 is the first whose pattern matches, and `name` becomes `"Wednesday"`.
Like an `if`, a `match` is an expression, and every arm must give the same type: a number in place of `"Tuesday"` would be E0401, "integer literal where string expected".
Change `3` on line 2 and run again to see the other arms.
