---
title: What crosses to a task
---

A spawned call's arguments are worked out first, by the caller, and the task gets copies of them, as any function call does.
Line 12 starts `ship` with `order`.
`ship` can't change its parameter, so line 4 copies it into `copy`, and line 5 changes that.
Line 15 prints what the task gave back, and line 16 prints `order.qty` afterwards.
Press Run.

The first line is the scope's value, `Ok` with the text `ship` gave back, where its copy is down to 2.
The second is `3`: `ship` changed only its copy, and `order.qty` is still `3`.
Numbers and strings are `Sendable`, which means they can cross to a task this way, and so are arrays, structs and enums made of them.
So is a `Console`, which is why tasks have been given `console`.
A `Ref` isn't: passing one to a task is E0475.
