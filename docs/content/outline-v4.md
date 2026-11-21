# The course outline (v4)

Built from a full read of `lughac spec` (Lugha v17, sections 1–7 and the example programs in 10).
`[Lnnn]` points at the spec's lines (the copy printed by the pinned `lughac spec`), so every
objective can be checked. v3 is in `outline-v3.md`.

For programmers new to Lugha: they know what a variable, a loop and a struct are.

**Titles.** Each lesson is a numbered list of steps, one per objective, and each step has its
title here before it's drafted. A title is a heading a programmer would look for in a reference:
it names the feature (Function declaration, Shadowing, Match guards), not what the learner does
with it (Declare a function), and never describes the step. A step teaches what its title promises, and a lesson holds only steps its
own title covers. An objective never moves to another lesson without this file changing first,
and every change is checked against both rules.

**Order.** Every step relies only on steps before it. Something may *appear* before it's taught
when a programmer can read it without a lesson (an array printed in Hello, world), but no step may
*rely* on understanding it. The dependency check at the end lists, for each lesson, every earlier
lesson one of its steps uses.

Status: **on the site** (approved and live), **approved** (converted, on a branch), or **to write**.
A step marked *(new)* or *(moved)* changes an approved lesson.

---

## 1. Basics

### 1.1 Hello, world (on the site)
1. **The main function**: write `fun main()` and print with `println`. [L1417]
2. **Semicolons**: every statement ends with `;`, since newlines mean nothing. [L279]
3. **Comments**: `//`, `/* … */` (they nest) and `/** … */`. [L279–285]
4. **Exit codes**: `fun main(): i32`, the only other form of `main`. [L1417]

### 1.2 Values and types (on the site)
1. **Integer types**: the integer types `i8 … i64`, `u8 … u64`, and their `MIN` and `MAX`. [L526–540]
2. **Floating-point types**: `f32` and `f64`, and a float always prints with a `.`. [L1124]
3. **Integer literals**: `1_000_000`, `0xFF`, `0b1010`, `0o600`; a leading zero is still decimal (W0107). [L300–313]
4. **Float literals**: `2e5` is an error (E0107); write `2.0e5`. [L314]
5. **Characters and strings**: `'a'`, `"text\n"`, and a string can't span lines. [L321, L717]

### 1.3 Variables (on the site)
1. **Variable declaration**: `let`, with the type worked out or written after a colon. [L420, L672–676]
2. **Mutable variables**: `let mut`, and E0501 without it. [L251, L872]
3. **Assignment** *(moved from 2.1)*: assignment is a statement with no value, so `a = b = 0` is E0204. [L490]
4. **Number literal types**: from what's around it, else `i64` or `f64`; a number that doesn't fit is a compile error. [L676–678]
5. **Shadowing**: a second `let`, and `let x = x + 1;` reads the outer `x`. [L979]
6. **Constants**: `const NAME: T = value;`, and no mutable globals. [L1130]

### 1.4 Operators and conversions (on the site)
1. **Integer division**: same-type arithmetic, integer division, `%` takes the left side's sign. [L693, L893]
2. **Conversion with as**: `let e: f64 = 5` and `total / 2.0` are refused; convert with `as`. [L678, L686, L724]
3. **Lossy conversions**: truncation, saturation. [L724]
4. **Integer overflow**: `integer overflow`, exit 101; it never wraps. [L893]
5. **Comparison and logical operators**: `&&`, `||`, `!`, and `a < b < c` is E0203. [L470–488, L695–698]

---

## 2. Control flow and functions

Control flow comes first: its lessons need only `main`. Functions come after, so returning early,
returning from a loop and recursion can use `if` and loops.

### 2.1 Blocks and scopes (approved)
1. **Block expressions**: its last expression without `;`. [L987]
2. **Statements and ()**: a `;` throws the value away, and the block gives `()`. [L545, L1049]
3. **Variable scope**: at the `}` of its block (E0301 after it). [L987]

