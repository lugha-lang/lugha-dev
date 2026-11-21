---
title: defer and panics
---

A panic leaves blocks too, and here it ends the program.
Line 2 defers `cleaning up`, and line 4 reads past the end of `ages`, so the program panics.
Press Run.

`cleaning up` prints before the program ends with the panic: as it leaves `main`, the panic runs `main`'s pending defer.
