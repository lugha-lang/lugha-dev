---
title: impl Display
---

`console.println` and `"{x}"` print a value through `Display`, one method, `fun show(self): string`.
`impl Display for Version` on lines 3 to 5 shows a version as `v1.10`.
Line 9 prints one, and line 10 puts one in a string.
Line 11 prints an array of versions through `.debug()`.
Press Run.

A debug form never uses `Display`: the array on line 11 shows each `Version` with its fields.
