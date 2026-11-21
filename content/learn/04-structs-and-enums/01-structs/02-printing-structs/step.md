---
title: Printing structs
start_error: E0422
error_note: `console.println` prints only values with a text form of their own, and a struct you declare has none until you write one. `.debug()` turns `p` into a string that shows its fields.
---

Line 5 now gives `console.println` the struct `p` itself.
Press Run.

The program doesn't run.
A struct has no text form of its own, as an array has none, so E0422 says `Point` doesn't implement `Display`, at line 5.
The help names two ways out.
The first, `impl Display for Point { … }`, writes a text form for `Point`, with code that later lessons teach.
The second, `.debug()`, works for a struct as it does for an array.
A struct's debug form is its name, then each field and its value in braces, in the order `Point` declares them.
Add `.debug()` after `p` on line 5 and run again, or press Solve.
