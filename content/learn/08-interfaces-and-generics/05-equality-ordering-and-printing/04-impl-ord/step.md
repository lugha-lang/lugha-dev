---
title: impl Ord
start_output: [Version { major: 1, minor: 9 }, Version { major: 1, minor: 10 }, Version { major: 2, minor: 0 }]\nfalse\nfalse\n
---

`Ord` written by hand is one method, `cmp`, which gives back `Ordering.Less`, `Ordering.Equal` or `Ordering.Greater`.
`cmp` on line 4 orders versions by `major` alone, so 1.9 and 1.10 count as one release line, and `sort` on line 17 uses it, as do `<`, `<=`, `>` and `>=`.
`Version` gets `==` from `with Eq` on line 1, and lines 20 and 21 compare 1.9 and 1.10 both ways.
Press Run.

It runs, with W0108: "`Version`'s `==` and `<` can disagree".
Line 20 prints `false`, since the derived `==` compares `minor` too, and line 21 `false`, since `cmp` finds neither less: the two are neither equal nor ordered.
As the help says, write `Eq` to compare what `cmp` compares.
Remove `with Eq` from line 1, and after it add an `impl Eq for Version` block with `fun eq(self, other: Version): bool = self.major == other.major;`, or press Solve.
