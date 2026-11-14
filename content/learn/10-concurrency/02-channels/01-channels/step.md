---
title: Channels
---

In 10.1 two threads shared a `Ref`, and a channel is another way for them to work together: one green thread hands values to another.
`Chan.new()` on line 9 makes one, and it carries `i64` values because line 9 writes `Chan<i64>`.
Passing `c` to `produce` copies the handle, and both copies name the same channel; `c.is(d)` tells whether two handles do.
`c.send(i)` on line 3 waits until a receiver takes the value, and `c.recv()` on line 12 waits for one to arrive.
Press Run.

`recv` gives an `Option`, so line 12 prints each value wrapped in `Some`.
Each "sent" line comes after `main` has taken that value, though not always after `main` has printed it, as "sent 1" shows.
