---
title: Sorting
start_error: E0422
error_note: `sort` needs to know how two values compare, which a type says by being `Ord`. `Person` isn't, so add `with Ord` after its declaration, or sort with `sort_by` and a rule of your own.
---

`sort` gives back a new array in ascending order.
Lines 4 and 5 sort numbers and strings, and line 7 sorts `Person`s.
Press Run.

The program doesn't run.
`sort` needs a type that is `Ord`, one with an order of its own, and `Person` has none.
E0422 says so on line 7: "`Person` doesn't implement `Ord`".
Of the two ways its help offers, the one for now is `with Ord` after the declaration: as `with Eq` gives `==`, it gives an order, by the fields in the order they're declared, here by `name` first.
To sort by age, `sort_by` takes the rule as a closure instead, one that says whether `a` comes before `b`.
It keeps people of the same age in their order.
Floats have `<` but no order of their own: `[1.5, -2.0, 0.5].sort()` is E0451, and its help says "sort them with `xs.sort_by(f64.total_order)`", which gives `[-2.0, 0.5, 1.5]`.
Change `people.sort()` on line 7 to `people.sort_by(fun(a, b) = a.age < b.age)` and run again, or press Solve.
