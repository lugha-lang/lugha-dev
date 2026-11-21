---
title: debug
---

`debug(x)` on line 3 writes `x` to standard error, with the file and line, and then gives `x` back.
Standard error is a second output, kept apart from what `console.println` prints, for messages about the program, and the output panel shows it too.
`debug` needs no `Console`, so any function can use it, and because it gives back the value it can sit inside an expression, as `debug(price * 3) + 1` does.
Press Run.

Line 4 prints `31`.
The output panel shows the program's standard output first and its standard error after it, so the line `debug` wrote comes after `31`, though `debug` ran first.
That line is `[src/main.la:3] price * 3 = 30`, the file and line, the expression, and its value.
`debug` gave back `30`, so `total` is `30 + 1`.
`.debug()` gives back a string to print, and `debug(x)` writes the value out itself and gives back the value.
