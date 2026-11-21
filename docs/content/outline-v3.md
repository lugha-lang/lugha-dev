# The course outline (v3)

Built from a full read of `lughac spec` (Lugha v17, sections 1–7 and the example programs in 10).
`[Lnnn]` points at the spec's lines (the copy printed by the pinned `lughac spec`), so every
objective can be checked. v1, with the owner's comments, is in `outline-v1.md`.

For programmers new to Lugha: they know what a variable, a loop and a struct are. Titles use the
words a programmer looks for. Each lesson lists what the learner can do after it, and a lesson
teaches only that; the reader check's questions come from these objectives, written before the
draft.

**Order.** Every lesson relies only on lessons before it. Something may *appear* before it's taught
when a programmer can read it without a lesson (an array printed in Hello, world), but no step may
*rely* on understanding it. The dependency check is at the end of this file.

**Surprises** are the rules a programmer from another language would get wrong: material for a
"predict, then run" step or a mistake that `lughac` stops.

Status: **written** (on the site, to restructure against this outline) or **to write**.

---

## 1. Basics

What every program is made of: values, their types, names, and the operators between them.

### 1.1 Hello, world (written)
- Write `fun main()`, run it, and print with `println`.
- Return an exit code with `fun main(): i32`.
- Write comments: `//`, `/* … */` (they nest), and `/** … */` doc comments. [L279–285]
- Know every statement ends with `;`, since newlines mean nothing. [L279]
- Surprises: block comments nest; `main` can only be `fun main()` or `fun main(): i32`. [L281, L1417]

### 1.2 Values and types (to write)
- Name the built-in types: `i8 … i64`, `u8 … u64`, `f32`, `f64`, `bool`, `char`, `string`. [L526–540]
- Write literals: `1_000_000`, `0xFF`, `0b1010`, `0o600`, `3.14`, `2.0e-3`, `'a'`, `"text\n"`, `true`. [L300–325, L717]
- Know how floats print: always with a `.` (`2.0`), and with an exponent from `1e16`. [L1124]
- Surprises:
  - `2e5` is an error: a float needs a `.` (`2.0e5`). [L314]
  - A leading zero is still decimal: `0600` is six hundred (warning W0107). [L313]
  - Strings can't span lines; write `\n`. [L321]

### 1.3 Variables (written as "Names", to restructure)
- Declare with `let`, and use the name where the value would go. [L420]
- Know variables can't change unless declared `let mut` (E0501). [L251, L872]
- Let the type be worked out, or write it after a colon. [L672–676]
- Know how a number literal gets its type: from what's around it (an annotation, the other operand, a parameter), else `i64` or `f64`. [L676–677]
- Shadow a variable with a second `let`, and know a variable's scope starts after its declaration, so `let x = x + 1;` reads the outer `x`. [L979]
- Declare a constant with `const NAME: T = value;`, and know there are no mutable globals. [L1130]
- Surprises:
  - `let e: f64 = 5;` is an error: a whole number never becomes a float. [L678, L686]
  - A number that doesn't fit its type is a compile error (`let d: u8 = 300;`). [L678]

### 1.4 Operators and conversions (to write)
- Use `+ - * / %` on two numbers of the same type, and get that type. [L693]
- Know integer division gives an integer, and `%` takes the sign of the left side. [L893]
- Convert with `as`, and know what it does: narrowing truncates, float to integer truncates toward zero and saturates. [L724]
- Write a float where a float is expected: `let e: f64 = 5;` is refused, `5.0` or `5 as f64` is fine. [L678, L686]
- Use comparisons and `&& || !` (short-circuit), and know the precedence that matters. [L470–488, L695–698]
- Surprises:
  - Integer overflow stops the program (`integer overflow`, exit 101); it never wraps. [L893]
  - Division by zero panics for integers, but gives `inf` or `NaN` for floats. [L893, L967]
  - `a < b < c` is an error (E0203). [L470]
  - `-x` works on `i32`, `i64`, `f32`, `f64` only: `-x` on an `i8` is E0404 (tested). [L699]

---

## 2. Functions and control flow

