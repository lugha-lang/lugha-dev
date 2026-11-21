---
title: Derive blocks
---

A derive block says, in one place, how a type gets an interface's items.
Line 5 says how every `i64` gets `Describe`, and line 9 does the same for `string`.
`tell` on line 13 takes any `T: Describe`, so lines 16 and 17 call it with either.
A block's items are reached through the interface: through a bound such as `tell`'s, or by naming it, as `Describe.describe(7)` on line 18 does.
Press Run.
