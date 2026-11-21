---
title: Comments
---

`//` turns the rest of a line into a comment, as on line 2, and `/* … */` can cover several lines.
In Lugha a `/*` comment can hold another one: line 3 opens a comment, and line 4 opens a second inside it.
Press Run.

Only `one` and `five` print.
Block comments nest, so the `*/` on line 4 closes only the inner comment, and the outer one runs on to line 5.
So you can comment out code that already has a comment in it.
