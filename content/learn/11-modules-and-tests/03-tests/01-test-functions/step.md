---
title: Test functions
---

A test is a function with `@test` on the line before it, as on line 3 of `test/shapes_test.la`.
This one takes no parameters and returns nothing.
`assert` on line 6 panics unless what it's given is true, and a panic fails the test.
A file outside `src`, such as this one in `test/`, names the package's modules with the package's name in front.
`lugha.toml` names the package `geometry`, so line 1 imports `geometry.shapes`.
The Test button runs a package's tests and shows their results in the Tests tab.
Press Test.

The Tests tab has a line for the test, then a count.
The test is named by its file's path, with `.` for `/` and no `.la`, then the function's own name: `test.shapes_test.area_of_three`.
`ok` after it means it passed, and the last line counts 1 test, 1 passed and 0 failed.
