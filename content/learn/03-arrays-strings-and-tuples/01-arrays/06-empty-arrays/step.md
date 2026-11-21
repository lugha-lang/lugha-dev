---
title: Empty arrays
start_error: E0412
error_note: `[]` has no elements to take a type from, and `lughac` won't work one out from the lines after it, so the array's type has to be written.
---

Line 2 now starts `list` empty, with `[]`, and line 3 pushes a string into it.
Press Run.

The program doesn't run.
`[]` has no elements, so it says nothing about what the array will hold, and `lughac` works out a type only from what's written there, not from line 3.
E0412 says it "cannot infer the element type of `[]`" on line 2.
Its help shows the way out for an array of `i64`: write the type after a colon, as in `let xs: i64[] = [];`.
This list holds strings, so its type is `string[]`.
Add `: string[]` after `list` on line 2 and run again, or press Solve.
