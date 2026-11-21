---
title: Passing the console
start_error: E0301
error_note: `console` is a parameter of `main`, so it exists only inside `main`. `greet` has no parameter called `console`, so on line 2 there is nothing by that name.
---

`greet`, on lines 1 to 3, prints a line with `console.println`, and `main` calls it on line 6.
Press Run.

The program doesn't run: E0301 says "cannot find `console` in this scope", at line 2.
`console` is a parameter of `main`, and a parameter belongs to its own function, the way a variable declared in a block belongs to that block.
A function prints only through a `Console` it's given.
So `greet` needs a `console: Console` parameter of its own, and `main` passes it the console it was given.
Write `console: Console` between the parentheses on line 1 and `console` between them on line 6, then run again, or press Solve.
