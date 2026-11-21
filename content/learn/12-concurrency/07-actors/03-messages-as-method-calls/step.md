---
title: Messages as method calls
---

Calling a method on a handle sends the actor a message, and the actor handles its messages one at a time, in the order they came.
`log` on line 6 returns nothing and takes 300 milliseconds, so `l.log(...)` on lines 18 and 19 is sent and `main` goes on at once, without waiting for it to be handled.
`all` on line 11 returns a value, so line 21 waits for the answer.
Line 17 reads the clock, and lines 20 and 22 check how long `main` has waited at each point.
Press Run.

Line 20 prints `true`: the two `log` calls took `main` less than 300 milliseconds, so it didn't wait for them.
By the time `all` is handled, both messages to `log` before it have been, so it gives both lines, and line 22 shows `main` waited at least the 600 milliseconds they took.
