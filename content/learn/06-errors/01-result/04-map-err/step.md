---
title: map_err
---

`map_err` changes the error inside an `Err`, and leaves an `Ok` as it is.
It takes a function from the old error to the new one, passed by name the way `update` takes one: here `explain` on line 8, which puts more words around the message.
Line 11 divides 10 by 0, line 12 prints the result as it is, and line 13 prints it again after `map_err(explain)`.
Press Run.

Line 12 prints the `Err` with the message from `divide`, and line 13 prints it with `explain`'s words around that message.
