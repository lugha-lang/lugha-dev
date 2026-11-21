---
title: Actor declaration
---

An actor is a task that keeps its own state, and other tasks reach it only by calling its methods.
`actor Counter` on line 1 declares the state, the field `count` on line 2, and the methods, as a struct and its `impl` would together.
Inside the methods `self` is the state, and `add` takes `mut self`, so line 5 can change `count`.
Line 13 starts the actor in the scope with the state's first value, as a task is started, and gives back a handle, `c`.
Lines 14 to 16 call the actor's methods through `c`, and the scope stops the actor once its body is done.
Press Run.

`5` comes from line 16: the actor added 2 and 3 to its `count`, which started at 0.
The last line is the scope's value, `Ok(())`.
