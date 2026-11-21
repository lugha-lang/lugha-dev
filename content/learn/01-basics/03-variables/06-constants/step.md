---
title: Constants
---

A value the whole program shares is a constant, declared with `const` outside any function, as on line 1.
A constant's type is always written, here `i64`.
Line 5 uses `MAX_SCORE` the way it would use a variable.
Press Run.

It prints `60`, `MAX_SCORE` minus `score`.
Nothing can assign to a constant: `MAX_SCORE = 5;` would be E0501, the error from step 2.
`let` isn't allowed outside a function, so a value the whole program shares is always a `const`, worked out once before `main` runs.
