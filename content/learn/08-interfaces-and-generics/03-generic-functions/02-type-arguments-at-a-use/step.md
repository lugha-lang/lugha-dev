---
title: Type arguments at a use
start_error: E0412
---

Line 9 calls `first` with an empty array, which has no element to fill `T` in from.
Press Run.

E0412: "cannot infer the element type of `[]`".
Its help annotates a variable, as `names` did in step 1; here the array goes straight into `first`, so the type goes on the call instead.
A type argument can be written where the function is used, in angle brackets after its name: `first<string>([])` makes `T` a `string`.
Make line 9's call `first<string>([])`, or press Solve.
Methods take them the same way: for an `i64[]` called `xs`, `xs.map<string>(fun(p) = "{p} coins")` says `map` gives a `string[]`.