### 2.1 Blocks and scopes (to write)
- Know a block `{ … }` has a value: its last expression without `;`. [L987]
- Know a `;` turns an expression into a statement and throws its value away. [L1049]
- Know a variable lives until the `}` of its block. [L987]
- Know `()` is the value of a block with nothing at the end. [L545, L561]
- Surprise: assignment is a statement, not an expression, so `a = b = c` and `if (x = 1)` are errors (E0204). [L490]

### 2.2 Functions (written)
- Declare a function with typed parameters and a return type, and return the body's last expression. [L1379]
- Know inference is local: parameters and return types are always written, never worked out from the body. [L672–676, L1383]
- Know a trailing `;` throws the value away (E0503). [L1049]
- Write `=` bodies. [L1383]
- Know parameters can't be reassigned, and shadow one with `let mut n = n;`. [L1400]
- Know the order of functions in a file doesn't matter. [L1132]
- Surprise: no default parameters and no overloading: a name means one function (E0302). [L1403]

### 2.3 if (part of "Control flow", written)
- Use `if` / `else if` / `else` as an expression whose branches have one type. [L981]
- Know a condition must be a `bool`: a number is never read as one. [L981]
- Return early with `return`, and write a recursive function. [L412, L1402] (moved from 2.2, which has no `if` to show them)
- Surprise: parentheses around a condition are optional and braces are required. [L361]

### 2.4 match (drafted)
- Choose between values with `match` on integers, strings and `bool`, with `_` for the rest. [L636]
- Use `match` as an expression whose arms have one type. [L636]
- Add guards (`_ if n < 0 =>`) and or-patterns (`1 | 2 =>`), and know a guarded arm doesn't count toward covering every case. [L636, L638, L642] (`n if n < 0 =>` is refused at the top level in m159: E0403, see 2.4's notes)
- Surprises: a `match` must cover every case, so integers and strings always need `_` (E0417); an unreachable arm is warning W0102. [L638, L640]

### 2.5 Loops (part of "Control flow", written)
- `while`, and `for i in a..b` over a range (b excluded). [L989, L996]
- `loop`, `break`, `continue`, and `break value` out of a `loop`. [L1033, L1037]
- Label a loop and `break outer;` or `continue outer;` out of an inner one. [L1035]
- Surprises:
  - Only `loop` gives a value: `break value` out of `while` or `for` is E0514. [L1033]
  - `while true { return 1; }` doesn't count as returning from a function (E0503, tested); use `loop`. [L1407–1415]

---

## 3. Arrays, strings and tuples

### 3.1 Arrays (to write)
- Build arrays with `[1, 2, 3]` and `[0; 10]`, read and write by index, and read `.len`. [L645–648]
- Grow with `push` and empty with `clear`, which need `let mut`. [L739–745]
- Loop with `for x of xs`, and change elements with `for x of mut xs`. [L1010, L1012]
- Join with `+` and compare with `==`. [L650, L704]
- Surprises:
  - `in` is only for ranges; an array needs `of` (`for x in [1, 2]` is a parse error, tested). [L427]
  - An index out of range stops the program with the length and the index. [L645]
  - An empty `[]` needs a type: `let xs: i64[] = [];`. [L647]
  - The loop variable can't be changed, and the body can't change the array being looped over. [L1010]

### 3.2 Strings and characters (written as "Text", to restructure)
- Interpolate with `{expr}`, and format with specifiers: `{x:.2}`, `{n:>6}`, `{n:05}`, `{n:#x}`. [L323, L1109–1118]
- Join with `+`, and know `+` won't take a string and a number. [L670, L694]
- Know a string is immutable UTF-8: `.len` counts bytes, `s[i]` is a byte (`u8`), `for b of s` loops over bytes, and `char_count()` counts characters. [L670, L720, L1017]
- Use the helpers: `split` and `lines` (they give a `string[]`), `trim`, `contains`, `starts_with`, `slice`, and `join` on a `string[]`. [L760–771]
- Use `char`: `'a'`, comparisons, `is_digit()`, `to_upper()`. [L717–721]
- Surprises:
  - Every `{` in a string interpolates: write `{{` for a brace. [L323]
  - `char` methods know ASCII and Latin-1 only (`ß` keeps its case). [L721]
  - `slice` works on byte offsets and can cut a character in half. [L768]

