---
title: Net
---

A `Net` reaches the network: `net.connect("example.com:80")` on line 2 opens a connection to a host and port, and gives `Ok(Conn)` or an `Err`.
The programs on this site run without a network.
Press Run.

So the connection is an `Err`, and line 4 prints it after `can't connect:`: the system's own message, saying the name `example.com` couldn't be looked up.
