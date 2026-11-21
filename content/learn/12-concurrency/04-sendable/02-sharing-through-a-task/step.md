---
title: Sharing through a task
start_error: E0475
---

Copies of a `Ref` share one box, as in Ref.
`bump` on line 1 adds 1 to the number in a box, and lines 8 and 9 hand the same box to two tasks.
Press Run.

E0475 on lines 8 and 9: a `Ref` isn't `Sendable`, since two tasks would share it, and a `Ref` belongs to one task.
Here each task can give back its answer instead, and the scope adds them up.
When many tasks need one changing value, the help names two ways: send copies through a channel, which comes next, or keep the value in an actor, at the end of the chapter.
Make line 11 `console.println(r.debug());`.
Replace lines 8 and 9 with `let a = s.spawn(bump(count));`, `let b = s.spawn(bump(count));` and `a.join().unwrap() + b.join().unwrap()`.
Make line 6 `let count = 0;`.
Replace lines 1 to 3 with `fun bump(n: i64): i64 = n + 1;`.
Or press Solve.
