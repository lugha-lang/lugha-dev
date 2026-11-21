---
title: Where an impl lives
start_error: E0459
error_note: An `impl` must be written in the module that declares the interface or the one that declares the type. `Display` and `bool` both come with the language, so this program can't implement one for the other.
---

An `impl` is written in the module that declares the interface or the one that declares the type; a module is one part of a program, and every program so far has been a single module.
`Display` is the interface `console.println` prints through, and its method is `show`.
Lines 1 to 3 implement it for `bool`, to print `true` as `yes`.
Press Run.

The program doesn't run.
`Display` and `bool` both come with the language, so no `impl` in this program can implement one for the other.
E0459 says so at line 1: "this `impl Display for …` must be written in the module that declares `Display`".
For a type you declare yourself, `impl Display` is allowed.
Use an interface of your own instead.
Change line 6 to print `true.label()`, `show` on line 2 to `label`, and line 1 to `impl Label for bool {`.
Then, above line 1, declare an interface `Label` with one method, `fun label(self): string;`, and run again, or press Solve.
