---
title: try_send and try_recv
---

`try_send` and `try_recv` never wait: they say what happened instead.
`try_send` gives `.Sent`, `.Full(v)` when there's no room, or `.Closed(v)` when the channel is closed, the last two giving `v` back.
`try_recv` gives `.Ready(v)`, `.Empty` when nothing has come, or `.Closed` when the channel is closed and empty.
The channel on line 2 holds one value, and lines 3 to 9 try each case, closing it on line 7.
Press Run.

`Sent` comes from line 3, since the channel had room for `1`.
`Full(2)` comes from line 4: `1` still fills the channel, so `2` comes back.
Line 5 gives `Ready(1)`, and line 6 gives `Empty`, since nothing else was sent.
After line 7 closes the channel, line 8's `try_send` gives `Closed(3)`, and line 9's `try_recv` gives `Closed`.
