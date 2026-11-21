---
title: Shadowing
---

There's another way to give a name a new value without `mut`: declare it again.
Line 3 declares `score` a second time, from the old `score`.
Press Run.

It compiles and prints `15`.
A second `let` makes a new variable that hides the old one, which is called shadowing.
The new `score` starts at the end of its declaration, so `score + 5` on line 3 reads the old one.
Line 5 shadows it again with a string, which `mut` could never do: assigning changes a variable's value but never its type, while shadowing makes a new variable.