### 3.3 Tuples and destructuring (to write)
- Build tuples `(1, "a")`, read `t.0`, and return several values from a function. [L906]
- Destructure: `let (q, r) = divmod(7, 2);`, `for (name, age) of people` over an array of tuples, tuple patterns in `match`. [L907–908]
- Surprise: `let mut (x, y)` isn't valid: write `let (mut x, mut y)`. [L908]

---

## 4. Structs and enums

### 4.1 Structs (written)
- Declare a struct, build one with every field (E0413), read and print it. [L563, L1090]
- Change a field, which needs `let mut` on the variable. [L872]
- Build one from another with struct update, `Point { x: 1, ..p }`. [L563]
- Surprise: a struct literal in an `if` or `match` condition needs parentheses (E0205). [L492]

### 4.2 Methods (to write)
- Attach methods with `impl`, with `self` or `mut self`. [L728–731]
- Write associated functions and call them on the type, `Vec2.new(1.0, 2.0)`, and use `Self`. [L732, L822]
- Surprise: `v.add(v)` with a `mut self` method is E0508; copy first. [L733]

### 4.3 Enums (to write)
- Declare an enum whose variants carry data, and build them with a dot: `Shape.Circle(2.0)`. [L565]
- Use `match` to take an enum apart, binding its data, and know it must cover every variant. [L636–641]
- Declare a recursive enum such as a list or a tree. [L567]
- Surprises:
  - It's `Shape.Circle`, never `Shape::Circle` (E0207). [L357]
  - A recursive enum needs no box. [L567]

### 4.4 Option (to write)
- Know Lugha has no null: every value is a real value, and a value that might be missing is an `Option`. [L239, L559]
- Represent a missing value with `Option`, `Some` and `None`, and take it apart with `match`. [L569]
- Use `unwrap_or`, `is_some`, `is_none`; parse text with `parse_i64`; get the last element with `pop`; add without overflowing with `checked_add`. [L772–785, L739–745, L949–961, L1053–1084]
- Surprise: `None` on its own needs a type (E0412). [L569]

### 4.5 More patterns (to write)
- `if let`, `while let`, and `let … else`, on `Option` and your own enums. [L991–994]
- Nested patterns, and `mut` bindings in an arm. [L636–643]
- Surprise: a bare name at the top of a pattern is a variant, not a binding, and a misspelled variant becomes a binding (warning W0103). [L641, L436]

---

## 5. Value semantics

### 5.1 Copies (written: the model for the course's voice)
- Know assigning a struct, an array or an enum gives an independent copy, and a copy needs its own `mut`. [L547]
- Know a function gets copies of its arguments and returns what it changed. [L1401]
- Know copies are cheap: they share memory until one side writes (copy-on-write). [L652, L1450]

### 5.2 Shared references with Ref (written)
- Share one value with `Ref.new`, `get`, `set`, `is`, the only value that copies share. [L571–582]
- Build a structure that points at itself through `Option<Ref<Node>>`. [L584]
- Surprises: `set` needs no `let mut`; `get` gives a copy; `==` on boxes is E0404 (use `is`). [L582, L583]

### 5.3 What Lugha checks for you (to write)
- Know there's no null, no dangling pointer, and no reading past an array. [L239, L1466]
- Know the garbage collector frees memory, and you never do. [L1421]
- Know what stops a program (overflow, bounds, division by zero, `stack overflow`) and that it exits with 101. [L1051, L1188, L1439]
- Surprise: deep recursion overflows the stack, so walk long lists with a loop. [L1439]

---

## 6. Error handling

### 6.1 Result (to write)
- Return `Ok` or `Err` from something that can fail, and handle both. [L747]
- Use `map_err`, `ok`, `unwrap_or`; read a file with `read_file`, which gives a `Result`. [L777–783, L1071–1075]

### 6.2 The ? operator (to write)
- Pass an `Err` or a `None` up with `?`. [L752–758]
- Surprises: the error types must match; `?` in `main` is E0424. [L753, L758]

