---
title: Where an impl lives
start_error: E0459
---

A program can be split into modules, which come in Modules in chapter 11; every program so far has been one.
An `impl` is written in the module that declares the interface or the one that declares the type.
Line 1 implements `Display` for `bool`, so that `true` would print as `yes`; `Display` is the interface `console.println` prints through.
Press Run.

E0459: "this `impl Display for …` must be written in the module that declares `Display`".
`Display` and `bool` both come with the language, so neither is declared in this program, and no `impl` here can implement one for the other.
Declare an interface of your own instead: above line 1, write an interface `Label` with one method, `fun label(self): string;`, then change line 1 to `impl Label for bool {`, `show` on line 2 to `label`, and line 6 to print `true.label()`, or press Solve.
For a type you declare yourself, `impl Display` is allowed, as Equality, ordering and printing shows later in this chapter.
