---
title: Results can't be ignored
start_error: E0467
---

`check_age` on line 1 gives `Ok(())` for an age that makes sense, and an `Err` saying why otherwise.
`()` in `Ok(())` is the value that means nothing: there's no answer to give back, only whether it worked.
Line 9 calls it with `150` as a statement, and nothing looks at what it gives back.
Press Run.

The program doesn't run.
Other values can be thrown away with a `;`, but a `Result` used as a statement would lose its `Err` without anyone looking, so it doesn't compile.
E0467 says this `Result<(), string>` is discarded.
Its help names ways to handle it, `match` among them, and `?`, which comes in the next lesson.
It also says to drop it on purpose with `let _ = …;`, and `let _ = check_age(150);` would print only `checked`.
Handle it with an `if let` that prints the error: make line 9 `if let .Err(e) = check_age(150) {`, then `console.println(e);` and a closing `}` on the next lines, and run again, or press Solve.
