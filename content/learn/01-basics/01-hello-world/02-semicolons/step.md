---
title: Semicolons
start_error: E0201
error_note: Every statement ends with a `;`, and a line break doesn't end one. Line 2 has no `;`, so the statement runs on into line 3, and `console` is where the `;` should have been.
---

Now there are two `console.println` lines, and line 2 has no `;` at its end.
Press Run.

This time the program doesn't run.
Lugha reads a line break the same as a space, so a statement ends at its `;`, not at the end of a line.
Without the `;`, line 2 runs on into line 3.
E0201 says so: it expected a `;` and found `console`, the first word of line 3.
`src/main.la:3:5` under it says where: the file, line 3, column 5.
Add the `;` at the end of line 2 and run again, or press Solve.
