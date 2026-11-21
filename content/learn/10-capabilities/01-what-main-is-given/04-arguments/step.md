---
title: Arguments
---

`args: string[]` on line 1 is what the program was started with, the program's own path first.
Line 2 prints how many there are, and lines 3 to 6 stop with exit code 1 when no name follows the path.
Line 7 greets each name, skipping the path with `skip(1)` from Iterators.
Here the program is started with no arguments after its path.
Press Run.

So it prints the usage line and exits with 1.
In the Playground, the input tab passes arguments: with `Ann Ben` it prints `3`, `hello, Ann` and `hello, Ben`.
