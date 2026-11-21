---
title: Matching on Result
---

This is `divide` again.
The loop on line 9 tries the divisors `2` and `0`, and line 10 matches on each `Result`.
`.Ok(q)` on line 11 names the answer `q`, and `.Err(e)` on line 12 names the message `e`, each with its dot as in any pattern.
The `match` has to cover both: without the `.Err` arm it's E0417, "`.Err` not covered".
Press Run.

The first pass takes the `.Ok` arm and prints `10 / 2 is 5`, and the second takes the `.Err` arm and prints the message.
