---
title: Actor declaration
---

The green threads so far shared values through channels.
An actor is a green thread that keeps its own state, and other threads reach it only by calling its methods.
`actor Counter` on line 1 declares the state, the field `count` on line 2, and the methods, as a struct and its `impl` would together.
Inside the methods `self` is the state, so line 5, in `add`, changes `count`.
Line 12 starts the actor with `spawn` and the state's first value.
Press Run.

Only the actor's own methods reach its fields, so `c.count` in `main` would be E0439.
A field may not hold a `Ref` either, because that box would then be shared outside the actor, and that's E0439 too.
