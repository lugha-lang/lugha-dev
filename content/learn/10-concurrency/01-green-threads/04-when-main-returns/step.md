---
title: When main returns
start_output: work: started\nmain: done\n
---

`work` sets a `defer` on line 4, prints, and sleeps for 100 milliseconds on line 6.
`task.yield_now()` on line 11 lets `work` start before `main` goes on.
Press Run.

"work: cleaned up" never prints.
When `main` returns, the program exits with `main`'s code, and green threads still running are dropped without running their defers.
So `main` has to `join` a thread it needs finished.
A panic in any green thread ends the program too, with exit code 101.
The fixed `main.la`:


```lugha {13}
import std.task;

fun work() {
    defer println("work: cleaned up");
    println("work: started");
    task.sleep(100);
}

fun main() {
    let t = spawn work();
    task.yield_now();
    println("main: done");
    t.join();
}
```

Add `t.join();` as line 13, or press Solve.
