---
title: What crosses to a task
---

A spawned call's arguments are worked out first, by the caller, and the task gets copies of them, as a function call does (Copies).
Line 12 starts `ship` with `order`; `ship` can't change its parameter, so line 4 copies it into `copy`, as in Passing by value, and line 5 changes that.
Line 15 prints what the task gave back, and line 16 prints `order.qty` afterwards.
Press Run.

`ship` changed only its copy: `order.qty` is still `3`.
Numbers and strings are `Sendable`, and so are arrays, structs and enums made of them: they can cross to a task this way.
A `Ref` isn't: passing one to a task is E0475, as the next step shows.
