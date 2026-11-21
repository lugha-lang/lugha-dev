---
title: Updating a box
start_error: E0404
error_note: `+` works on numbers, and `count` is a box holding one, a `Ref<i64>`. Take the number out with `get`, or change it with `update`.
---

Line 5 tries to add `1` to `count` and put the result back in the box with `set`.
Press Run.

The program doesn't run, because `count` is the box, not the number in it.
E0404 says `+` can't be applied to `Ref<i64>` and `i64`: `Ref<i64>` is a box holding an `i64`, and `+` needs the `i64` inside.
The help under it is about comparing boxes, which line 5 doesn't do.
`count.set(count.get() + 1)` would work, and `update` does it in one call.
It takes a function that gets an `i64` and returns one, calls it with what's in the box, and puts back what it returns.
`add_one` on line 1 is such a function, and `update` takes it by name: `add_one(0)` would call it, but `add_one` alone hands over the function.
Write `count.update(add_one)` on line 5 and run again, or press Solve.
