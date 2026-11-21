---
title: impl Ord
start_output: [Version { major: 1, minor: 9 }, Version { major: 1, minor: 10 }, Version { major: 2, minor: 0 }]\nfalse\nfalse\n
---

`Ord` written by hand is one method, `cmp`, which gives back `Ordering.Less`, `Ordering.Equal` or `Ordering.Greater`.
`cmp` on line 4 orders versions by `major` alone, so 1.9 and 1.10 count as one release line, and `sort` on line 17 uses it, as do `<`, `<=`, `>` and `>=`.
`Version` gets `==` from `with Eq` on line 1, and lines 20 and 21 compare 1.9 and 1.10 both ways.
Press Run.

The program runs, after a warning on line 1, W0108: "`Version`'s `==` and `<` can disagree".
Its help says to write `impl Eq for Version` so that `==` compares what `cmp` compares.
Line 17 prints the sorted array.
Line 20 prints `false`, since the derived `==` compares `minor` too.
Line 21 prints `false`, since `cmp` finds neither less: `==` says the two differ, while `cmp` finds them equal.
Remove `with Eq` from line 1, and after line 1 add an `impl Eq for Version` block with `fun eq(self, other: Version): bool = self.major == other.major;`, then run again, or press Solve.
