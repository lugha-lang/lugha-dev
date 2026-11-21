---
title: Ref.update
---

`update` takes a function, and a closure can be written right there instead of a named one like `add_one`, which `update` took by name in the Ref lesson.
Line 3 passes `update` the closure `fun(n) = n * 3`, and `n` takes its type from `update`'s parameter, a `fun(i64): i64`, as `x` did from `apply`'s.
Press Run.

`update` called the closure on the `10` in the box and put back the `30` it returned, which line 4 prints.
