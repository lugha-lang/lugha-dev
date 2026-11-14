---
title: Stopping an actor
---

An actor runs until it's stopped or the program ends, and every handle has `stop()` and `join()` for that.
`stop` on line 12 is a message too, so the `show` queued before it still runs, then the actor ends.
`join` waits until the actor has ended and gives an `Option<string>`: `None` when it was stopped.
Press Run.

The actor behind `b` has `by: 0`, so `show` divides by zero on line 5, and its panic message prints.
The panic ends only that actor, and `b.join()` on line 17 gives `Some` with the message.
So a panic stays inside its actor: `main` learns of it from `join`, and anyone who calls that actor afterwards panics instead.
