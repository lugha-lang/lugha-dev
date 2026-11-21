---
title: Stack overflow
start_output: 
---

`sum` on line 6 adds up a list by calling itself on the rest of it, on line 9.
Lines 14 to 17 build a list of a million `1`s.
Every call to `sum` waits for the next one to finish, and each waiting call takes room on the stack, which is finite: a million don't fit.
Press Run.

The program panics with `stack overflow`, the one panic that can't say where it happened, and exits with code 101.
Walk a long list with a loop instead.
Replace lines 7 to 10, the `match`, with `let mut total = 0;` and `let mut rest = list;`, then `while let .Cons(head, next) = rest {` with `total += head;` and `rest = next;` inside and a closing `}`.
Each pass adds the first value left in the list, and `rest = next` moves on to the rest, so `sum` no longer calls itself.
End `sum` with `total`, with no `;`, as its value, and run again, or press Solve.
