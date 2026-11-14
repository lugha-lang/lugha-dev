---
title: Deriving for structs
start_error: E0451
---

`derive Describe for struct` on line 15 covers every struct at once.
Inside it, `derive.fields(self, (), part)` calls `part` once per field, in order, and gives back an array of the results.
`part` is passed as a value, as in Functions as values.
`part` gets the second argument as `ctx`, then the field's name and value.
Here `ctx` is `()`, nothing; step 7 puts it to use.
`part` must be generic over one `F: Describe`, since each field has its own type.
Press Run.

`lughac` gives E0451: `price` is an `f64`, and no block covers `f64`.
A struct meets `Describe` only when each of its fields does.
Add a block for `f64` after line 11; Solve does it for you.
