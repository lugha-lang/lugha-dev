---
title: Integer division
---

In the last lesson `height * 300` had to fit a `u8`, because arithmetic works on two numbers of the same type and gives that type.
So dividing two whole numbers gives a whole number.
Lines 2 and 3 divide whole numbers with `/`, and line 4 takes a remainder with `%`.
Line 5 divides two floats.
Press Run.

Line 2 prints `3`, without the half.
Line 3 prints `-3`: the fraction is dropped toward zero, not rounded down.
Line 4 prints `-1`, since a remainder takes its sign from the left side.
Line 5 prints `3.5`: the half is kept only when both sides are floats.
