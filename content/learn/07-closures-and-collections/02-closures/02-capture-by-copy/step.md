---
title: Capture by copy
---

A closure can use the variables around it.
`scale` on line 3 uses `rate`, which is `2` at that point, and line 4 changes `rate` to `7` afterwards.
Line 5 calls `scale(5)`, and line 6 prints `rate`.
Press Run.

Line 5 prints `10`, not `35`: `scale` copied `rate` when line 3 made it, so line 4's change doesn't reach it.
Line 6 prints `7`, so `rate` itself did change.
