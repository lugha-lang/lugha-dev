---
title: Results can't be ignored
start_error: E0467
---

`check_age` on line 1 gives `Ok(())` for an age that makes sense, and an `Err` saying why otherwise.
`()` in `Ok(())` is the value that means nothing, since there's no answer to give back, only whether it worked.
Line 9 calls it with `150` as a statement, on its own.
Press Run.

E0467: "this `Result<(), string>` is discarded".
A `Result` used as a statement doesn't compile: it has to be handled, or dropped on purpose.
Other values can be thrown away with a `;`, as in Blocks and scopes, but a `Result` can't.
Handle it with an `if let`: make line 9 `if let .Err(e) = check_age(150) {`, then `console.println(e);` and a closing `}` on the next lines, or press Solve.
To drop one on purpose, write `let _ = check_age(150);`, as the help says.
`?`, which the help also names, comes in the next lesson.
