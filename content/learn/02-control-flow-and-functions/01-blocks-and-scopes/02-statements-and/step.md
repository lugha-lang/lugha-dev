---
title: Statements and ()
start_error: E0422
error_note: `console.println` needs a value with a text form, and `()` has none: it's what the block gave back once its last line ended in `;`.
---

Line 5 now ends with a `;`.
Press Run.

A `;` turns an expression into a statement, and a statement throws its value away: `price + tax;` works out `46` and drops it.
The block is left with no last expression, so it gives back `()`, a value that means nothing.

W0106 warns that `total` holds `()`, and its help names the fix: remove the semicolon.
E0422 on line 7 follows from that: `console.println` prints only values that have a text form, and `()` has none.
Its help suggests `.debug()`, but that would only print `()`: the fix is the `;`.

Remove the `;` on line 5 and run again, or press Solve.
