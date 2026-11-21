---
title: map_err
---

`map_err` changes the error inside an `Err`, and leaves an `Ok` as it is.
It takes a function from the old error to the new one, here `explain` on line 8, passed by name, as `update` took `add_one` in Ref.
Line 12 prints the failed division as it is, and line 13 prints it again after `map_err(explain)`.
Press Run.
