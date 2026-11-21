---
title: public
start_error: E0318
error_note: `unit` is `public`, so another package could call it, but it couldn't name the `Square` it gets back, since `Square` isn't `public`. A `public` function's parameter and return types must be `public` too.
---

`public` makes an item visible to other packages too, the ones that import its module.
Line 3 of `src/shapes.la` declares `unit` as `public`, but it returns a `Square`, and line 1 declares `Square` with no keyword.
This program is one package, with no other package to import it.
Press Run.

The program doesn't run, even with no other package here.
Another package could call `unit` but couldn't name the `Square` it returns, so a `public` declaration's parameter and return types must be `public` too.
E0318 says so, at line 3 of `shapes.la`.
Its help gives two ways out: make `Square` `public`, or drop `public` from `unit`.
Either would build here, since `main.la` is in the same package, but making `Square` `public` keeps `unit` usable by other packages.
The field `side` can stay without one: `main.la`, in the same package, reads it on line 5, though another package couldn't.
Add `public` before `struct Square` on line 1 of `shapes.la` and run again, or press Solve.
