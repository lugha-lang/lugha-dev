# Full sweep: reading findings (2026-11-21)

Four readers, one per three chapters, read every lesson in `docs/content/v5`. Nothing was changed.
All line references, error codes, quoted messages, step titles and outputs were checked and are right,
and none of the lessons has questions to the learner, language comparisons, old syntax in prose, or cycle/GC claims.
Items marked ✔ I checked myself against the file.

## A. Errors: the text tells the learner something wrong (fix)

1. ✔ **4.1 step 2** (`4.1-structs.md:88`): "Add `y: 0` after `x: 3,` on line 4" — line 4 is `Point { x: 3 }`, no comma.
   → "Add `, y: 0` after `x: 3` on line 4, or press Solve."
2. ✔ **12.1 step 1** (`12.1-tasks-and-scopes.md:22`): never says what happens to old line 5, which no longer compiles once `t` is inside the scope.
   → "Replace lines 4 and 5 with `let r = scope s {`, then `let t = s.spawn(square(7));` and `t.join().unwrap()` inside it, a closing `};`, and `console.println(r.debug());`, or press Solve."
3. ✔ **1.4 step 3** (`1.4-operators-and-conversions.md:90`): "Write those on lines 3 and 4" — line 4 also needs `total.` and keeps `/ 7.0`.
   → "Write `total.truncate<u8>()` on line 3 and `total.round<f64>() / 7.0` on line 4, or press Solve, which also adds lines 5 and 6."
4. ✔ **2.5 step 1** (`2.5-functions.md:24`): "a function's parameter types and return type are always written", then the next line leaves the return type off.
   → "`lughac` works out a `let`'s type from its value, but a function's parameter types are always written, and so is its return type when it gives a value back."
5. **8.7 step 1** (`8.7-deriving.md:20`): "how numbers, strings and every struct get `Describe`" — the block covers only `i64`, and step 3 shows `f64` isn't covered.
   → "how `i64`s, strings and every struct get `Describe`".
6. **10.3 step 2** (`10.3-the-console.md:47`): "`console.stdout_only()` … passes it to `noisy`" — the call doesn't pass anything; line 8 does.
   → "Line 8 passes `noisy` a narrower `Console`, `console.stdout_only()`, whose `eprint` and `eprintln` do nothing and which has no input to read, while `console` itself still writes to both."
7. **10.4 step 1** (`10.4-clock-env-and-entropy.md:15`): "later than 14 November 2023" — 1700000000000 is 22:13 UTC that day.
   → "past mid-November 2023".

## B. Fix steps with a sentence after "or press Solve" (your rule)

Most fix steps add one sentence after the Solve sentence that explains the result (about 30, e.g. 1.1 s2, 4.3 s1, 6.2 s3).
Seven put a sentence there that the learner needs *before* making the change, so it reads out of order:
11.2 s3 (line 116), 12.1 s1 (line 23), 12.1 s5 (line 168), 12.3 s2 (line 68), 12.4 s2 (line 63), 12.5 s2 (line 66), 6.2 s3 (line 351, where "or press Solve" is attached to a description, not an instruction).
→ Recommended: move those seven above the instruction; leave the explaining-the-result ones as they are.

## C. Clarity (rewrites; each keeps the meaning)

