---
title: Empty arrays
start_error: E0412
---

Now the list starts empty, and line 3 pushes a string into it.
Press Run.

E0412 says `lughac` "cannot infer the element type of `[]`".
`[]` has no elements to take a type from, and `lughac` doesn't look ahead to line 3 for one.
Write the type after a colon: add `: string[]` after `list` on line 2, or press Solve.
