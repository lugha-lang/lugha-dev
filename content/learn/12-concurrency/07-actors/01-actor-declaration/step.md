---
title: Actor declaration
---

An actor is a task that keeps its own state, and other tasks reach it only by calling its methods.
`actor Counter` on line 1 declares the state, the field `count` on line 2, and the methods, as a struct and its `impl` would together.
Inside the methods `self` is the state, and `add` takes `mut self`, as a method in Methods can, so line 5 changes `count`.
Line 13 starts the actor in the scope with the state's first value, as a task is started, and gives back a handle, `c`.
The scope stops the actor once its body is done.
Press Run.

Only the actor's own methods reach its fields: `c.count` in `main` is E0439.