### 2.2 if (approved)
1. **if expressions**: `if` / `else if` / `else` as an expression. [L981]
2. **Branch types**: E0403. [L981]
3. **Boolean conditions**: a number is never read as one (E0403). [L981]
4. **Braces and parentheses**: parentheses optional, braces required (E0201). [L361, L424]

### 2.3 match (approved)
1. **match expressions**: arms, `_`, and arms of one type. [L636]
2. **Or-patterns**: `6 | 7 =>`. [L642]
3. **Exhaustiveness**: E0417; strings and integers need `_`, a `bool` doesn't. [L638]
4. **Match guards**: `_ if n < 0 =>`, and a guarded arm doesn't count toward covering. [L636, L638]
5. **Unreachable arms**: W0102. [L640]

### 2.4 Loops (approved)
1. **while loops**: `while`. [L989]
2. **for loops over ranges**: `for i in a..b`, `b` excluded. [L996]
3. **break and continue**. [L1037]
4. **loop and break with a value**: `loop` and `break value`; E0514 out of `while` or `for`. [L1033]
5. **Loop labels**: labels, `break outer;`, `continue outer;`. [L1035]

### 2.5 Functions (approved)
1. **Function declaration**: typed parameters and a return type, which are always written; order in a file doesn't matter. [L1379, L1132, L672–676]
2. **Return values**: a trailing `;` is E0503. [L1049]
3. **Expression bodies**. [L1383]
4. **Immutable parameters**: E0501, `let mut n = n;`. [L1400]
5. **No overloading**: no overloading or defaults (E0302). [L1403]

