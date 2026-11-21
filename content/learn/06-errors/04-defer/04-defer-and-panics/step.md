---
title: defer and panics
---

A panic leaves blocks too, on its way to ending the program.
Line 2 defers a line printing `cleaning up`, and line 4 reads `ages[2]`, past the end of `ages`, which has two elements.
Press Run.

`cleaning up` prints first: as the panic leaves `main`, it runs `main`'s pending defer.
Then the panic gives the length and the index, and where it happened, and the program exits with code 101.
