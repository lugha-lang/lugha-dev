---
title: Exhaustiveness
start_error: E0417
error_note: A `match` needs an arm for every value its subject could hold. `command` could be any string, and only three have arms, so a last arm such as `_` has to catch the rest.
---

This `match` is on a string, `command`, with an arm for each of three commands, and `command` is `"stop"`.
Press Run.

The program doesn't run: E0417 says "non-exhaustive match: other values of `string` are not covered".
A `match` must cover every value `command` could hold, and `command` could be any string, not only the three the arms name.
It doesn't matter that `command` is `"stop"`: `lughac` checks the `match` before the program runs.
An integer has too many values to list as well, so a `match` on a string or an integer needs a last arm that catches the rest.
A `bool` doesn't need one, since `true` and `false` cover it.
Add the arm the help line names, `_ => 0,` as line 7 and run again, or press Solve.
