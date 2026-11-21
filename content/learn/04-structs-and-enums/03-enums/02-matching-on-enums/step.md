---
title: Matching on enums
---

A `match` reaches a variant's data: names in its parentheses are given the data, so `.Circle(r)` on line 9 names the radius `r`.
A variant in a pattern has a leading dot and no enum name before it, as on lines 9 to 11.
A name without a dot would be a new variable that matches anything, like `t` in the match lesson.
Press Run.

The arms must cover every variant: without `.Empty`, E0417 says "`.Empty` not covered".
