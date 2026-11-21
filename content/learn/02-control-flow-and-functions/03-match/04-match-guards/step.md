---
title: Match guards
start_error: E0417
error_note: A `match` has to cover every value of `temperature`, and guarded arms don't count toward that, so every `i64` but `0` is left without an arm.
---

An arm can have a condition, called a guard, written after the pattern with `if`, as on lines 5 and 6.
There the pattern is a name, `t`, which matches any value and names it for the condition, and the arm matches only when the condition is true.
Press Run.

The program doesn't run: E0417 again, "non-exhaustive match: other values of `i64` are not covered".
Lines 4 to 6 cover every number, but `lughac` doesn't count arms with a guard, so it sees only `0` covered.
The help line asks for `_ => …` as the last arm, which has no guard and covers the rest.
A guard is also how an arm takes a span of numbers, such as 90 to 99, since a pattern can't.
Change line 6 to `_ => "above zero",` and run again, or press Solve.
