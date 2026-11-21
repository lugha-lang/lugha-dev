---
title: let else
start_error: E0429
---

`let … else` keeps its bindings in scope for the rest of the block, where `if let`'s `n` exists only inside its own block.
Its `else` runs when the pattern doesn't match, and the whole `let … else` ends with `;` on line 4.
Line 2 names the number `n`, and the `console.println` on line 5 uses it.
Press Run.

E0429: "the `else` of a `let … else` must not finish".
If the `else` block ended normally, line 5 would run with no `n` to read.
So the block has to leave, here with `return;`, which ends `report` without a value.
Add `return;` as a new line after line 3, or press Solve.
