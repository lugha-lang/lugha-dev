---
title: Match guards
start_error: E0417
---

An arm can have a condition, written after the pattern with `if`, as on lines 5 and 6.
There the pattern is a name, `t`, which matches any value and gives it the name `t` to use in the condition.
The arm matches only when the condition is true.
Press Run.

It gives E0417 again.
When `lughac` checks that every value is covered, it counts only the arms without a condition.
So the last case has to be an arm without one: change line 6 to `_ => "above zero",` and run again, or press Solve.
A range such as `90..100` isn't a pattern, so a guard is how an arm takes a range of numbers.
