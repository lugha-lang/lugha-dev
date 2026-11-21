---
title: debug
---

`debug(x)` on line 3 writes `x` to standard error, with the file and line, and gives `x` back.
It needs no `Console`, so any function can use it, and since it gives `x` back it can go inside an expression.
Press Run.

Line 3 writes `[src/main.la:3] price * 3 = 30`, and `debug` gives `30` back, so `total` is `31`.
Unlike `.debug()`, it writes the value out itself and gives back the value, not a string.
The output pane shows standard error as well, which is where this line goes.
