---
title: Deriving for structs
start_error: E0451
---

`derive Describe for struct` on line 15 covers every struct that asks.
Inside it, `derive.fields(self, (), part)` calls `part` once per field, in order, and gives back an array of the results.
`part` on line 13 is passed as a value, as in Functions as values, and gets the second argument as `ctx`, then the field's name and value.
Here `ctx` is `()`, nothing; derive.build, in step 8, puts it to use.
`part` is generic over one `F: Describe`, since each field has its own type.
Line 19's `Book` now has a `price`, an `f64`.
Press Run.

E0451 on line 19, where `Book` asks: "`price` is `f64`, which no `derive Describe` block covers".
A struct gets `Describe` only when each of its fields does.
After line 11, add a `derive Describe for f64` block with `fun describe(self): string = "{self}";` in it, or press Solve.
A struct's `describe` is reached only through the interface: `Book { … }.describe()` is E0415.
