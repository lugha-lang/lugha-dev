---
title: Env
---

An `Env` reads the program's environment variables, the named settings a program is started with.
`get(name)` gives an `Option<string>`: `Some` with the value, or `None` when the variable isn't set or can't be read as text.
Line 9 asks whether `PATH` is set, and line 10 asks for a variable nobody sets.
`greeting` on line 1 matches on `env.get("USER")`, and line 11 prints what it gives.
`env.only(["HOME"])` on line 12 gives a narrower `Env` that reads only `HOME`, and line 13 asks it for `PATH`.
Here the program runs with `PATH` set and `USER` not set.
Press Run.

`true` is line 9: `PATH` is set.
`None` is line 10.
`USER` isn't set, so `greeting` takes its `None` arm.
The last `None` is line 13: through `narrow`, every variable but `HOME` looks unset, `PATH` too.
