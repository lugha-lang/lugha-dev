---
title: Starting an actor
---

An actor starts in a scope, as a task does: `main` takes the root scope on line 11, and line 12 starts a `Counter` in it with `root.spawn`.
Line 13 copies the handle into `d`, and line 14 sends `add(5)` through the copy.
Press Run.

Copies of a handle reach the same actor, so `d.add(5)` shows up in `c.get()` on line 15.
