---
title: Linked structures
---

`Node` on line 1 links to the next node through `Option<Ref<Node>>`: `None` at the end, or a box holding the next node.
Line 5 links `first` to the box `second`, and line 6 calls `set` on `second`.
Line 7 takes the box out of `first.next`, and line 8 prints the value of the node in it.
Press Run.

It prints `20`, because `first` holds the same box as `second`.
A plain `Option<Node>` would also compile, but `first` would then hold its own copy of the next node, and no later change to `second` would reach it.
