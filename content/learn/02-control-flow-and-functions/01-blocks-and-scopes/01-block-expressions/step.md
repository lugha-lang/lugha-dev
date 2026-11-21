---
title: Block expressions
---

In the first lesson, the last line of `main`, a value written without a `;`, was what `main` gave back.
Any block in braces works the same way.
Lines 2 to 6 are a block that declares `price` and `tax`, and the block's value goes into `total`.
Press Run.

Line 7 prints `46`.
A block's value is its last expression, written without a `;`, here `price + tax` on line 5.
An expression is any code that gives a value, such as `40` or `price + tax`.
