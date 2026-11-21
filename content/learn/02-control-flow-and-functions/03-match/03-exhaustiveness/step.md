---
title: Exhaustiveness
start_error: E0417
---

This `match` is on a string, with an arm for each of the three commands, and `command` is `"stop"`.
Press Run.

`lughac` refuses it with E0417, "non-exhaustive match: other values of `string` are not covered".
A `match` must cover every value `command` could hold, and `command` could be any string.
An integer has too many values to list as well.
So a `match` on a string or an integer needs a last arm that catches the rest, such as `_`.
A `bool` doesn't need one, since `true` and `false` cover it.
Add the arm the help asks for, `_ => 0,`, as line 7, or press Solve.
