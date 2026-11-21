---
title: Constants
---

A value the whole program shares is a constant, declared with `const` outside any function, as on line 1.
Its type is always written.
Press Run.

Line 5 reads `MAX_SCORE` like a variable, but nothing can assign to it, and trying is E0501.
`let` is refused outside a function, so a shared value is always a `const`, worked out once before `main` runs.
