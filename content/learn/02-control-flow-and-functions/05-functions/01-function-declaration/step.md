---
title: Function declaration
---

So far `main` has been the only function, and a new one is declared the same way, with `fun`.
Line 1 declares `area`: after its name come its parameters, `width` and `height`, each with its type, and after the `)` a `:` and its return type, the type it gives back.
Its body on line 2 gives back `width * height`, its last expression.
Line 6 calls `area` with `7` and `3`.
Press Run.

It prints `21`.
`area` comes first here, but the order of functions in a file doesn't matter, so `main` could be at the top instead.
`lughac` works out a `let`'s type from its value, but a function's parameter types are always written, and so is its return type when it gives a value back.
Leave the return type off, as `main` does on line 5, and the function gives back `()`, which means nothing.
