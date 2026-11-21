---
title: any and all
---

`any` and `all` take the same kind of closure as `filter`, but give back one `bool`.
`any` on line 3 asks whether some age is under 18.
`all` on line 4 asks whether every age is under 18, and on line 5 whether every age is above `0`.
Press Run.

Line 3 prints `true`, because `17` is under 18.
Line 4 prints `false`, because `34` and `52` aren't.
Line 5 prints `true`, since every age is above `0`.
