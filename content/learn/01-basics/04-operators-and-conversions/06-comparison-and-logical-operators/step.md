---
title: Comparison and logical operators
start_error: E0203
---

Comparisons give a `bool`, and line 4 checks in one go that `age` is at least 18 and under 65.
Press Run.

Comparisons don't chain, so `lughac` stops at E0203.
The two halves are joined with `&&`: write `18 <= age && age < 65` on line 4 and run it again, or press Solve.
Line 5 uses `!` for not and `||` for or, and `&&` and `||` stop as soon as the answer is known.
So when `zero` is 0, `zero != 0 && 10 / zero > 1` is `false` and the division by zero from step 4 never runs.
