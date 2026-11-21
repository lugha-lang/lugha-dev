---
title: Reading input
---

The `Console` reads too: `console.read_line()` gives the next line of the program's input, without its `\n`.
It's a `Result<Option<string>, string>`: `Ok(Some(line))` for a line, `Ok(None)` once the input has ended, and an `Err` when it can't be read.
The `while let` on line 4 keeps reading as long as `read_line` gives a line, and stops at the end of the input or at an `Err`.
Line 5 counts the lines, and line 6 adds each one up as a number, or 0 when it isn't one.
Here the program starts with no input.
Press Run.

The first `read_line` is already `Ok(None)`, so the loop never runs, and line 8 prints `0 lines, total 0`.
In the Playground, the input tab gives a program its input: with `3`, `4` and `10` on three lines it prints `3 lines, total 17`.
