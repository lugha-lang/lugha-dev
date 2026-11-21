---
title: Package visibility
---

Without `private`, an item is visible in every module of its package, not only its own.
A package is what a `lugha.toml` describes: this one, in the file list, names the package `geometry`, and both `.la` files belong to it.
A program without a `lugha.toml` is one package too.
So `src/main.la` can build a `shapes.Square` on line 4, read its `side` field on line 5 and call `shapes.area` on line 6.
Press Run.

The output panel shows `3.0`, the `side` that line 5 reads, then `9.0` from `shapes.area` on line 6.
