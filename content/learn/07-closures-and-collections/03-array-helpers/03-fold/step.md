---
title: fold
---

To turn a whole array into one value, use `fold`.
It starts from the value you give it, calls its closure with the result so far and each element in turn, left to right, and gives back the last result.
Line 3 starts from `0` and adds each number.
Line 4 starts from the first number and keeps the larger of the two each time.
Press Run.

Line 5 prints the sum, `22`, and line 6 the largest number, `9`.
