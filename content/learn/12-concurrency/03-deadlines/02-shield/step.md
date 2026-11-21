---
title: shield
start_output: saving\ntrue\n
---

`save` on line 3 prints `saving`, sleeps 200 milliseconds on line 5, standing in for the saving, then prints `saved` and `after saving`.
Line 11's scope has a deadline of 100 milliseconds.
Press Run.

The deadline cancels `save` in its sleep on line 5, so `saved` never prints.
`shield within 500 { … }` holds cancellation off for its block, for at most 500 milliseconds, so that work which shouldn't stop halfway can finish.
The cancellation that was held off applies after the block, so `after saving` still doesn't print.
Put lines 5 and 6 inside `shield within 500 {` and a closing `}`, or press Solve.
