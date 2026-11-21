---
title: Passing the console
start_error: E0301
---

`greet` on line 1 prints a line, and `main` calls it on line 6.
Press Run.

`lughac` gives E0301 on line 2, "cannot find `console` in this scope".
`console` is a parameter of `main`, and a parameter belongs to its own function, the way a `let` belongs to its block.
There is no `println` without a `Console`, as Hello, world showed.
So `greet` needs a `console: Console` parameter of its own, and `main` passes it the console it was given.
Write `console: Console` between the parentheses on line 1 and `console` between them on line 6, or press Solve.
