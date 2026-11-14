---
title: Derive blocks
start_error: E0415
---

Up to now a type met an interface by having its methods in its own `impl`.
A derive block instead says, in one place, how a type meets it.
Line 5 says how every `i64` meets `Describe`, and line 9 does the same for `string`.
`tell` on line 13 takes any `T: Describe`, so it can be called with either.
Press Run.

`lughac` gives E0415 on line 19.
A block's items don't become methods of `i64`, so they are reached only through a bound such as `tell`'s.
Change line 19 to `tell(5);`; Solve does it for you.
