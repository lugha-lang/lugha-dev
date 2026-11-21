---
title: Expression bodies
---

A body that is a single expression can be written after `=` instead of between braces, as on line 1.
Press Run.

It prints `21` again, because `= width * height;` means the same as a body in braces holding `width * height`.
Its final `;` ends the declaration, so it doesn't throw the value away the way the `;` in step 2 did.
The return type is still written in this form.
