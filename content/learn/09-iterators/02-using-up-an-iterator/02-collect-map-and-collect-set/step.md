---
title: collect_map and collect_set
---

An iterator can end in a set or a map instead of an array.
`collect_set()` on line 3 keeps each name once, in the order first seen.
`collect_map()` on line 5 needs tuples of key and value, and when a key comes twice, it keeps its first place and its later value wins.
Press Run.
