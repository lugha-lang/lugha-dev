---
title: Channels
---

A channel carries values from one task to another, in order.
`Chan<i64>.new(4)` on line 9 makes one that holds up to four `i64`s, and gives its two ends: a `Sender<i64>`, `tx`, and a `Receiver<i64>`, `rx`.
`produce` on line 1 sends three squares with `out.send`, and closes the channel on line 5 when it's done.
`rx.recv()` on lines 12 to 15 waits for the next value and gives `Some(v)`, or `None` once the channel is closed and empty.
Press Run.

The first three lines are the squares, each in `Some`, in the order `produce` sent them.
The fourth `recv` gives `None`: three values came, then the close.
The last line is the scope's value, `Ok(())`.
Here the channel never fills; when one is full, `send` waits for room.
A channel made with `Chan<i64>.new(0)` holds no values, so each `send` waits until a receiver takes the value.
