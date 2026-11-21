---
title: Env
---

An `Env` reads the program's environment variables.
`get(name)` gives an `Option<string>`: `Some` with the value, or `None` when the variable isn't set (or can't be read as text), so `greeting` on line 1 matches on it, and line 11 prints what it gives.
Line 9 asks whether `PATH` is set, and line 10 asks for a variable nobody sets.
`env.only(["HOME"])` on line 12 gives a narrower `Env` that reads only `HOME`, and line 13 asks it for `PATH`.
Here the program runs with `PATH` set and `USER` not set.
Press Run.

So `greeting` takes its `None` arm, and through `narrow`, `PATH` looks unset.
