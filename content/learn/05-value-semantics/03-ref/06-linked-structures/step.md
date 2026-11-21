---
title: Linked structures
---

`Node` on line 1 links to the next node through its `next` field, an `Option<Ref<Node>>`: `None` at the end, or a box holding the next node.
Line 4 makes `second`, a box holding a node, and line 5 makes `first`, with that box as its `next`.
Line 6 then puts a new node, with value `20`, in `second` with `set`.
Line 7 takes the box out of `first.next`, and line 8 prints the value of the node in it.
Press Run.

It prints `20`, because `first.next` holds the same box as `second`.
A plain `Option<Node>` would also compile, but `first` would then hold its own copy of the next node, and the change on line 6 wouldn't reach it.
