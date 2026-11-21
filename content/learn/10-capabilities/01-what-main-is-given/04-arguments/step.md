---
title: Arguments
---

`args: string[]` on line 1 holds what the program was started with: its own path first, then any arguments.
Line 2 prints how many there are.
Lines 3 to 6 print a usage line and return exit code 1 when no name follows the path.
Line 7 greets each name, skipping the path with `skip(1)`.
Here the program starts with no arguments after its path.
Press Run.

The first line is `1`: `args` holds only the path.
So the program prints the usage line, and the panel shows "Exited with code 1".
In the Playground, the input tab passes arguments: with `Ann Ben` it prints `3`, `hello, Ann` and `hello, Ben`.
