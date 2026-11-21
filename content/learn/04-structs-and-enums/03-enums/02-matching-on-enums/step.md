---
title: Matching on enums
---

A `match` can reach a variant's data: names in a pattern's parentheses are given the data, so `.Circle(r)` on line 9 names the radius `r`.
A variant in a pattern has a leading dot and no enum name before it, as on lines 9 to 11.
A name without a dot would be a new variable that matches anything, like `t` in `t if t < 0 =>`.
The arms must cover every variant: without the `.Empty` arm on line 11, E0417 would say "`.Empty` not covered".
Press Run.

Line 16 prints `12.56`, the area of a circle of radius 2.0.
Line 17 prints `2.0`, the area of a 1.0 by 2.0 rectangle.
