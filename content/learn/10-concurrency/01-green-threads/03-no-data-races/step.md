---
title: No data races
---

This time both threads share one `Ref` box, and line 5 adds 1 to it 1000 times in each.
Press Run.

Only one green thread runs at any instant, so there are no data races: two threads never touch `total` at once.
A thread is switched out when it waits, and also after 4096 function calls and loop turns, so a long loop can't keep the others waiting.
That switch can fall between reading a value and writing it back.
Had line 5 read the total, yielded, then set it, both threads would often read the same value, and the program would print 1000.
Sharing one OS thread also means green threads never use two cores at once.
