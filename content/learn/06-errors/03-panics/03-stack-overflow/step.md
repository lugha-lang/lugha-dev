---
title: Stack overflow
start_output: 
---

`sum` on line 6 is the recursive sum from Recursive enums, and lines 14 to 17 build a list of a million `1`s.
Every call to `sum` waits for the next one to finish, and each waiting call takes room on the stack, which is finite: a million don't fit.
Press Run.

It panics with `stack overflow`, the one panic that can't say where it happened.
Walk a long list with a loop instead.
Replace lines 7 to 10, the `match`, with `let mut total = 0;` and `let mut rest = list;`, then `while let .Cons(head, next) = rest {` with `total += head;` and `rest = next;` inside and a closing `}`.
End `sum` with `total`, with no `;`, as its value, or press Solve.
Each pass takes one node's number, and `rest = next` moves on to the rest of the list, so `sum` no longer calls itself.
