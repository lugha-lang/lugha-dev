---
title: Entropy and random numbers
---

An `Entropy` gives random bytes from the system: `entropy.bytes(16)` on line 4 is 16 of them, the kind to use for keys and tokens.
For ordinary random numbers, `import std.random;` on line 1 brings in the standard library's `random` module, used as `random.` on lines 6, 9 and 10 (Modules covers `import`), and `random.from_entropy(entropy)` on line 6 seeds a generator from the system.
`rng.between(1, 7)` on line 7 is a whole number from 1 up to 6, which can change from run to run, and `rng` is `let mut` because every `Rng` method takes `mut self`: each call moves it on.
`random.seeded(42)` on lines 9 and 10 seeds from a number instead: two generators with the same seed give the same numbers in the same order, so line 11 compares two equal rolls.
Press Run.
