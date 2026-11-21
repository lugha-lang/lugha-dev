---
title: Characters and strings
start_error: E0102
---

That leaves text, which has two types.
A `char` in single quotes is one character, as on line 2.
A `string` in double quotes is any text, with escapes such as `\t` for a tab on line 4.
`\u{…}` writes a character by its Unicode number in hex, in a `char` on line 3 and in a string on line 4.
The string on line 5 runs on to line 6.
Press Run.

`lughac` reports E0102 twice, once for each line, because a string ends on the line it starts.
A line break inside a string is written `\n`.

Join lines 5 and 6 with `\n` and run again, or press Solve.
