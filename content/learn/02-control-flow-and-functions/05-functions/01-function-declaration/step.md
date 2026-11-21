---
title: Function declaration
---

So far `main` has been the only function, and a new one is declared the same way.
After `fun` and the name come its parameters with their types, and after the `)` a `:` and the type it gives back.
`main` calls `area` on line 6.
Press Run.

It prints `21`.
`area` comes first here, but the order of functions in a file doesn't matter, so `main` could be at the top instead.
`lughac` works out a `let`'s type from its value, but a function's parameter types are always written, and so is its return type when it gives a value back.
Leave the return type off, as `main` does on line 5, and the function gives back `()`, which means nothing.
