---
title: Comparison and logical operators
start_error: E0203
---

Comparisons such as `<=` and `<` give a `bool`.
Line 4 tries to check in one go that `age` is at least 18 and under 65, with `18 <= age < 65`.
Line 5 uses `!` for not and `||` for or.
Press Run.

The program doesn't run: E0203 says "`<=` and `<` can't be chained".
`18 <= age` gives a `bool`, and comparing that with `65` is never what was meant, so `lughac` refuses it.
The help line shows the way: two comparisons joined with `&&`, which means and; the parentheses it shows aren't needed.
`&&` and `||` stop as soon as the answer is known, so on line 5 `!member` is already `true`, and `age > 60` is never worked out.
Write `18 <= age && age < 65` on line 4 and run again, or press Solve.
