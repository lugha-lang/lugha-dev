---
title: Semicolons
start_error: E0201
---

Now there are two `console.println` lines, and line 2 has no semicolon.
Press Run.

`lughac` gives E0201: it expected a `;` where line 3 begins.
Lugha reads a line break the same as a space, so a statement ends at its `;`, not at the end of a line.

Add the `;` on line 2 and run again, or press Solve.
It's also why two statements can share one line, as long as each has its `;`.
