---
title: Matching on Option
start_error: E0417
---

`Option` is an enum, so a `match` gets at the value inside, as it did for `Shape`.
Line 13 matches on what `find` gives back for each name, and `.Some(i)` on line 14 names the position `i`.
Press Run.

E0417 on line 13: "non-exhaustive match: `.None` not covered".
A `match` covers every variant, and nothing here says what happens when a name isn't found.
Add `.None => console.println("{wanted} isn't there"),` after line 14, or press Solve.
`None` is built without a dot, but every variant in a pattern has its dot, `Some` and `None` included.
