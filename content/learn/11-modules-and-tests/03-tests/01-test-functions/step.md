---
title: Test functions
---

A test is a function with `@test` on the line before it, as on line 3 of `test/shapes_test.la`.
It returns nothing, and takes no parameters here; Testing with capabilities shows the ones it may take, and a parameter of any other type is E0434.
`assert` on line 6 panics unless what it's given is true, and a panic fails the test.
The test file is in `test/`, outside `src`, so line 1 of `test/shapes_test.la` names the module with the package's name in front, `geometry.shapes`; `lugha.toml` gives the package that name.
Press Test.

The Tests tab names each test by its file's path, with `.` for `/` and no `.la`, then its own name: `test.shapes_test.area_of_three`.
