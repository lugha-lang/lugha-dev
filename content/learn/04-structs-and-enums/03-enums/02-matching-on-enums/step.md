---
title: Matching on enums
start_error: E0212
---

A `match` reaches a variant's data: names in its parentheses are given the data, so `Circle(r)` on line 9 names the radius `r`.
Press Run.

E0212 on lines 9 and 10 says a variant in a pattern takes a leading dot, `.Circle(r)`, with no enum name before it.
A name without a dot is a new variable that matches anything, like `t` in the match lesson, so line 11's `Empty` isn't flagged yet.
Put a `.` before `Circle`, `Rect` and `Empty` on lines 9 to 11, or press Solve.
Fix only lines 9 and 10, and line 11 gets E0468: a bare name that is one of `Shape`'s variants needs its dot.
The arms must cover every variant too: without `.Empty`, E0417 says "`.Empty` not covered".
