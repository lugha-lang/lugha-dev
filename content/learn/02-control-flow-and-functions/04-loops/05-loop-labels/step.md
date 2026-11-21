---
title: Loop labels
start_output: 1 1\n1 2\n1 3\n2 1\n3 1\n3 2\n3 3\n
---

One `for` runs inside another: for each `row` on line 2, the loop on line 3 goes through each `col`.
Line 7 prints the pair, and `{row}` and `{col}` put each number into the text.
Line 5's `break` is meant to stop everything at the first pair whose product is 4.
Press Run.

It prints seven pairs.
Row 1 prints `1 1`, `1 2` and `1 3`.
Row 2 prints `2 1`, then `2 2` makes 4 and the `break` runs.
A `break` ends only the loop it's in, the inner one, so the outer loop goes on to row 3, which prints `3 1`, `3 2` and `3 3`.
To leave the outer loop, give it a label, a name followed by `:`, before its `for`, and write that name after `break`.
`continue outer;` works the same way, going on to the outer loop's next turn.
Add `outer:` before `for` on line 2 and `outer` after `break` on line 5, then run again, or press Solve.
