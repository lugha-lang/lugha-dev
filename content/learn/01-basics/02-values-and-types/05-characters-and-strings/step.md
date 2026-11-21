---
title: Characters and strings
start_error: E0102
---

Text has two types.
A `char` holds one character, in single quotes, as on line 2.
A `string` holds any text, in double quotes, and a `\` inside it starts an escape, such as `\t` for a tab on line 4.
`\u{…}` writes a character by its Unicode number in hex, in a `char` on line 3 and in a string on line 4.
The string that starts on line 5 runs on to line 6.
Press Run.

The program doesn't run, and E0102, "unterminated string", shows twice.
A string ends on the line it starts, so the string opened on line 5 never closes, and the `"` on line 6 is read as the start of another one.
The help line under each error gives the way to put a line break in a string: `\n`.
Join lines 5 and 6 into `"first line\nsecond line"` and run again, or press Solve.