### 6.3 Panics (to write)
- Know what `unwrap`, `expect` and `panic` do, what a panic prints, and that it exits with 101 and can't be caught. [L1051, L782–783]

### 6.4 defer (to write)
- Run cleanup when a block is left with `defer`, including on an early `?`, last first. [L1039–1047]
- Surprise: a panic, `exit` and the end of the program skip pending defers. [L1039]

---

## 7. Functions as values and collections

### 7.1 Functions as values (to write)
- Pass and store functions: function types `fun(i64): i64`, named functions as values, arrays of functions. [L843–856]
- Know a variant with data is a function: `Shape.Circle` is a `fun(f64): Shape`. [L853]

### 7.2 Closures (to write)
- Write `fun(x) = x * 2` and `fun(x: i64): i64 { … }`. [L463, L858]
- Use `Ref`'s `update` with a closure. [L575]
- Surprises: a closure captures copies when it's made, and can never change a captured variable (E0511); use a `Ref` for a counter. A closure can't call itself. [L864–868, L1435]

### 7.3 Array helpers (to write)
- Use `map`, `filter`, `fold`, `any`, `all`, `sort_by`, and `sort` on numbers and strings. [L789–798]
- Surprise: the helpers return new arrays and never change the original. [L789]

### 7.4 Iterators (to write)
- Get an iterator with `iter()`, `range(a, b)`, `chars()`; chain `map`, `filter`, `take`, `enumerate`, `zip`; finish with `collect`, `sum`, `count`, `find`. [L911–947]
- Loop over any type with a `next` method. [L1019]
- Surprise: `xs.map(f)` is an array, made now; `xs.iter().map(f)` is an iterator, run lazily. [L942–944]

### 7.5 Maps and sets (to write)
- Build `#{"ann": 31}` and `#{1, 2}`, read and change entries, loop with `for (k, v) of m`. [L895–902]
- Use `get` (gives an `Option`), `has`, `insert`, `remove`; `union`, `intersect`, `minus` on sets; `collect_map`, `collect_set`. [L899–901]
- Surprises: `m[k]` on a missing key panics; keys can't contain floats; order is insertion order. [L897–899]

---

## 8. Generics and interfaces

### 8.1 Generic functions (to write)
- Write `fun max<T: Ord>(a: T, b: T): T`, and know type arguments are inferred at a call, never written. [L496, L800–811]
- Surprise: a bare `T` can only be stored, copied, passed and printed: `==` needs `Eq`, `<` needs `Ord`. [L805–806]

### 8.2 Generic types (to write)
- Declare `struct Stack<T>` and `enum List<T>`, with `impl` blocks and bounds on them. [L800, L826]

### 8.3 Interfaces (to write)
- Declare an interface, satisfy it just by having the methods, and use it as a bound. Default methods. [L816–829]

### 8.4 Interface values (to write)
- Store different types behind one interface (`Shape[]`), call methods on them, and match on the type inside. [L831–841, L639]
- Surprise: a value converts to an interface only where exactly that interface is expected; a `Circle[]` isn't a `Shape[]`. [L833–834]

### 8.5 Equality, ordering and printing (to write)
- Know `==` compares deeply, and what has no `==` (functions, `Ref`s, interface values). [L704–715]
- Give your type its own equality (`eq` and `hash` together), order (`cmp`, which `sort` then uses) and printed form (`show`). [L713, L814, L1090–1107]

### 8.6 Operator overloading (to write)
- Make `+ - * / %` and `[ ]` work on your type with `add`, `sub`, …, `index`, `set_index`. [L882–890]

---

## 9. Modules and tests (needs steps with several files)

### 9.1 Modules (to write)
- Split a program into files, `import` a module, and use `module.item`; aliases and named imports. [L1138–1143, L1273–1287]

### 9.2 Visibility (to write)
- Use `private`, `public`, and the default, and keep a struct's fields private behind a constructor. [L1365–1377]
- Surprise: no keyword doesn't mean private; it means the whole package. [L1365–1373]

### 9.3 Tests (to write)
- Write `@test` functions with `assert`, `assert_eq`, `assert_ne`, and run them with Test. [L90, L1053–1084]

