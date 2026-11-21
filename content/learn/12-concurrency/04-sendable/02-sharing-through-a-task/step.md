---
title: Sharing through a task
start_error: E0475
error_note: `count` is a `Ref`, and both tasks would get the same box, so they could change it at the same time. A `Ref` stays with one task, so it can't be passed to `s.spawn`.
---

Copies of a `Ref` share one box.
`bump` on line 1 adds 1 to the number in a box, lines 8 and 9 hand the same box to two tasks, and line 11 prints the number afterwards.
Press Run.

The program doesn't run.
A `Ref` isn't `Sendable`: two tasks would share its box, and a `Ref` belongs to one task.
So each line that passes `count` to a task is an E0475, on lines 8 and 9.
The help names two ways to share a changing value between tasks, an actor or copies sent through a channel, and both come later in this chapter.
This fix needs neither: each task can give back its answer, and the scope can add them up.
Make line 11 `console.println(r.debug());`.
Replace lines 8 and 9 with `let a = s.spawn(bump(count));`, `let b = s.spawn(bump(count));` and `a.join().unwrap() + b.join().unwrap()`.
Make line 6 `let count = 0;`.
Replace lines 1 to 3 with `fun bump(n: i64): i64 = n + 1;`.
Or press Solve.
