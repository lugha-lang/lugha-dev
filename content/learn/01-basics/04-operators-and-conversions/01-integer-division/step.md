---
title: Integer division
---

In the last lesson `height * 300` had to fit a `u8`, because arithmetic works on two numbers of the same type and gives that type.
So dividing two whole numbers gives a whole number, and line 2 prints `3`.
Press Run.

Line 3 prints `-3`: Lugha drops the fraction toward zero rather than rounding down.
`%` on line 4 takes its sign from the left side, giving `-1`.
The half survives only when both sides are floats, as on line 5.
