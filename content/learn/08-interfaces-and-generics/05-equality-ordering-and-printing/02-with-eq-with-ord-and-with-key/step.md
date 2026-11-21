---
title: with Eq, with Ord and with Key
---

`with` after a declaration asks for an interface built from the fields.
`with Eq` compares them, `with Ord` orders by the fields, in the order they're declared, and `with Key` hashes them so the type can be a map key or a set value.
`Ord` and `Key` both extend `Eq`, so `Version` on line 1 has `==` too, and so does `Tag` on line 2.
Line 6 prints a sorted copy and leaves `versions` as it was.
Line 7 compares two versions with `<`, line 8 checks one for equality, and line 9 puts two equal tags in a set.
Press Run.

`major` is declared first, so it decides first: 1.9 and 1.10 sort before 2.0.
Between those two, `minor` decides, and 9 comes before 10.
The set on line 9 keeps one of the two equal tags.
