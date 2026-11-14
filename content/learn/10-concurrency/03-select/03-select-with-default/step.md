---
title: select with default
---

An `after` arm still waits up to its limit.
A `default` arm runs when no other arm can go on at once, so a `select` with one never waits.
Arms can send too: `c.send(i)` on line 5 goes on when this channel has room.
Press Run.

The channel holds one value, so the first send is queued and the next two fall to `default` on line 6.
A `select` can't have both `after` and `default`, because with `default` it never waits long enough for `after` to fire, so `lughac` gives E0438.
