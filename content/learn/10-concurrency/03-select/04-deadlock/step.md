---
title: Deadlock
start_output: got 1\ngot 2\ngot 3\n
---

Without `after` or `default`, a `select` can wait forever, and so can a plain `recv`.
This `produce` from 10.2 has lost its `close`.
Press Run.

`main` takes the three values, then waits in `recv` on line 10 for a fourth, but `produce` has finished without closing the channel.
When no green thread can go on and none is sleeping, the program panics with "deadlock: every green thread is waiting" and exits with code 101.
Closing the channel once `produce` has sent everything gives `recv` its `None`, so the loop ends:


```lugha {5}
fun produce(c: Chan<i64>) {
    for i of range(1, 4) {
        c.send(i);
    }
    c.close();
}

fun main() {
    let c: Chan<i64> = Chan.new();
    spawn produce(c);
    while let Some(v) = c.recv() {
        println("got {v}");
    }
    println("done");
}
```

Add `c.close();` as line 5, or press Solve.
