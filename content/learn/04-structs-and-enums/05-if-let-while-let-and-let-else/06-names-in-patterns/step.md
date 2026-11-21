---
title: Names in patterns
start_output: an empty shape\n
---

`describe` matches on a `Shape`, and line 9's pattern is `Emtpy`, written without a dot.
Line 16 describes a circle.
Press Run.

A name without a dot in a pattern is always a new binding that matches any value, like `n` in `.Some(n)`, and that holds for a name on its own as an arm's whole pattern too.
`Emtpy` is misspelled, so it's no variant's name, and it catches every shape.
W0103 says "unused binding `Emtpy`", at line 9, and its help says a variant is written with a dot.
The two W0102 warnings mark the arms on lines 10 and 11 unreachable: line 9 comes first, so no shape gets past it.
So the circle prints `an empty shape`.
With its dot, a misspelling is an error instead: `.Emtpy` is E0415, "no variant `Emtpy` on `Shape`".
A bare name written on purpose, as in `other =>`, catches every value the arms above it didn't, and names it.
Write `.Empty` on line 9 and run again, or press Solve.
