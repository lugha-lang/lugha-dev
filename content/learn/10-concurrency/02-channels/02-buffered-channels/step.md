---
title: Buffered channels
---

This time `Chan.buffered(3)` on line 9 makes a channel that holds up to 3 values, so `send` waits only when it's full.
`join` on line 11 waits for `produce` to finish, and it can, because all three values fit before `main` takes any.
Press Run.

`try_recv` on lines 12 to 15 takes a value if one is ready, without waiting.
Line 15 finds the channel empty, so it gets `None` at once.
