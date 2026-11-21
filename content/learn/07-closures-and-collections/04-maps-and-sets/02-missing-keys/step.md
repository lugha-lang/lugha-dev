---
title: Missing keys
---

`get` on line 3 gives an `Option`: `Some` with the value, or `None` when the key isn't there, as on line 4.
`has` on line 5 only asks whether the key is there.
Line 6 reads a missing key with `[…]`.
Press Run.

Lines 3 to 5 print `Some(31)`, `None` and `false`.
Then line 6 panics: the program stops with `no key "dee" in the map` and the line it happened on, and exits with code 101.
When a key may be missing, use `get` or `has`.
