---
title: Reading input
---

The `Console` reads too: `console.read_line()` gives the next line of the program's input, without its `\n`.
It's a `Result<Option<string>, string>`: `Ok(Some(line))` for a line, `Ok(None)` once the input has ended, and an `Err` when it can't be read.
`while let` on line 4 keeps reading as long as `read_line` gives a line, and stops at the end of the input or at an `Err`, as `pop` did in if let, while let and let else.
Line 6 adds each line up as a number, or 0 when it isn't one.
Here the program is started with no input.
Press Run.

The first `read_line` is already `Ok(None)`, so the loop never runs.
In the Playground, the input tab gives a program its input: with `3`, `4` and `10` on three lines it prints `3 lines, total 17`.
