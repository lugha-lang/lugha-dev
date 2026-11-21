---
title: The main function
---

A Lugha program starts at `main`, the function that `fun` declares on line 2.
Line 1 is a doc comment, `/** … */`, a note about the function after it.
When the program starts, `main` is given the console as a parameter, named `console`, of type `Console`.
Line 3 prints through it, with `console.println`.
Press Run.

The output panel shows `Hello, world`, then "Exited with code 0".
That's the program's exit code: this `main` gives nothing back, so the program ends with 0 when it reaches the end of `main`.
