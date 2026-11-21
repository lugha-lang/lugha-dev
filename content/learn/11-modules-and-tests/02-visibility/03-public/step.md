---
title: public
start_error: E0318
---

`public` makes an item visible to other packages too, the ones that import its module.
Line 3 of `shapes.la` declares `unit` as `public`, but it returns a `Square`, which has no keyword.
This program is one package, with no other package to import it.
Press Run.

That's E0318, even with no other package here: another package could call `unit` but couldn't name the `Square` it returns.
A `public` declaration's parameter and return types must be `public` too, so `Square` needs the keyword.
`side` still has none: `main.la`, in the same package, can read it, but another package couldn't.
Add `public` before `struct Square` on line 1 of `shapes.la`, or press Solve.