- 1.4:52 "`as` comes before `/`" → "`as` is worked out before `/`".
- 1.4:87 "too large for an exact `f64`" → "too large for an `f64` to hold exactly".
- 1.4:88 "Methods do these conversions instead, the target type in `<…>`," → "…instead, with the target type in `<…>`,".
- 2.5:89 "means exactly the braces with `width * height` inside" → "means the same as a body in braces holding `width * height`".
- 3.1:345 "It needs no `Console`, so it can go anywhere, even inside an expression." → "It needs no `Console`, so any function can use it, and since it gives `x` back it can go inside an expression."
- 3.2:266 "compares code points" → "compares their Unicode numbers" (1.2's term).
- 4.3:77/79 E0468 on a bare variant name isn't explained until 4.5 → line 79: "…and line 11 gets E0468: a bare name that is one of `Shape`'s variants needs its dot."
- 4.5:171 two colons in a row → "E0501 says `n` is not mutable: names in a pattern are read-only, like parameters."
- 4.5:173 "copy" twice → "`mut` before the name in the pattern does that in one step, giving the arm its own copy to change."
- 6.3:78 one long instruction → split after "a closing `}`".
- 7.1:79 → "`Some`, `Ok` and `Err` are function values the same way, once a written function type says what they hold, as `wrap`'s type does on line 17."
- 7.4:130 → "…and both have `clear`, which empties them, as line 10 does for `ages`."
- 8.1:114 → "Line 1 implements `Display` for `bool`, so that `true` would print as `yes`; `Display` is the interface `console.println` prints through."
- 8.1:206 → "…and the help's `with Named` is E0462 here, since `with` needs derive blocks, which come in Deriving."
- 8.2:210 → "…but converting it to an interface `Loud` that `Dog` implements and `Pet` doesn't extend is E0422."
- 8.3:60 → "for an `i64[]` called `xs`, …".
- 8.5:51 "orders them in the order they're declared" → "orders by the fields, in the order they're declared".
- 8.7:140 "the last step puts it to use" → "derive.build, in step 8, puts it to use" (the lesson is split in two files).
- 9.1:18 "in for loops over ranges" → "the range `1..4` in Loops".
- 9.1:174 one sentence about two lines → split into the `char` quotes sentence and the `bytes()` sentence.
- 10.2:19 comma splice → "…and `append_file` on line 8 adds to the end. Each gives `Ok` with the number of bytes written."
- 10.2:91 "climbs out of the folder `dir` is" → "climbs out of `dir`'s folder".
- 10.2:130 "where step 3's paths" → "whereas step 3's paths".
- 10.6:19 "every method the interface gives no default" → "every method the interface doesn't give a default for".
- 12.1:61 run-on → "A task can be joined more than once: line 15 joins both again and adds their answers up as the body's value. Line 17 prints the scope's value, `Ok` with that sum."
- 12.1:96 "(here really: …)" → "(outside a test it really sleeps: virtual time is only for tests)".
- 12.2:63 "unless it's given a name" (naming a task is never shown) → "A task is named after the function it calls, so the first two are `check` and `crash`."
- 12.3:61 "as its saving" → "standing in for the saving".
- 12.4:19 → "Numbers and strings are `Sendable`, and so are arrays, structs and enums made of them."
- 12.7:147 "too" twice → "An actor's own panic fails its scope as well: …".

## D. Your call

- **Cross-references to other lessons** are written several ways ("In the last lesson", "as in Blocks and scopes", "it comes in 3.1"). Recommended: lesson titles everywhere; only 2.1:48 ("it comes in 3.1" → "it comes in Arrays") uses a number.
- **10.1:108 and 10.3:21** point learners to the Playground's input tab. The Playground still runs m159 with `args()` help. Keep them for the switch PRP, which brings the Playground to v18.
- **11.4:23** "a program on this site is the package `playground`, so its tests' names start `playground.main.`" — true for tests in `src`; 11.3's `test/` tests are named by path (`test.shapes_test.…`). A learner may expect `geometry.` there. Could add: "Tests in `test/` are named by their path instead, as in Tests."
- **11.4:162** "a plain test" is never defined (integration tests aren't in the course) → "a test runs on virtual time".
- **12.4 step 2**: its objective says a channel or actor shares for many tasks; the step teaches returning answers and mentions channels/actors only in its last sentence.
- **8.7 obj 2** says "only through the interface"; the step says "through the interface", since `5.describe()` works at m239 against the spec (already in the ../lugha notes).
- **1.2:50** introduces `bool` in the floats step; fine as the one place it's introduced, or move it to 1.4 step 6.
- **2.2:48** "its notes say" vs the Kind line's "labels": use the word the output pane uses.
- **5.1:118** "a parameter written without `mut`" before `mut` parameters (5.2); the notes say this was chosen.
- **5.4:301** "holds an array or a box": the spec counts strings too; could add "a string".
- **12.2 step 2** imports `std.task` without using it; removing it shifts every line ref and needs a rerun. Recommended: leave it.
- **3.2:244** says the bytes aren't printed because they aren't valid UTF-8; really it's the site's runner. Fine as is?
- **6.4:282** E0456's help mentions `fs.remove_file`, files come in chapter 10; could add a sentence.

## E. For ../lugha (no lesson change)

- E0429's help still offers `exit(…)` (4.5 Kind line), which is gone (E0471).
- E0404's help for `count + 1` talks about comparing boxes (5.3).
- Joins the lesson-notes list already collected (Clock.local_offset, last Sender, `with Key` beside `impl Eq`, `5.describe()`, stale E0452/E0313 helps, "panicked" vs "failed", E0439 vs E0475, select order, `<fun>` debug, skill mut-param line).
- 6.3 step 3 needs m239+ on the visitors' sandbox (part of the switch PRP).
