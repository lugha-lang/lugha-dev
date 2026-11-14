---
title: Starting an actor
start_error: E0439
---

Step 1 started `Counter` from a literal, but an associated function can make the state too: `new` on line 4 returns `Self`, the actor's state.
Line 14 calls it without `spawn`.
Press Run.

That's E0439: the state exists only inside the actor, so it has to be started with `spawn`.
The E0501 on line 16 comes from the same mistake: without `spawn`, `d` is a plain value.
Calling `add` on it would need `let mut`, which a handle's `mut self` methods don't.
Copies of a handle, like `d` on line 15, reach the same actor, so `d.add(5)` shows up in `c.get()`.
The fixed `main.la`:


```lugha {14}
actor Counter {
    count: i64,

    fun new(start: i64): Self = Self { count: start };

    fun add(mut self, n: i64) {
        self.count += n;
    }

    fun get(self): i64 = self.count;
}

fun main() {
    let c = spawn Counter.new(10);
    let d = c;
    d.add(5);
    println(c.get());
}
```

Add `spawn` before `Counter.new(10)` on line 14; Solve does it for you.
