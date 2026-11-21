---
title: Matching on Option
start_error: E0468
---

`Option` is an enum, so a `match` gets at the value inside, as it did for `Shape`.
Line 13 matches on what `find` gives back for each name.
`.Some(i)` on line 14 names the position `i`, and line 15 covers a name that isn't there.
Press Run.

E0468 on line 15: `None` is a variant of `Option<i64>`, so in a pattern it takes a leading dot.
`None` is built without one, but every variant in a pattern has its dot, `Some` and `None` included.
Change `None` to `.None` on line 15, or press Solve.
Leaving out that arm is E0417, so the program has to say what happens when a name isn't found.
