---
title: Ref boxes
---

A `Ref` is a box: a place that holds one value, read with `get` and replaced with `set`.
`Ref.new(1)` on line 2 makes a box holding `1`, and `a` names it.
Line 3 copies `a` into `b`, line 4 calls `set(5)` on `b`, and line 5 prints `a.get()`.
Press Run.

It prints `5`, though line 4 called `set` on `b`.
Copying a `Ref` copies only a handle to the box, not the box itself, so `a` and `b` name the same box:

```diagram
file = "diagram.svg"
alt = "a and b both point at one box, which holds 5"
```

Every other value you have met so far gives you a copy of your own when you copy it.
