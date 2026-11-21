---
title: Comments
---

`//` turns the rest of a line into a comment, as on line 2.
`/* … */` covers everything between its marks, even across lines, and these comments nest: line 3 opens one, and line 4 opens a second inside it.
Press Run.

Only `one` and `five` print.
The `*/` on line 4 closes the inner comment, so the outer one runs on to the `*/` on line 5, and lines 3 to 5 are all comment.
That's what lets you comment out code that already has a comment in it.
