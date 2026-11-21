---
title: Stopping an actor
---

An actor runs until it's stopped, and its scope stops it once the scope's body is done, which is how the actors in steps 1 and 3 ended without a `stop`.
`a.stop()` on line 11 stops it sooner, after the messages already sent; an actor has no `join`.
Line 12 calls `show` on the stopped actor.
Press Run.

A call to a stopped actor panics where it's made, here in the scope's body, with "actor `Divider` has stopped", and a panic in the body fails the scope too; the `Failure` names the scope, `s`.
A panic inside an actor's method fails its scope as well: with `by: 0`, `show` divides by zero, and the scope is an `Err`.
