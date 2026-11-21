---
title: Counters with Ref
start_error: E0511
---

`count` on line 2 is a `let mut` variable.
The closure `tick` on line 3 takes no parameters, and its body, in braces, adds `1` to `count`.
Lines 4 and 5 call `tick` twice, and line 6 prints `count`.
Press Run.

The program doesn't run.
`tick` copied `count` when line 3 made it, so `count += 1` could only change that copy, never the `count` that line 6 prints.
E0511 says so on line 3: "can't change `count`: closures capture by copy".
Its help says to return a new value instead, which works when only the closure needs the result.
Here `main` must see the count too, so put it in a `Ref`: the closure copies the handle, and the closure and `main` reach the same box.
Make line 2 `let count = Ref.new(0);`, line 3's body `count.set(count.get() + 1);`, and line 6 print `count.get()`, then run again, or press Solve.
