---
title: Type arguments at a use
start_error: E0412
---

Line 9 calls `first` with an empty array, which has no element to fill `T` in from.
Press Run.

The program doesn't run.
E0412 says so at the `[]` on line 9: "cannot infer the element type of `[]`".
Its help writes the type on a variable, as line 13 did in the last step, but here the array goes straight into `first`, so the type goes on the call instead.
A type argument can be written where the function is used, in angle brackets after its name: `first<string>([])` makes `T` a `string`.
Methods take them the same way: for an `i64[]` called `xs`, `xs.map<string>(fun(p) = "{p} coins")` says `map` gives a `string[]`.
Make line 9's call `first<string>([])` and run again, or press Solve.
