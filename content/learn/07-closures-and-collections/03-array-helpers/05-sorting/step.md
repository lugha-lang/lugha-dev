---
title: Sorting
start_error: E0422
---

`sort` gives back a new array in ascending order, for numbers and for strings, as lines 4 and 5 show.
Line 7 sorts people.
Press Run.

E0422: "`Person` doesn't implement `Ord`", so there's no order for two `Person`s to follow.
The help offers `with Ord`, which orders by the fields in the order they're declared, here by `name` first.
To sort by age, `sort_by` takes the rule as a closure instead, one that says whether `a` comes before `b`.
Change `people.sort()` on line 7 to `people.sort_by(fun(a, b) = a.age < b.age)`, or press Solve.
It gives back a new array too, and people of the same age keep their order.
Floats have `<` but no order of their own: `[1.5, -2.0, 0.5].sort()` is E0451, whose help says "sort them with `xs.sort_by(f64.total_order)`", and `[1.5, -2.0, 0.5].sort_by(f64.total_order)` gives `[-2.0, 0.5, 1.5]`.
