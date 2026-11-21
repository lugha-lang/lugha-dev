---
title: with on your own interfaces
start_error: E0422
error_note: `tell` needs a `Describe`, and `Book` gets one from the interface's `derive` blocks only when it asks, with `with Describe` after its declaration.
---

`with Eq` and `with Key` asked for interfaces the language knows how to build from a type's fields.
An interface of your own can be built from a type's fields too, if it has `derive` blocks that say how.
`Describe` on lines 1 to 3 is one, and its blocks on lines 5, 9 and 15 cover `i64`s, strings and every struct.
The next steps explain lines 5 to 17; this step needs only lines 19 to 24.
`tell` on line 21 takes any `T: Describe`, and line 24 passes it a `Book`.
Press Run.

The program doesn't run.
A struct gets an interface from the interface's blocks only when it asks, as it does for `Eq`, and `Book` on line 19 doesn't ask.
E0422 says so at the call on line 24: "`Book` doesn't implement `Describe`".
`impl Describe for Book = derive;` on a line of its own asks the same way.
Add `with Describe` after the `}` on line 19 and run again, or press Solve.
