---
title: Format specifiers
---

A `:` after the expression in braces starts a format specifier, which changes how the value is written.
Line 3 prints `share` as it is, and line 4 adds `:.2`, which asks for two decimals.
Lines 5 to 8 use other specifiers on whole numbers.
Press Run.

Line 3 prints `0.6666666666666666`, and line 4 rounds it to `0.67`; a precision like `.2` works only on floats.
Lines 5 and 6 ask for a width of 6 characters, shown inside the square brackets: `>` puts `42` at the end of the six, and `<` at the start.
On line 7, the `0` before the width 3 pads `7` with zeros, giving `007`.
On line 8, `x` writes `255` in hex, and `#` puts `0x` in front: `0xff`.
