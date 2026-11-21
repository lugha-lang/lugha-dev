---
title: Failure
---

A scope's `Err` holds a `Failure`, with the failing task's name in `f.task` and how it failed in `f.kind`.
`f.kind` is `.Error(e)` for a task that gave `Err(e)`, `.Panic(m)` for one that panicked, and `.Deadline` for a scope that ran out of time, which comes in Deadlines.
`report` on line 13 matches on it, and lines 25 to 33 give it three scopes: one whose task fails with an `Err`, one whose task panics, and one whose task is fine.
A task is named after the function it calls, so the first two are `check` and `crash`.
A panic's message ends with where it happened, as in Panics, so `m` here does too.
Press Run.
