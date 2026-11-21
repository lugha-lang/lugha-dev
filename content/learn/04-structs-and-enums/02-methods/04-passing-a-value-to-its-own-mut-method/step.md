---
title: Passing a value to its own mut method
start_error: E0508
error_note: `p.add(p)` gives `add` the same `p` it changes as `self`, and that isn't allowed. A copy made with `let` can be passed instead.
---

`add` on line 4 is a `mut self` method that adds another point, `other`, to `self`.
Line 12 tries to add `p` to itself, with `p.add(p)`.
Press Run.

The program doesn't run.
E0508 says "cannot pass `p` to a `mut self` method called on `p`", at line 12.
The help says to copy it first: `let w = p;` makes a separate copy of `p`, and `w` can be passed instead.
Change line 12 to `p.add(w);`, then add `let w = p;` on a new line before it, and run again.
Or press Solve.
