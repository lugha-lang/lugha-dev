---
title: Deriving for structs
start_error: E0451
error_note: `Book` asks for `Describe`, so each of its fields needs it too, and no `derive` block covers `price`, an `f64`.
---

`derive Describe for struct` on line 15 covers every struct that asks.
Inside it, `derive.fields(self, (), part)` calls `part` once per field, in order, and gives back an array of the results.
`part` on line 13 is passed to `derive.fields` as a function value, and gets `derive.fields`'s second argument as `ctx`, then the field's name and value.
Here `ctx` is `()`, nothing.
`part` is generic over one `F: Describe`, since each field has its own type.
Line 19's `Book` now has a `price`, an `f64`.
Press Run.

The program doesn't run.
A struct gets `Describe` only when each of its fields does, and no block covers `f64`.
E0451 says so on line 19, where `Book` asks: "`price` is `f64`, which no `derive Describe` block covers".
A struct's `describe` is reached only through the interface: `Book { … }.describe()` is E0415.
After line 11, add a `derive Describe for f64` block with `fun describe(self): string = "{self}";` in it, and run again, or press Solve.
