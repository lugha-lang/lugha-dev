---
title: Checked arithmetic
start_output: 255\n
---

`level` on line 2 is a `u8`, which holds 0 to 255.
Line 3 adds 5 to it, and line 4 adds 10.
Press Run.

Line 3 prints `255`.
Then line 4 panics with `integer overflow`, since 260 doesn't fit in a `u8`, and the program exits with code 101.
`checked_add` does the same addition and gives an `Option`: `Some` with the sum, or `None` where `+` would panic, so the program goes on.
On line 3, write `level.checked_add(5).debug()` in place of `level + 5`, and on line 4, `level.checked_add(10).debug()` in place of `level + 10`, then run again.
Or press Solve.
