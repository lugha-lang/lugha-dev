---
title: collect_map and collect_set
---

An iterator can end in a set or a map instead of an array.
`collect_set()` on line 3 keeps each name once, in the order first seen.
`collect_map()` on line 5 needs tuples of a key and a value, as `scores` on line 4 holds.
Press Run.

The set holds `"ann"` once, then `"bo"`.
In the map, `"ann"` comes twice: it keeps its first place, and its later value, `3`, wins.
