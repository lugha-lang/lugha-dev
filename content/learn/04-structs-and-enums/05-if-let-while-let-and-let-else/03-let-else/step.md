---
title: let else
start_error: E0429
error_note: When `typed` isn't a number, the `else` block runs and there's no `n`, so the block must not go on to line 5. End it with `return;` so `report` stops there.
---

`let … else` is a `let` with a pattern: line 2 names the number inside `.Some(n)`, and when the pattern doesn't match, its `else` block runs.
Unlike `if let`'s `n`, which exists only inside its own block, this `n` stays in scope for the rest of the block, and line 5 uses it.
The whole `let … else` ends with the `;` on line 4.
Press Run.

The program doesn't run.
E0429 says "the `else` of a `let … else` must not finish", at line 2.
When the `else` block runs there's no `n`, so if the block ended normally, line 5 would run with no `n` to read.
The block has to leave instead, and the help lists ways to; here `return;` does it, ending `report` without a value.
Add `return;` as a new line after line 3 and run again, or press Solve.
