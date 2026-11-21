---
title: Variable scope
start_error: E0301
error_note: `price` was declared inside the block on lines 2 to 5, so it ends at the block's `}` on line 5. On line 6 there is no `price` to print.
---

Lines 2 to 5 are a block again, and `price` is declared inside it, on line 3.
Line 6, after the block's `}`, tries to print `price`.
Press Run.

The program doesn't run: E0301 says "cannot find `price` in this scope", at line 6.
A variable's scope is the part of the code where it exists, and a variable declared in a block ends at the `}` that closes it.
So `price` doesn't exist on line 6.
What's left of the block is its value, in `total`.
Print `total` on line 6 instead and run again, or press Solve.
