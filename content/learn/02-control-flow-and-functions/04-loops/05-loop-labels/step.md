---
title: Loop labels
start_output: 1 1\n1 2\n1 3\n2 1\n3 1\n3 2\n3 3\n
---

One `for` runs inside another, and line 7 prints each `row` and `col` pair, putting both numbers into the text with `{…}`.
Line 5 should stop everything at the first pair whose product is 4.
Press Run.

The `break` there ends only the inner loop, the one it's in, so row 2 prints `2 1` and stops, and row 3 runs as normal.
To leave the outer loop, give it a label, a name followed by `:`, before its `for`, and name it after `break`.
Add `outer:` before `for` on line 2 and `outer` after `break` on line 5, or press Solve.
`continue outer;` works the same way, going on to the outer loop's next turn.
