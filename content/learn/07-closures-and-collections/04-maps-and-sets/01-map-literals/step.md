---
title: Map literals
---

A map holds values under keys, written `Map { key: value }`, and keeps its keys in the order they were added.
`ages` on line 2 is a `Map<string, i64>`.
`ages["ann"]` on line 3 reads a value, and line 4 adds a key by assigning to it.
Line 5 changes a value where it is, with `+=`.
An empty `Map {}` takes its type from where it's used, as `[]` does: on line 7, from the type written after `none_yet`.
A map prints through `.debug()`, as an array does.
Press Run.

Line 3 prints `31`.
Line 6 prints the map after lines 4 and 5: `"cy"` is added at the end, and `"bo"` is now `41`.
Line 8 prints the empty map.
