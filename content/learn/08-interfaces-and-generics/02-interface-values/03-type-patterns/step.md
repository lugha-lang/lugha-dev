---
title: Type patterns
start_error: E0417
---

To reach the value inside a `Shape`, `match` on the type it holds.
`c: Circle` on line 18 matches when `s` holds a `Circle`, and names it `c`, a `Circle` with its fields.
`_: Square` on line 19 matches a square without naming it, since its arm doesn't need it.
Press Run.

The program doesn't run.
Any type that implements `Shape` could be inside, even one written later, so the `match` needs a `_` arm even with an arm for each type here.
E0417 says so at the `match` on line 17: "non-exhaustive match: `_` not covered".
Add `_ => "something else",` as a new line after line 19 and run again, or press Solve.
