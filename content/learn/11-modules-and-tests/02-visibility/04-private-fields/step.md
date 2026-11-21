---
title: Private fields
start_error: E0313
---

A field can be `private` too, and then only its own module can set or read it.
In `src/range.la`, line 1 makes both of `Range`'s fields `private`.
`Range.new`, on lines 4 and 5, puts the smaller number in `lo`: it swaps `a` and `b` when `a` is larger.
Line 4 of `src/main.la` builds a `Range` with a literal instead, with `lo` above `hi`.
Press Run.

The program doesn't run.
It's E0313 again, this time for a field: "`hi` is private to module `range`", at line 4 of `src/main.la`.
Outside its module, a struct literal needs every field it sets to be visible, and the error names `hi`, one of the two private fields this literal sets.
The help says to build the `Range` with one of `Range`'s functions, which here means `new`.
Change line 4 of `src/main.la` to `let r = range.Range.new(5, 1);` and run again, or press Solve.