### 2.6 Return and recursion (drafted from approved steps, in review)
1. **Early return** *(new, split from the if lesson's step 5)*: `return` ends a function and gives back a value. [L1407]
2. **Return checking** *(moved from if)*: an `if` without `else` never counts as returning (E0503). [L1407–1415]
3. **Returning from a loop** *(moved from Loops)*: `while true` never counts; `loop` does. [L1407–1415]
4. **Recursion** *(moved from if)*: recursion, and the branch that stops it. [L1402]

---

## 3. Arrays, strings and tuples

### 3.1 Arrays (drafted)
1. **Array literals**: `[1, 2, 3]`, `[0; 10]`, and `.len`. [L645–648]
2. **Indexing**: `xs[i]`, and writing needs `let mut`. [L645, L872]
3. **Bounds checking**: the program stops with the length and the index. [L645]
4. **push and clear**: `push` and `clear`. [L739–745]
5. **Empty arrays**: `let xs: i64[] = [];`. [L647]
6. **for … of loops**: `for x of xs`; `in` is for ranges only (parse error). [L1010, L427]
7. **Changing elements in a loop**: `for x of mut xs`. [L1010, L1012]
8. **Array concatenation and equality**: `+` and `==`. [L650, L704]

### 3.2 Strings and characters (drafted; replaces "Text" on the site)
1. **String interpolation**: `{expr}`. [L323]
2. **Format specifiers**: `{x:.2}`, `{n:>6}`, `{n:05}`, `{n:#x}`. [L1109–1118]
3. **Escaping braces**: `{{`. [L323]
4. **String concatenation**: `+`, which won't take a string and a number. [L670, L694]
5. **String length**: `.len` counts bytes, `char_count()` characters. [L670]
6. **Bytes**: `s[i]` is a `u8`, `for b of s`. [L720, L1017]
7. **String methods**: `split`, `lines`, `trim`, `contains`, `starts_with`, `join`. [L760–771]
8. **Slicing**: byte offsets, which can cut a character in half. [L768]
9. **The char type**: comparisons, `is_digit()`, `to_upper()`, ASCII and Latin-1 only. [L717–721]

### 3.3 Tuples and destructuring (drafted)
1. **Tuples**: `(1, "a")` and `t.0`. [L906]
2. **Multiple return values**. [L906]
3. **Destructuring with let**: `let (q, r) = …`, and `let (mut x, mut y)`, not `let mut (x, y)`. [L907–908]
4. **Destructuring in loops**: `for (name, age) of people`. [L907]
5. **Tuple patterns**: tuple patterns. [L908]

---

## 4. Structs and enums

### 4.1 Structs (approved; replaces "A struct of your own")
1. **Struct declaration**. [L563]
2. **Printing structs**. [L1090]
3. **Struct literals**: E0413. [L563]
4. **Field assignment**: needs `let mut` on the variable. [L872]
5. **Struct update syntax**: `Point { x: 1, ..p }`. [L563]
6. **Struct literals in conditions**: parentheses (E0205). [L492]

### 4.2 Methods (approved)
1. **Methods**: `self`. [L728–731]
2. **mut self methods**: `mut self`. [L728–731]
3. **Associated functions and Self**: associated functions, `Vec2.new(1.0, 2.0)`, and `Self`. [L732, L822]
4. **Passing a value to its own mut method**: `v.add(v)` is E0508; copy first. [L733]

### 4.3 Enums (approved)
1. **Enum declaration**: variants with data, `Shape.Circle(2.0)`; `Shape::Circle` is E0207. [L565, L357]
2. **Matching on enums**: bind its data, cover every variant. [L636–641]
3. **Recursive enums**: a recursive enum needs no box. [L567]

### 4.4 Option (approved)
1. **Option instead of null**: no null; `Option`, `Some`, `None`. [L239, L559, L569]
2. **Matching on Option**. [L569]
3. **Typing None**: E0412. [L569]
4. **unwrap_or, is_some and is_none**: and `is_some`, `is_none`. [L772–785]
5. **Parsing numbers**: `parse_i64`. [L772–785]
6. **pop**. [L739–745]
7. **Checked arithmetic**: `checked_add`. [L949–961]

### 4.5 if let, while let and let else (approved; was "More patterns")
1. **if let**. [L991–992]
2. **while let**: `while let`. [L993]
3. **let else**. [L994]
4. **Nested patterns**: nested patterns. [L636]
5. **mut bindings**: `mut` bindings. [L643]
6. **Variants and bindings**: at the top of a `match` on an enum a name is a variant; a misspelled one inside a variant becomes a binding (W0103). [L641, L994]

---

## 5. Value semantics

### 5.1 Copies (approved; on the site as "Everything is a value")
1. **Copies**: assigning gives an independent copy. [L547]
2. **Mutable copies**. [L547]
3. **Copying arrays**. [L547]
4. **Passing by value**: and return what they changed. [L1401]
5. **Quiz** (quiz).
6. **Copy-on-write** *(new, an objective without a step)*: copy-on-write. [L652, L1450]

### 5.2 Ref (approved; on the site as "Sharing on purpose")
1. **Ref boxes**: `Ref.new`, `get`. [L571–582]
2. **set without mut**: `set`. [L582]
3. **get returns a copy**: `get` gives a copy. [L582]
4. **Updating a box**: `update` with a function passed by name, which gets the contents and returns the new ones; `count + 1` on a box is E0404. [L578, L583] (owner, 2026-11-14)
5. **Identity with is** *(new)*: `==` is E0404. [L583]
6. **Linked structures** *(new)*: `Option<Ref<Node>>`. [L584]

### 5.3 Memory and safety (approved; was "What Lugha checks for you")
1. **Memory safety**: no null, no dangling pointer, no reading past an array. [L239, L1466]
2. **Variable initialization** *(added, owner 2026-11-14)*: every variable gets a value where it's declared; `let total: i64;` is E0201. [L979, L1466]
3. **Garbage collection**: you never free anything. [L1421, L1464]
("What stops a program" moved to 6.3.)

---

## 6. Error handling

### 6.1 Result (approved)
1. **Ok and Err**. [L747]
2. **Matching on Result**. [L747]
3. **Reading files**: `read_file` gives a `Result`, and `write_file` makes the file first (added while drafting, for the owner). [L1071–1072]
4. **map_err**. [L777–783]
5. **ok, unwrap_or, is_ok and is_err**: `ok`, `unwrap_or`, `is_ok`, `is_err` (owner, 2026-11-14). [L777–780]

### 6.2 The ? operator (approved)
1. **? on Result**: and nothing after a failed `?` runs. [L752–753, L758]
2. **? on Option**. [L754]
3. **Error types**: the error types must match; `ok_or` turns an `Option` into a `Result` (added while drafting, for the owner). [L753, L757, L773, L785]
4. **Errors in main**: `?` in `main` is E0424. [L757]

### 6.3 Panics (approved)
1. **panic**: what it prints, exit 101, and it can't be caught. [L1051]
2. **unwrap and expect**: `unwrap`, `expect`. [L782–783]
3. **Stack overflow** *(moved from 5.3)*: `stack overflow`; walk long lists with a loop. [L1439]

### 6.4 defer (approved)
1. **defer**: and it reads variables as they are when it runs (owner, 2026-11-14). [L1039]
2. **defer and early returns**: including `?`. [L1039–1047]
3. **Defer order**: last first, and a defer in a loop runs at the end of each pass (owner, 2026-11-14). [L1039]
4. **When defers don't run**: a panic, `exit`; "the end of the program" moved to 10.1 (owner, 2026-11-14). [L1039, L1051]
5. **Deferred values** *(added, owner 2026-11-14)*: a deferred statement must be `()`, so a `Result` is E0456; `defer { …; }` discards it on purpose. [L1039]

---

## 7. Closures, iterators and collections (was "Functions as values and collections")

### 7.1 Functions as values (approved)
1. **Function types**: types like `fun(i64): i64`; a function value prints as `<fun>` and has no `==` (E0404) (owner, 2026-11-14). [L843–856]
2. **Arrays of functions**. [L843–856]
3. **Variants as functions**: `Shape.Circle` is a `fun(f64): Shape`; so are `Some`, `Ok`, `Err`, and an associated function is a value too (owner, 2026-11-14). [L852–853]

### 7.2 Closures (approved)
1. **Closures**: `fun(x) = x * 2` and `fun(x: i64): i64 { … }`. [L463, L858]
2. **Capture by copy**: a copy, taken when the closure is made. [L864]
3. **Counters with Ref**: a captured variable can't change (E0511). [L864–868]
4. **Ref.update**: `update` with a closure (5.2 taught it with a named function). [L578]
5. **map and and_then** *(added, owner 2026-11-14)*: on `Option` and `Result`, with a closure. [L774–781]
6. **Closures and recursion**: a closure can't call itself. [L1435]

### 7.3 Array helpers (approved)
1. **map**: a new array; the original never changes. [L789]
2. **filter**: and `filter` and `map` chain (owner, 2026-11-14). [L791, L798]
3. **fold**. [L789–798]
4. **any and all**. [L789–798]
5. **Sorting**: `sort` on numbers and strings, `sort_by`; `sort` on a struct is E0419 (owner, 2026-11-14). [L793–794]

### 7.4 Iterators (approved)
1. **Iterators**: `iter()`, `range(a, b)`, `chars()`. [L911–916]
2. **Chaining iterators**: adapters one after another, and `chain` (owner, 2026-11-14). [L918–936]
3. **enumerate**. [L924]
4. **zip**. [L932]
5. **collect, sum, count and find**: and `min`, `max`, `position`; `fold`/`any`/`all` work on iterators too (owner, 2026-11-14). [L925–938]
6. **Laziness**: `xs.map(f)` is made now, `xs.iter().map(f)` lazily; `take` and `skip` (owner, 2026-11-14). [L922–923, L940–944]
7. **Custom iterators**: a `next` method. [L1019]
8. **More adapters** *(added, owner 2026-11-14)*: `take_while`, `skip_while`, `flat_map`, `s.bytes()`. [L914, L934–936]

### 7.5 Maps and sets (approved)
1. **Map literals**: `#{"ann": 31}`, read and change entries, `m[k] += v`; `#{}` takes its type from where it's used (owner, 2026-11-14). [L895–898]
2. **Missing keys**: `get` gives an `Option`; `m[k]` panics. [L898]
3. **Iterating a map**: `for (k, v) of m`, in insertion order; `for … of mut` is E0442, loop over `keys()`; `values()` (owner, 2026-11-14). [L897, L898, L902]
4. **Sets**: `#{1, 2}`, `has`, `insert`, `remove`; `remove` and `clear` on maps too (owner, 2026-11-14). [L898–899]
5. **Set operations**: `union`, `intersect`, `minus`; `==` ignores order (owner, 2026-11-14). [L899, L903]
6. **collect_map and collect_set**: `collect_map`, `collect_set`. [L900]
7. **Key types**: keys can't contain floats. [L896]

---

## 8. Generics and interfaces

### 8.1 Generic functions (approved)
1. **Generic functions**: type arguments are inferred, never written; E0412 when nothing fixes them (owner, 2026-11-14). [L800, L811–812]
2. **Type bounds**: `==` needs `Eq`, `<` needs `Ord`; several bounds, `T: Ord + Eq` (owner, 2026-11-14). [L802, L805–806]
3. **Numeric bounds** *(added, owner 2026-11-14)*: `T: Num`, and `T: Float`. [L803–804]

### 8.2 Generic types (approved)
1. **Generic structs**: `Pair<T>`; a bare `Pair` in a type is E0418 (owner, 2026-11-14). [L800, L810–811]
2. **Generic enums**: `List<T>`. [L800, L569]
3. **Generic impl blocks**: `impl` blocks and bounds; `Self` is `Stack<T>`; a bounded method on the wrong type is E0419 (owner, 2026-11-14). [L812, L822, L826]

### 8.3 Interfaces (approved)
1. **Interface declaration**: and `Self` in it, and 7.4's `next` as the prelude's `Iter<T>` (owner, 2026-11-14). [L816, L819–820]
2. **Implementing an interface**: by having its methods. [L816–829]
3. **Interfaces as bounds**. [L816–829]
4. **Default methods**. [L816–829]

### 8.4 Interface values (approved)
1. **Interface values**: `Shape[]`. [L831–841]
2. **Method calls on interface values**. [L831–841]
3. **Type patterns**. [L639]
4. **Interface conversion**: a `Circle[]` isn't a `Shape[]`. [L833–834]

### 8.5 Equality, ordering and printing (approved)
1. **Deep equality**: and what has no `==`. [L704–715]
2. **Custom equality: eq and hash**: `eq` and `hash` together. [L713]
3. **Custom ordering: cmp**: `cmp`, which `sort` then uses. [L814]
4. **Custom printing: show**: `show`. [L1090–1107]

### 8.6 Operator overloading (approved)
1. **Arithmetic operators**: `add`, `sub`, …; without a method it's E0404; `+=` through `add` (owner, 2026-11-14). [L882–883, L886–887]
2. **Mixed operands** *(added, owner 2026-11-14)*: a second `mul` for `v * 2.0`, and `impl f64` for `2.0 * v`. [L884–885]
3. **Index operators**: `index`, `set_index`; `g[x, y]` is a tuple index (owner, 2026-11-14). [L889]

### 8.7 Derive blocks (approved; added by the owner, 2026-11-14)
1. **Derive blocks**: `derive Describe for i64 { … }`; items only through a bound, `5.describe()` is E0415. [L371, L825]
2. **Deriving for structs**: `derive … for struct`, `derive.fields`; a field no block covers is E0451. [L825, L1893]
3. **Deriving for enums**: `derive.variant`, `derive.index`. [L825]
4. **A type's own item**: it replaces the block's, as 8.5's `eq`, `hash` and `show` do. [L825, L713]
5. **Overlapping blocks** *(added, owner 2026-11-14)*: E0452 for two blocks on one type, or a block outside the interface's module. [L825, L1894]
6. **derive.all and derive.fold** *(added, owner 2026-11-14)*. [L825]
7. **derive.build** *(added, owner 2026-11-14)*. [L825]

---

## 9. Modules and tests (needs steps with several files)

### 9.1 Modules (approved)
1. **Multiple files**. [L1138–1143]
2. **import**: `module.item`. [L1138–1143]
3. **Import aliases**. [L1273–1287]
4. **Named imports**. [L1273–1287]

### 9.2 Visibility (approved)
1. **private**. [L1365–1377]
2. **Package visibility**: it means the whole package, not private. [L1365–1373]
3. **public**. [L1365–1377]
4. **Private fields**: behind a constructor. [L1365–1377]

### 9.3 Tests (approved)
1. **Test functions**: `@test` and `assert`. [L90, L1053–1084]
2. **assert_eq and assert_ne**: `assert_eq`, `assert_ne`. [L1053–1084]
3. **Running tests**: Test. [L90]

---

## 10. Concurrency

### 10.1 Green threads (approved)
1. **spawn**. [L586–589]
2. **join**. [L586–589]
3. **No data races**: one OS thread. [L1184–1187]
4. **When main returns** *(moved from 6.4, owner 2026-11-14)*: the program ends, and defers pending in other green threads don't run. [L12, L1039]

### 10.2 Channels (approved)
1. **Channels**: `Chan.new()`. [L594–600]
2. **Buffered channels**: `Chan.buffered(n)`. [L594–600]
3. **Closing a channel**: `recv` gives `None`. [L594–600]

### 10.3 select (approved)
1. **select**. [L605]
2. **Timeouts with after**. [L605]
3. **select with default**. [L605]
4. **Deadlock**: when every thread waits, a panic (exit 101). [L1189]

### 10.4 Actors (approved)
1. **Actor declaration**. [L607–624]
2. **Starting an actor**. [L607–624, L1190]
3. **Messages as method calls**. [L607–624]
4. **Stopping an actor** *(owner, 2026-11-14)*: `stop`, `join`; a panic ends only the actor. [L621, L1190]

---

## Left out of the course

Each for a reason, recorded so it isn't mistaken for a gap:

- **C interop** (`extern`, `[link]`): the sandbox refuses it. [section 8]
- **Packages and `lugha.toml` beyond `[package]`, git packages**: the sandbox refuses them. [L1145–1182]
- **The standard library modules** (`std.math`, `fs`, `json`, `http`, …): the standard library page (O9).
- **`include_bytes`/`include_str`**: for library authors. [L1079] (Derive blocks moved to 8.7, owner 2026-11-14.)
- **The rest of derive blocks**: `for tuple` blocks, `derive.variants`, `derive.build_variant`, and `for handle` with `derive.address` (handles need `extern type`, which the sandbox refuses). [L825]
- **Bit operators, wrapping and saturating arithmetic**: not taught. [L700–702, L949–961]

## Dependency check

Every lesson, and each earlier lesson one of its steps uses. Read down: nothing points forward.

| Lesson | Relies on |
|---|---|
| 1.1 Hello, world | — |
| 1.2 Values and types | 1.1 |
| 1.3 Variables | 1.2 |
| 1.4 Operators and conversions | 1.3 |
| 2.1 Blocks and scopes | 1.3 |
| 2.2 if | 2.1 (a branch's value) |
| 2.3 match | 2.2 (arms agree like branches) |
| 2.4 Loops | 2.2 (`if` inside the loops), 2.3 (`loop` as an expression, like `match`) |
| 2.5 Functions | 2.1 (the body's value), 1.3 (shadowing) |
| 2.6 Return and recursion | 2.2, 2.4 (`loop`), 2.5 |
| 3.1 Arrays | 2.4 |
| 3.2 Strings and characters | 2.4 (`for b of s`), 3.1 (`string[]`) |
| 3.3 Tuples and destructuring | 2.5 (two returns), 2.3 (patterns), 3.1 |
| 4.1 Structs | 1.3, 2.3, 2.5 |
| 4.2 Methods | 2.5, 4.1 |
| 4.3 Enums | 2.3, 4.1, 2.6 (a recursive function over a list) |
| 4.4 Option | 4.3, 3.1 (`pop`), 3.2 (strings to parse), 1.4 (`checked_add`) |
| 4.5 if let, while let and let else | 4.3, 4.4, 2.6 (`let … else` returns) |
| 5.1 Copies | 2.5, 3.1, 4.1, 4.3 |
| 5.2 Ref | 5.1, 4.2, 4.4 (`Option<Ref<Node>>`) |
| 5.3 Memory and safety | 1.4, 3.1, 4.4, 5.1 |
| 6.1 Result | 4.3, 4.4 |
| 6.2 The ? operator | 6.1, 2.6 |
| 6.3 Panics | 4.4, 6.1, 2.6 (recursion), 4.3 (a long list) |
| 6.4 defer | 2.1, 6.2 |
| 7.1 Functions as values | 2.5, 4.3 |
| 7.2 Closures | 7.1, 5.2 (`update`), 2.6 (recursion) |
| 7.3 Array helpers | 3.1, 7.2 |
| 7.4 Iterators | 2.4, 3.2 (strings, for `chars()`), 3.3 (`zip`), 4.2 (`next`), 4.4, 7.2 |
| 7.5 Maps and sets | 3.3, 4.4, 7.4 (`collect_map`) |
| 8.1 Generic functions | 2.5, 3.1 |
| 8.2 Generic types | 4.1, 4.2, 4.3, 8.1 |
| 8.3 Interfaces | 4.2, 8.1 |
| 8.4 Interface values | 8.3, 2.3 (type patterns in `match`) |
| 8.5 Equality, ordering and printing | 4.2, 7.3 (`sort`), 7.5 (`hash`), 8.3 |
| 8.6 Operator overloading | 4.2, 8.3 |
| 8.7 Derive blocks | 3.3, 6.1, 6.2, 8.1, 8.3, 8.5 |
| 9.1 Modules | 2.5, 4.1 |
| 9.2 Visibility | 9.1, 4.2 |
| 9.3 Tests | 2.5 |
| 10.1 Green threads | 2.5, 7.2 (spawning a closure) |
| 10.2 Channels | 10.1, 4.5 (`while let`) |
| 10.3 select | 10.2 |
| 10.4 Actors | 4.2, 10.1 |

Still appearing before it's taught, by design (readable without a lesson, not relied on):
- An array printed in Hello, world (1.1) and Values and types (1.2), before Arrays (3.1).
- `sort` in Array helpers (7.3) on numbers and strings only; ordering your own types waits for 8.5.

## Spec lines that contradict each other (tested)

| Spec says | Tested with the pinned lughac |
|---|---|
| "There is no `unwrap()`" [L785] | `unwrap` works |
| "Strings are not iterable in v0" [L1010] | `for b of "hi"` gives the bytes |
| `for path in paths` in the `defer` example [L1042] | `in` over an array is a parse error: use `of` |
| "Command-line arguments are not accessible in v0" [L1417] | `args()` works |
| `~` missing from the prefix rule [L446] | `~a` works |
| unary `-` listed for `i32 i64 f32 f64` [L699] | `-a` on an `i8` is E0404 (a gap to report to `../lugha`?) |
| integers need "a `_` or a binding" [L638] | a plain name at the top of a pattern is E0403; `mut t` works (2.3's notes) |
