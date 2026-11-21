---
title: Private fields
start_error: E0313
---

A field can be `private` too, and then only its own module can set or read it.
`Range.new` in `range.la` puts the smaller number in `lo`: it swaps `a` and `b` when `a` is larger.
Line 4 of `main.la` builds a `Range` with a literal instead, with `lo` above `hi`.
Press Run.

It's E0313 again, this time for a field: "`hi` is private to module `range`".
Outside its module, a struct literal needs every field visible, so a `Range` has to be built with `new`, as the help says.
Change line 4 to `let r = range.Range.new(5, 1);`, or press Solve.
