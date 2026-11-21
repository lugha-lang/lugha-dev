---
title: Interface declaration
---

An interface names a set of methods that different types can share.
`Shape` on lines 1 to 4 lists two, with their signatures and no bodies.
`Circle` implements it with `impl Shape for Circle` on lines 8 to 11, which gives each method its body, and line 15 calls them with a dot, like the methods in Methods.
An interface's methods can use `Self` for the type that implements it, as in `fun bigger(self, other: Self): bool`.
Press Run.
