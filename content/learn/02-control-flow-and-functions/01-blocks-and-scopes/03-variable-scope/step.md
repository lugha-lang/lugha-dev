---
title: Variable scope
start_error: E0301
---

`price` is declared inside the block, on line 3, and line 6 tries to print it after the block's `}`.
Press Run.

`lughac` refuses it with E0301, "cannot find `price` in this scope".
A variable declared in a block ends at the `}` that closes it, so `price` doesn't exist on line 6.
What's left of the block is its value, in `total`.
Print `total` on line 6 instead and run again, or press Solve.
