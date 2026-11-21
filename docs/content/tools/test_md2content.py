"""Tests for md2content: run with `python3 -m unittest discover docs/content/tools`."""
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(__file__))
import md2content as m  # noqa: E402

LESSON = '''# 9.9 A lesson (v5, Lugha v18)

## Objectives

1. **First** *(new)*: something.

---

## Step 1: First thing
Kind: read

Some text, with `code`.
Press Run.

It prints `1`.

```lugha
fun main(console: Console) {
    console.println(1);
}
```

Output:

```text
1
```

## Step 2: A fix
Kind: fix (start gives E0301 "cannot find `x` in this scope")

Line 2 uses `x`.
Press Run.

Change it, or press Solve.

Start:

```lugha
fun main(console: Console) {
    console.println(x);
}
```

Solution:

```lugha
fun main(console: Console) {
    console.println(2);
}
```

Output (solution):

```text
2
```

## Notes

- Notes are not converted.
'''


class Slug(unittest.TestCase):
    def test_words(self):
        self.assertEqual(m.slug("for … of loops"), "for-of-loops")
        self.assertEqual(m.slug("assert_eq and assert_ne"), "assert-eq-and-assert-ne")
        self.assertEqual(m.slug("derive.all and derive.fold"), "derive-all-and-derive-fold")
        self.assertEqual(m.slug("Results can't be ignored"), "results-cant-be-ignored")


class Kind(unittest.TestCase):
    def test_read(self):
        k = m.parse_kind("read")
        self.assertEqual((k.fix, k.test, k.error, k.failing), (False, False, None, []))

    def test_read_with_tests(self):
        self.assertTrue(m.parse_kind("read (Test)").test)

    def test_error(self):
        self.assertEqual(m.parse_kind('fix (start gives E0471 "x")').error, "E0471")

    def test_error_after_a_warning(self):
        k = m.parse_kind('fix (start gives warning W0106 "a" and E0422 "b")')
        self.assertEqual(k.error, "E0422")

    def test_prints(self):
        k = m.parse_kind('fix (start prints "checking the input" and exits 1)')
        self.assertEqual((k.fix, k.error, k.prints), (True, None, True))

    def test_silent_panic(self):
        k = m.parse_kind("fix (start panics: stderr `panic: stack overflow`, exit 101, no stdout)")
        self.assertEqual((k.prints, k.silent), (True, True))

    def test_failing(self):
        k = m.parse_kind('fix (Test: `afternoon` fails with "x" at line 20)')
        self.assertEqual((k.test, k.failing), (True, ["afternoon"]))

    def test_unknown(self):
        with self.assertRaises(m.ConvertError):
            m.parse_kind("quiz")


class Steps(unittest.TestCase):
    def setUp(self):
        self.lesson = m.parse_lesson("9.9-a-lesson.md", LESSON)

    def test_titles(self):
        self.assertEqual(self.lesson.title, "A lesson")
        self.assertEqual([s.title for s in self.lesson.steps], ["First thing", "A fix"])

    def test_prose_stops_at_the_code(self):
        self.assertEqual(self.lesson.steps[0].prose, "Some text, with `code`.\nPress Run.\n\nIt prints `1`.")

    def test_read_step(self):
        st = m.convert_step(self.lesson, self.lesson.steps[0], {})
        self.assertIn("console.println(1);", st.start["src/main.la"])
        self.assertIsNone(st.solution)
        self.assertEqual(st.expected, "1\n")

    def test_fix_step(self):
        st = m.convert_step(self.lesson, self.lesson.steps[1], {})
        self.assertIn("println(x)", st.start["src/main.la"])
        self.assertIn("println(2)", st.solution["src/main.la"])
        self.assertEqual((st.front["start_error"], st.expected), ("E0301", "2\n"))

    def test_error_note(self):
        noted = LESSON.replace("Change it, or press Solve.\n", "Change it, or press Solve.\n\nError note: `x` was never declared.\n")
        lesson = m.parse_lesson("9.9-a-lesson.md", noted)
        st = m.convert_step(lesson, lesson.steps[1], {})
        self.assertEqual(st.front["error_note"], "`x` was never declared.")
        self.assertNotIn("Error note", st.text)

    def test_error_note_needs_a_start_error(self):
        noted = LESSON.replace("It prints `1`.\n", "It prints `1`.\n\nError note: none here.\n")
        lesson = m.parse_lesson("9.9-a-lesson.md", noted)
        with self.assertRaises(m.ConvertError):
            m.convert_step(lesson, lesson.steps[0], {})

    def test_stray_text_stops_it(self):
        bad = LESSON.replace("Output:\n", "A stray sentence.\n\nOutput:\n")
        lesson = m.parse_lesson("9.9-a-lesson.md", bad)
        with self.assertRaises(m.ConvertError):
            m.convert_step(lesson, lesson.steps[0], {})


class Files(unittest.TestCase):
    def test_paths_and_roles(self):
        self.assertEqual(m.label_role("Start, `src/main.la`:"), ("start", "src/main.la", None, None))
        self.assertEqual(m.label_role("`src/shapes.la` (start and solution):"), ("both", "src/shapes.la", None, None))
        self.assertEqual(m.label_role("`lugha.toml`:"), ("both", "lugha.toml", None, None))
        self.assertEqual(m.label_role("Start, the test (lines 18 to 21):"), ("start", "src/main.la", 18, None))
        self.assertEqual(m.label_role("Lines 1 to 17 (start and solution):"), ("both", "src/main.la", 1, None))
        self.assertEqual(
            m.label_role("`src/main.la` (`src/shapes.la` as in step 1):"),
            ("both", "src/main.la", None, ("src/shapes.la", 1)),
        )

    def test_split_blocks_join_in_line_order(self):
        code = m.join_pieces([(18, "@test\nfun t() {}\n"), (1, "fun a() {}\n\n")])
        self.assertEqual(code.split("\n")[17], "@test")


class Imports(unittest.TestCase):
    def test_keeps_only_what_is_imported(self):
        files = {
            "src/main.la": "import range;\n",
            "src/range.la": "import geo.square;\n",
            "src/geo/square.la": "",
            "src/shapes.la": "",
            "lugha.toml": "",
        }
        kept = m.imported(files, {"src/main.la"})
        self.assertEqual(sorted(kept), ["lugha.toml", "src/geo/square.la", "src/main.la", "src/range.la"])


class Diagram(unittest.TestCase):
    def test_line_becomes_a_block(self):
        text, svg = m.diagrams('Before:\n\nDiagram: v4\'s `diagram.svg`, kept (alt "a box").\n\nAfter.')
        self.assertIn('```diagram\nfile = "diagram.svg"\nalt = "a box"\n```', text)
        self.assertEqual(svg, ["diagram.svg"])


class Writing(unittest.TestCase):
    def test_writes_a_step_folder(self):
        lesson = m.parse_lesson("9.9-a-lesson.md", LESSON)
        st = m.convert_step(lesson, lesson.steps[1], {})
        with tempfile.TemporaryDirectory() as d:
            m.write_step(d, st, None)
            md = open(os.path.join(d, "step.md")).read()
            self.assertTrue(md.startswith("---\ntitle: A fix\nstart_error: E0301\n---\n\nLine 2 uses `x`."))
            self.assertTrue(os.path.exists(os.path.join(d, "start/src/main.la")))
            self.assertTrue(os.path.exists(os.path.join(d, "solution/src/main.la")))
            self.assertEqual(open(os.path.join(d, "expected.txt")).read(), "2\n")


if __name__ == "__main__":
    unittest.main()
