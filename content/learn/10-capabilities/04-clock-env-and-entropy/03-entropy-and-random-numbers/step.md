---
title: Entropy and random numbers
---

An `Entropy` gives random bytes from the system: `entropy.bytes(16)` on line 4 is 16 of them, the kind for keys and tokens.
For random numbers, line 1 imports `std.random`: an `import` makes a module, a named group of functions, usable in this file, here the standard library's `random`, which lines 6, 9 and 10 use as `random.`.
`random.from_entropy(entropy)` on line 6 makes a generator, an `Rng`, seeded from the system.
`rng.between(1, 7)` on line 7 is a whole number from 1 up to 6.
`rng` is `let mut` because every `Rng` method takes `mut self`: each call changes the generator, so the next call gives its next number.
`random.seeded(42)` on lines 9 and 10 seeds two generators from the same number instead.
Press Run.

`16` is the key's length, from line 5.
The first `true` is line 8: the roll is from 1 to 6.
The second is line 11: generators with the same seed give the same numbers in the same order, so the two rolls are equal.
