---
title: Names in patterns
start_output: an empty shape\n
---

Line 16 describes a circle.
Press Run.

It prints `an empty shape`.
`Emtpy` on line 9 is misspelled and has no dot, and a bare name in a pattern is always a new binding, even when it is the whole pattern rather than part of a variant.
Spelled right, a bare `Empty` is E0468, as in Enums, but `Emtpy` is no variant's name, so it's read as a binding.
A binding matches any shape, and line 9 comes first, so every shape stops there.
`lughac` warns with W0103, "unused binding `Emtpy`", and marks lines 10 and 11 unreachable with W0102.
With the dot, a misspelling is an error instead: `.Emtpy` is E0415, "no variant `Emtpy` on `Shape`".
Write `.Empty` on line 9, or press Solve.
A bare name written on purpose, as in `other =>`, catches every value the arms above it didn't and names it.
