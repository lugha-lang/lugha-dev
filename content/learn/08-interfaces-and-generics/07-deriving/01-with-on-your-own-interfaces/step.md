---
title: with on your own interfaces
start_error: E0422
---

`with Eq` and `with Key` asked for interfaces the language knows how to build from a type's fields.
Your own interface can be built that way too, once it says how: the `derive` blocks on lines 5, 9 and 15 say how `i64`s, strings and every struct get `Describe`, and the next steps show how they're written.
`tell` on line 21 takes any `T: Describe`, and line 24 passes it a `Book`.
Press Run.

E0422 on line 24: "`Book` doesn't implement `Describe`".
A struct gets an interface from its blocks only when it asks, as it does for `Eq`.
Add `with Describe` after the `}` on line 19, or press Solve.
`impl Describe for Book = derive;` on a line of its own asks the same way.
