---
title: Or-patterns
---

An arm can also take more than one value.
Line 4 has two patterns, `6` and `7`, joined by `|`, and the arm matches when either does.
Press Run.

It prints `weekend`, since `day` is `6`.
Change `6` on line 2 to `7` and it still prints `weekend`, and any other number gives `weekday`.
