---
title: stdout and stderr
---

A program has two outputs: standard output, where `println` writes, and standard error, where `eprintln` writes, for messages about the run rather than its results.
`noisy` on line 1 writes one line to each, and line 7 calls it with the console.
Line 8 passes `noisy` a narrower `Console`, `console.stdout_only()`, whose `eprint` and `eprintln` do nothing and which has no input to read, while `console` itself still writes to both.
Press Run.

Both calls print `result: 42`, and only the first writes its note to standard error, which the output pane shows separately.
