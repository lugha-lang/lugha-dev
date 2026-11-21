---
title: Escaping braces
start_error: E0301
error_note: Inside a string, `{name}` puts in the value of a variable called `name`, and this program has none. A brace meant as text is written twice.
---

Line 2 means to print the text `{name}`, braces and all.
Press Run.

The program doesn't run.
A single `{` in a string starts an interpolation, so `lughac` reads `name` as an expression and looks for a variable with that name.
There's none, and E0301 says "cannot find `name` in this scope", at line 2, column 29.
To write a brace itself, double it: `{{` gives `{`, and `}}` gives `}`.
Change `{name}` on line 2 to `{{name}}` and run again, or press Solve.
