---
title: mut bindings
start_error: E0501
error_note: `n` is a name the pattern on line 4 gave the number inside `count`, and names in a pattern can't change, like parameters. `.Some(mut n)` gives the arm its own copy to change.
---

`count` on line 2 holds `Some(4)`, and the arm on line 4 names the number inside it `n`.
Line 5 adds 1 to `n`.
Press Run.

The program doesn't run.
E0501 says "cannot assign to `n`: it is not mutable", at line 5: names in a pattern can't change, like parameters.
The help suggests copying `n` into a `let mut`.
`mut` before the name in the pattern does that in one step, giving the arm its own copy to change, so `count` itself stays `Some(4)`, and line 10 prints it.
Change `.Some(n)` on line 4 to `.Some(mut n)` and run again, or press Solve.
