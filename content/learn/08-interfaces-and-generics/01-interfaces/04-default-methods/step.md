---
title: Default methods
---

An interface can give a method a body, which is then its default.
`describe` on line 3 has one, and it calls `area` on `self`.
`Circle`'s `impl` on lines 9 to 11 has no `describe`, so line 19 uses the default.
`Square`'s `impl` writes its own on line 15, which line 20 calls.
Press Run.