---

## 10. Concurrency

### 10.1 Green threads (to write)
- Run a call concurrently with `spawn`, and get its result with `join`. [L586–589, L1184]
- Know green threads share one OS thread, so there are no data races. [L1184–1187]

### 10.2 Channels (to write)
- Send between threads with `Chan.new()` and `Chan.buffered(n)`; `recv` gives `None` once closed. [L594–600]

### 10.3 select (to write)
- Wait on several channels with `select`, with `after(ms)` or `default`. [L605]
- Surprise: when every thread waits, the program stops with a deadlock panic (exit 101). [L1189]

### 10.4 Actors (to write)
- Declare an actor, start it with `spawn`, and send it messages by calling its methods. [L607–624, L1190]

---

## Left out of the course

Each for a reason, recorded so it isn't mistaken for a gap:

- **C interop** (`extern`, `[link]`): the sandbox refuses it. [section 8]
- **Packages and `lugha.toml` beyond `[package]`, git packages**: the sandbox refuses them. [L1145–1182]
- **The standard library modules** (`std.math`, `fs`, `json`, `http`, …): the standard library page (O9).
- **Derive blocks, `include_bytes`/`include_str`**: for library authors. [L825, L1079]
- **Bit operators, wrapping and saturating arithmetic**: shown once in 1.4 at most, not taught. [L700–702, L949–961]

## Dependency check

Every lesson, and what it relies on from earlier lessons. Read down: nothing points forward.

| Lesson | Relies on |
|---|---|
| 1.1 Hello, world | — |
| 1.2 Values and types | 1.1 |
| 1.3 Variables | 1.2 |
| 1.4 Operators and conversions | 1.3 |
| 2.1 Blocks and scopes | 1.3 |
| 2.2 Functions | 2.1 |
| 2.3 if | 2.1, 2.2 |
| 2.4 match | 2.3 |
| 2.5 Loops | 2.3 |
| 3.1 Arrays | 2.5 |
| 3.2 Strings and characters | 2.5 (`for b of s`), 3.1 (`string[]`) |
| 3.3 Tuples and destructuring | 2.2 (several returns), 2.4 (patterns), 3.1 |
| 4.1 Structs | 1.3, 2.4 |
| 4.2 Methods | 2.2, 4.1 |
| 4.3 Enums | 2.4, 4.1 |
| 4.4 Option | 4.3, 3.1 (`pop`), 3.2 (`parse_i64`), 1.4 (`checked_add`) |
| 4.5 More patterns | 4.3, 4.4 |
| 5.1 Copies | 2.2, 3.1, 4.1, 4.3 |
| 5.2 Ref | 5.1, 4.2, 4.4 (`Option<Ref<Node>>`) |
| 5.3 What Lugha checks | 1.4, 3.1, 5.1 |
| 6.1 Result | 4.3, 4.4 |
| 6.2 The ? operator | 6.1 |
| 6.3 Panics | 4.4, 6.1 |
| 6.4 defer | 2.1, 6.2 |
| 7.1 Functions as values | 2.2, 4.3 |
| 7.2 Closures | 7.1, 5.2 (`update`) |
| 7.3 Array helpers | 3.1, 7.2 |
| 7.4 Iterators | 2.5, 3.2 (`chars()`), 3.3 (`zip`), 4.4, 7.2 |
| 7.5 Maps and sets | 3.3, 4.4, 7.4 (`collect_map`) |
| 8.1 Generic functions | 2.2, 3.1 |
| 8.2 Generic types | 4.1, 4.2, 4.3, 8.1 |
| 8.3 Interfaces | 4.2, 8.1 |
| 8.4 Interface values | 8.3, 4.5 (type patterns) |
| 8.5 Equality, ordering and printing | 4.2, 7.3 (`sort`), 7.5 (`hash`), 8.3 |
| 8.6 Operator overloading | 4.2, 8.3 |
| 9.1 Modules | 2.2, 4.1 |
| 9.2 Visibility | 9.1, 4.2 |
| 9.3 Tests | 2.2 |
| 10.1 Green threads | 2.2, 7.2 (spawning a closure) |
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
