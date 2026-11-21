---
title: Failure
---

A scope's `Err` holds a `Failure`, with the failing task's name in `f.task` and how it failed in `f.kind`.
`f.kind` is `.Error(e)` for a task that gave `Err(e)`, `.Panic(m)` for one that panicked, and `.Deadline` for a scope that ran out of time.
`report` on line 13 matches on it.
Lines 25 to 33 give `report` three scopes: one whose task fails with an `Err`, one whose task panics, and one whose task is fine.
A task is named after the function it calls, so the first two are `check` and `crash`.
Press Run.

The first line comes from the `.Error(e)` arm on line 17, with `check`'s message as `e`.
The second comes from the `.Panic(m)` arm on line 18: a panic's message ends with where it happened, so `m` ends with `at src/main.la:8:9`, the `panic` on line 8.
The third scope's task is fine, so its value is `Ok`, and line 15 prints `all done`.
