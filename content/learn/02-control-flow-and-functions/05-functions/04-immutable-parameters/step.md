---
title: Immutable parameters
start_error: E0501
---

`with_tax` adds a tenth to `price` on line 2.
Press Run.

It gives E0501 for line 2, because a parameter is like a `let` without `mut`.
Its help suggests shadowing, which you met in Variables.
`let mut price = price;` makes a copy you can change, and from the next line on, `price` means the copy.
Add it as a new line 2, or press Solve.
