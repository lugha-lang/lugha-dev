---
title: Proc
---

A `Proc` starts other programs.
`proc.run(cmd, args)` on line 2 runs `echo` with two arguments, `hello` and `$HOME; rm -rf /`, and gives an `Ok(ProcessOutput)`, with its exit `code`, its `stdout` and its `stderr`.
`run_with` on line 4 also writes to the program's input, here two lines for `sort`.
Line 6 starts `sh` as an ordinary program, with `-c` and `exit 3` as its arguments, to get an exit code of 3, and line 8 names a program that doesn't exist.
Press Run.

Line 3 prints `$HOME; rm -rf /` exactly as it was written: each argument goes to the program as it is, with no shell in between, so `$HOME` isn't replaced and `;` doesn't start a second command.
Line 7 prints `3`: any exit code counts as `Ok`, so `unwrap` on line 6 gets the output.
Line 8's program doesn't exist, so it couldn't be started: that's an `Err`, holding the system's own message, as in Files.
