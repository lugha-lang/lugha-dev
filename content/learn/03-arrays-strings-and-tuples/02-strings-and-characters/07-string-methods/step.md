---
title: String methods
---

Most work on a string goes through its methods.
Line 3 takes the spaces off both ends with `trim`, then cuts the result at each comma with `split`, which gives a `string[]`.
`join` on line 5 puts an array of strings back together, with `" + "` between them.
`contains` on line 6 and `starts_with` on line 7 each give a `bool`, and `lines` on line 8 splits a string at each `\n`.
Press Run.

Line 4 prints the three items, `["milk", "bread", "eggs"]`, and line 5 prints `milk + bread + eggs`.
Lines 6 and 7 print `true`.
None of these methods changes the string it's called on: `line` still has its spaces on line 7, so it's trimmed again there.
Line 8 prints `["one", "two"]`.
