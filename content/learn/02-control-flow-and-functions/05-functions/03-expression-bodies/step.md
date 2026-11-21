---
title: Expression bodies
---

A body that is a single expression can be written after `=` instead of between braces, as on line 1.
Press Run.

It prints `21` again: `= width * height;` means the same as a body in braces holding `width * height`.
Here the final `;` ends the declaration, so it doesn't throw the value away the way the `;` in step 2 did.
The return type, `: i64`, is still written in this form.
