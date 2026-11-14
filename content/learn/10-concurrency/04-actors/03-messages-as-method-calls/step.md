---
title: Messages as method calls
---

Calling a method on a handle sends the actor a message, and the actor handles its messages one at a time, in the order they came.
`log` returns nothing, so `l.log("first")` on line 14 is queued and `main` goes on at once.
Press Run.

"main goes on" prints before "log: first", because `main` didn't wait for `log`.
`count` returns a value, so line 17 waits for it, and by then both messages to `log` have been handled.
