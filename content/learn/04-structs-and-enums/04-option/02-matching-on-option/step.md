---
title: Matching on Option
start_error: E0417
---

`Option` is an enum, so a `match` gets at the value inside, as it did for `Shape`.
Line 13 matches on what `find` gives back for each name, and `.Some(i)` on line 14 names the position `i`.
Press Run.

The program doesn't run.
A `match` has to cover every variant, and nothing here says what happens when a name isn't found.
E0417 says "non-exhaustive match: `.None` not covered", at line 13.
The missing arm is `.None`: `None` is built without a dot, but every variant in a pattern has its dot, `Some` and `None` included.
Add `.None => console.println("{wanted} isn't there"),` as a new line after line 14 and run again, or press Solve.
