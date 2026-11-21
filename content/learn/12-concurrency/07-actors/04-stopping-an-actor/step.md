---
title: Stopping an actor
---

An actor runs until it's stopped, and its scope stops it once the scope's body is done, which is how the actors in steps 1 and 3 ended without a `stop`.
`a.stop()` on line 11 stops it sooner, after the messages already sent; an actor has no `join`.
Line 10 calls `show` before the stop, and line 12 calls it on the stopped actor.
Line 8 keeps the scope's value in `ok`, though this time it turns out to be an `Err`.
Press Run.

`5` comes from line 10.
A call to a stopped actor panics where it's made, here in the scope's body, so line 12 prints nothing.
A panic in the body fails the scope too, so line 14 prints an `Err` with a `Failure`.
Its `task` is the scope, `s`, and its `kind` is a `Panic` with the message "actor `Divider` has stopped", then where the call was made, line 12.
