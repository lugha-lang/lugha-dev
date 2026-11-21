---
title: Proc
---

A `Proc` starts other programs.
`proc.run(cmd, args)` on line 2 runs `echo` with two arguments, `hello` and `$HOME; rm -rf /`.
It gives an `Ok(ProcessOutput)`, with the program's exit `code`, its `stdout` and its `stderr`.
`run_with` on line 4 also writes to the program's input, here two lines for `sort`.
Line 6 starts `sh` as an ordinary program, with `-c` and `exit 3` as its arguments.
Line 8 names a program that doesn't exist.
Press Run.

The first line is `echo`'s exit code, `0`, then its output, with `$HOME; rm -rf /` exactly as written.
Each argument goes to the program as it is, with no shell in between, so `$HOME` isn't replaced and `;` doesn't start a second command.
`apple,pear` is `sort`'s output, its lines joined by line 5.
Line 7 prints `3`: any exit code counts as `Ok`, so `unwrap` on line 6 gets the output.
Line 8's program couldn't be started, so the last line is an `Err`, holding the system's own message.
