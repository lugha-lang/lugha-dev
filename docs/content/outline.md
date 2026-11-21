# The course outline (v5, Lugha v18)

Built for Lugha v18 (`lughac` 0.18.x, tag m238) from the Lugha skill (`../lugha/skill/`, whose
examples `lughac` compiles and checks) and the v18 spec (`../lugha/docs/specs/Language v18
Specification.md`). `[name]` points at a skill page (`concepts/name.md` or `library/name.md`),
`[mNNN]` at the milestone in the spec's change list that brought the rule. v4, written for
v17, is in `outline-v4.md`; v3 in `outline-v3.md`.

For programmers new to Lugha: they know what a variable, a loop and a struct are.

**Theme.** The site's line is "For code you can trust." The course never says it, or anything
near it. It shows it: each place it lands is a program and what `lughac` or the program printed,
such as an error code, a refused path or a capability a function wasn't given. Learners infer the
rest (owner, 2026-11-20).

**Titles.** Each lesson is a numbered list of steps, one per objective, and each step has its
title here before it's drafted. A title is a heading a programmer would look for in a reference:
it names the feature (Function declaration, Shadowing, Match guards), not what the learner does
with it, and never describes the step. A step teaches what its title promises, and a lesson holds
only steps its own title covers. An objective never moves to another lesson without this file
changing first.

**Order.** Every step relies only on steps before it. Something may *appear* before it's taught
when a programmer can read it without a lesson (`console.println` from 1.1 on), but no step may
*rely* on understanding it. The dependency check at the end lists, for each lesson, every earlier
lesson one of its steps uses.

**Marks.** Every lesson is **to write**: no v17 program runs under v18 unchanged (printing alone
moved to `console`). A step marked *(v4 kept)* keeps its approved v4 objective and wording where
v18 left the rule alone, rewritten only for v18's syntax; *(changed)* keeps the title with a rule
v18 changed; *(new)* is new in v5; *(moved)* comes from another v4 lesson.

---

## 1. Basics

### 1.1 Hello, world (approved, 2026-11-20)
1. **The main function** *(changed)*: `fun main(console: Console)` and `console.println`. [capabilities; m180]
2. **Semicolons** *(v4 kept)*: every statement ends with `;`, since newlines mean nothing. [values-and-types]
3. **Comments** *(v4 kept)*: `//`, `/* … */` (they nest) and `/** … */`. [values-and-types]
4. **Exit codes** *(changed)*: `fun main(console: Console): i32`; returning the number is the only way to set one. [capabilities; m180]

### 1.2 Values and types (approved, 2026-11-20)
1. **Integer types** *(v4 kept)*: `i8 … i64`, `u8 … u64`, and their `MIN` and `MAX`. [values-and-types]
2. **Floating-point types** *(v4 kept)*: `f32` and `f64`; a float always prints with a `.`. [values-and-types]
3. **Integer literals** *(v4 kept)*: `1_000_000`, `0xFF`, `0b1010`, `0o600`; a leading zero is still decimal (W0107). [values-and-types]
4. **Float literals** *(v4 kept)*: `2e5` is an error (E0107); write `2.0e5`. [values-and-types]
5. **Characters and strings** *(changed)*: `'a'`, `"text\n"`, `\u{…}` in both; a string can't span lines. [values-and-types; m224]

### 1.3 Variables (approved, 2026-11-20)
1. **Variable declaration** *(v4 kept)*: `let`, with the type worked out or written after a colon. [values-and-types]
2. **Mutable variables** *(v4 kept)*: `let mut`, and E0501 without it. [values-and-types]
3. **Assignment** *(v4 kept)*: a statement with no value, so `a = b = 0` is E0204. [values-and-types]
4. **Number literal types** *(v4 kept)*: from what's around it, else `i64` or `f64`; one that doesn't fit is a compile error. [values-and-types]
5. **Shadowing** *(v4 kept)*: a second `let`, and `let x = x + 1;` reads the outer `x`. [values-and-types]
6. **Constants** *(v4 kept)*: `const NAME: T = value;`, and no mutable globals. [values-and-types]

### 1.4 Operators and conversions (approved, 2026-11-20)
1. **Integer division** *(v4 kept)*: same-type arithmetic, integer division, `%` takes the left side's sign. [values-and-types]
2. **Conversion with as** *(changed)*: `as` only where nothing is lost (`i32` to `f64`); `big as u8` is E0469. [values-and-types; m177]
3. **Narrowing conversions** *(changed; was "Lossy conversions")*: `truncate<u8>()`, `round<f64>()`, `saturate<u8>()`, `try_into<u8>()`, each saying what happens to a value that doesn't fit. [values-and-types; library/numbers-time-random; m177]
4. **Integer overflow** *(v4 kept)*: `integer overflow`, exit 101; it never wraps. [values-and-types]
5. **Sizes in bytes** *(new)*: `64.mb()`, `8.kb()`, in powers of 1024. [m174]
6. **Comparison and logical operators** *(v4 kept)*: `&&`, `||`, `!`, and `a < b < c` is E0203. [values-and-types]

---

## 2. Control flow and functions

Control flow comes first: its lessons need only `main`. Functions come after, so returning early,
returning from a loop and recursion can use `if` and loops.

### 2.1 Blocks and scopes (approved, 2026-11-20)
1. **Block expressions** *(v4 kept)*: its last expression without `;`. [functions]
2. **Statements and ()** *(v4 kept)*: a `;` throws the value away, and the block gives `()`. [functions]
3. **Variable scope** *(v4 kept)*: at the `}` of its block (E0301 after it). [functions]

### 2.2 if (approved, 2026-11-20)
1. **if expressions** *(v4 kept)*. [functions]
2. **Branch types** *(v4 kept)*: E0403. [functions]
3. **Boolean conditions** *(v4 kept)*: a number is never read as one (E0403). [functions]
4. **Braces and parentheses** *(v4 kept)*: parentheses optional, braces required (E0201). [functions]

### 2.3 match (approved, 2026-11-20)
1. **match expressions** *(v4 kept)*: arms, `_`, and arms of one type. [match-and-patterns]
2. **Or-patterns** *(v4 kept)*: `6 | 7 =>`. [match-and-patterns]
3. **Exhaustiveness** *(v4 kept)*: E0417; strings and integers need `_`, a `bool` doesn't. [match-and-patterns]
4. **Match guards** *(changed)*: `t if t < 0 =>`; ranges aren't patterns, so a guard does it. [match-and-patterns; m176]
5. **Unreachable arms** *(v4 kept)*: W0102. [match-and-patterns]

### 2.4 Loops (approved, 2026-11-20)
1. **while loops** *(v4 kept)*. [functions]
2. **for loops over ranges** *(v4 kept)*: `for i in a..b`, `b` excluded. [functions]
3. **break and continue** *(v4 kept)*. [functions]
4. **loop and break with a value** *(v4 kept)*: E0514 out of `while` or `for`. [functions]
5. **Loop labels** *(v4 kept)*: `break outer;`, `continue outer;`. [functions]

### 2.5 Functions (approved, 2026-11-20)
1. **Function declaration** *(v4 kept)*: typed parameters and a return type, always written; order in a file doesn't matter. [functions]
2. **Return values** *(v4 kept)*: a trailing `;` is E0503. [functions]
3. **Expression bodies** *(v4 kept)*. [functions]
4. **Immutable parameters** *(v4 kept)*: E0501, `let mut n = n;`. [functions]
5. **No overloading** *(v4 kept)*: no overloading or defaults (E0302). [functions]
6. **Passing the console** *(new)*: a function prints only through a `Console` it's given. A fix step: a function calling `console.println` without the parameter is E0301. [capabilities]

### 2.6 Return and recursion (approved, 2026-11-20)
1. **Early return** *(v4 kept)*. [functions]
2. **Return checking** *(v4 kept)*: an `if` without `else` never counts as returning (E0503). [functions]
3. **Returning from a loop** *(v4 kept)*: `while true` never counts; `loop` does. [functions]
4. **Recursion** *(v4 kept)*: and the branch that stops it. [functions]

---

## 3. Arrays, strings and tuples

### 3.1 Arrays (approved, 2026-11-20)
1. **Array literals** *(v4 kept)*: `[1, 2, 3]`, `[0; 10]`, and `.len`. [collections]
2. **Printing arrays** *(new)*: an array has no `Display`: `console.println(xs)` is E0422, `xs.debug()` gives `[1, 2, 3]`. [collections; m170]
3. **Indexing** *(v4 kept)*: `xs[i]`, and writing needs `let mut`. [collections]
4. **Bounds checking** *(v4 kept)*: the program stops with the length and the index. [collections]
5. **push and clear** *(v4 kept)*. [collections]
6. **Empty arrays** *(v4 kept)*: `let xs: i64[] = [];`. [collections]
7. **for … of loops** *(changed)*: `for x of xs`; `in` is for ranges only; the loop goes over the array as it was when it started, so the body may change `xs`. [collections; m224]
8. **Changing elements in a loop** *(v4 kept)*: `for x of mut xs`; changing `xs` itself there is E0507. [collections]
9. **Array concatenation and equality** *(v4 kept)*: `+` and `==`. [collections]
10. **debug** *(new)*: `debug(x)` writes `[file:line] x = …` to stderr and gives `x` back, so it goes inside an expression; no `Console` needed. [m170]

### 3.2 Strings and characters (approved, 2026-11-20)
1. **String interpolation** *(v4 kept)*: `{expr}`. [values-and-types]
2. **Format specifiers** *(v4 kept)*: `{x:.2}`, `{n:>6}`, `{n:05}`, `{n:#x}`. [library/text]
3. **Escaping braces** *(v4 kept)*: `{{`. [values-and-types]
4. **String concatenation** *(v4 kept)*: `+`, which won't take a string and a number. [values-and-types]
5. **String length** *(v4 kept)*: `.len` counts bytes, `char_count()` characters. [values-and-types]
6. **Bytes** *(v4 kept)*: `s[i]` is a `u8`, `for b of s`. [library/text]
7. **String methods** *(v4 kept)*: `split`, `lines`, `trim`, `contains`, `starts_with`, `join`. [library/text]
8. **Slicing** *(v4 kept)*: byte offsets, which can cut a character in half. [library/text]
9. **The char type** *(v4 kept)*: comparisons, `is_digit()`, `to_upper()`. [library/text]

### 3.3 Tuples and destructuring (approved, 2026-11-20)
1. **Tuples** *(changed)*: `(1, "a")`, `t.0`, and `t.debug()` to print one. [structs-and-enums]
2. **Multiple return values** *(v4 kept)*. [structs-and-enums]
3. **Destructuring with let** *(v4 kept)*: `let (q, r) = …`, and `let (mut x, mut y)`. [match-and-patterns]
4. **Destructuring in loops** *(v4 kept)*: `for (name, age) of people`. [match-and-patterns]
5. **Tuple patterns** *(v4 kept)*. [match-and-patterns]

---

## 4. Structs and enums

### 4.1 Structs (approved, 2026-11-20)
1. **Struct declaration** *(v4 kept)*. [structs-and-enums]
2. **Printing structs** *(changed)*: `p.debug()` gives `Point { x: 3, y: 4 }`; `console.println(p)` is E0422 until the type has `Display` (8.5). [structs-and-enums; m170]
3. **Struct literals** *(v4 kept)*: E0413. [structs-and-enums]
4. **Field assignment** *(v4 kept)*: needs `let mut` on the variable. [structs-and-enums]
5. **Struct update syntax** *(v4 kept)*: `Point { x: 1, ..p }`. [structs-and-enums]
6. **Struct equality** *(new)*: `with Eq` after the declaration gives `==`; without it, `a == b` is E0422. [structs-and-enums; m167]
7. **Struct literals in conditions** *(v4 kept; moved after equality, since its `==` needs `with Eq`)*: parentheses (E0205). [structs-and-enums]

### 4.2 Methods (approved, 2026-11-20)
1. **Methods** *(v4 kept)*: `self`. [structs-and-enums]
2. **mut self methods** *(v4 kept)*. [structs-and-enums]
3. **Associated functions and Self** *(v4 kept)*: `Vec2.new(1.0, 2.0)`, and `Self`. [structs-and-enums]
4. **Passing a value to its own mut method** *(v4 kept)*: `v.add(v)` is E0508; copy first. [structs-and-enums]

### 4.3 Enums (approved, 2026-11-20)
1. **Enum declaration** *(v4 kept)*: variants with data, built as `Shape.Circle(2.0)`. [structs-and-enums]
2. **Matching on enums** *(changed)*: a variant in a pattern has a leading dot, `.Circle(r) =>`. [match-and-patterns; m176]
3. **Recursive enums** *(v4 kept)*: a recursive enum needs no box. [structs-and-enums]

### 4.4 Option (approved, 2026-11-20)
1. **Option instead of null** *(v4 kept)*: no null; `Option`, `Some`, `None`. [errors]
2. **Matching on Option** *(changed)*: `.Some(n)` and `.None`; a `match` missing `.None` is E0417. [match-and-patterns; m176]
3. **Typing None** *(v4 kept)*: E0412. [errors]
4. **unwrap_or, is_some and is_none** *(v4 kept)*. [errors]
5. **Parsing numbers** *(v4 kept)*: `parse_i64`. [library/text]
6. **pop** *(v4 kept)*. [collections]
7. **Checked arithmetic** *(v4 kept)*: `checked_add`. [library/numbers-time-random]

### 4.5 if let, while let and let else (approved, 2026-11-20)
1. **if let** *(changed)*: `if let .Some(x) = o`. [match-and-patterns]
2. **while let** *(changed)*: `while let .Some(x) = xs.pop()`. [match-and-patterns]
3. **let else** *(v4 kept)*. [match-and-patterns]
4. **Nested patterns** *(v4 kept)*: `.Some(.Circle(r))`. [match-and-patterns]
5. **mut bindings** *(v4 kept)*. [match-and-patterns]
6. **Names in patterns** *(changed; was "Variants and bindings")*: a bare name is always a new binding, `other =>`, at the top of a pattern too; a variant always has its dot. [match-and-patterns; m176]

---

## 5. Value semantics

### 5.1 Copies (approved, 2026-11-20)
1. **Copies** *(v4 kept)*: assigning gives an independent copy. [structs-and-enums]
2. **Mutable copies** *(v4 kept)*. [structs-and-enums]
3. **Copying arrays** *(v4 kept)*. [collections]
4. **Passing by value** *(v4 kept)*: and return what they changed. [functions]
5. **Copies in a function call** *(changed; was a quiz, and lessons ask no questions, owner 2026-11-20)*: a read step showing what the quiz asked about. [functions]
6. **Copy-on-write** *(v4 kept)*. [collections]

### 5.2 mut parameters *(new lesson)* (approved, 2026-11-20)
1. **mut parameters**: `fun bump(mut c: Counter)` changes the caller's variable; checked in the sandbox at m238, `bump(mut c)` prints the change. [m166]
2. **mut at the call**: the call writes `mut` exactly where the parameter has it (E0443). [m166]
3. **Mutable places only**: an argument must be a `let mut` variable or a part of one (E0501). [m166]
4. **No aliasing**: the same variable twice in one call is E0508. [m166]

### 5.3 Ref (approved, 2026-11-21)
1. **Ref boxes** *(v4 kept)*: `Ref.new`, `get`. [library/collections]
2. **set without mut** *(v4 kept)*. [library/collections]
3. **get returns a copy** *(v4 kept)*. [library/collections]
4. **Updating a box** *(v4 kept)*: `update`; `count + 1` on a box is E0404. [library/collections]
5. **Identity with is** *(v4 kept)*: `==` is E0404. [library/collections]
6. **Linked structures** *(v4 kept)*: `Option<Ref<Node>>`. [library/collections]

### 5.4 Memory and safety (approved, 2026-11-21)
1. **Memory safety** *(v4 kept)*: no null, no dangling pointer, no reading past an array. [values-and-types]
2. **Variable initialization** *(v4 kept)*: `let total: i64;` is E0201. [values-and-types]
3. **Reference counting** *(changed; was "Garbage collection")*: each value is freed when its last holder goes; you never free anything. [m193]

---

## 6. Errors

### 6.1 Result (approved, 2026-11-21)
1. **Ok and Err** *(v4 kept)*. [errors]
2. **Matching on Result** *(changed)*: `.Ok(v)` and `.Err(e)`. [errors; m176]
3. **Results can't be ignored** *(new; replaces "Reading files", moved to 10.2)*: a `Result` used as a statement is E0467; `let _ = f();` drops one on purpose. [errors; m175]
4. **map_err** *(v4 kept)*. [errors]
5. **ok, unwrap_or, is_ok and is_err** *(v4 kept)*. [errors]

### 6.2 The ? operator (approved, 2026-11-21)
1. **? on Result** *(v4 kept)*: nothing after a failed `?` runs. [errors]
2. **? on Option** *(v4 kept)*. [errors]
3. **Error types** *(v4 kept)*: the error types must match; `ok_or`. [errors]
4. **Errors in main** *(v4 kept)*: `main` doesn't return a `Result`; handle it there and return an exit code. [errors]

### 6.3 Panics (approved, 2026-11-21)
1. **panic** *(v4 kept)*: what it prints, exit 101; it isn't a value to match on, and here it ends the program. [errors]
2. **unwrap and expect** *(changed)*: the panic names the line that called `unwrap`, not the prelude's. [errors; m173]
3. **Stack overflow** *(v4 kept)*. [errors]

### 6.4 defer (approved, 2026-11-21)
1. **defer** *(v4 kept)*: and it reads variables as they are when it runs. [errors]
2. **defer and early returns** *(v4 kept)*: including `?`. [errors]
3. **Defer order** *(v4 kept)*: last first; in a loop, at the end of each pass. [errors]
4. **defer and panics** *(changed; was "When defers don't run")*: a panic runs the pending `defer`s on its way out. [errors; m194]
5. **Deferred values** *(changed)*: a deferred statement must be `()`; `defer { let _ = f(); }`. [errors; m175]

---

## 7. Closures and collections

### 7.1 Functions as values (approved, 2026-11-21)
1. **Function types** *(v4 kept)*: `fun(i64): i64`; no `==` (E0404). [functions]
2. **Arrays of functions** *(v4 kept)*. [functions]
3. **Variants as functions** *(v4 kept)*: `Shape.Circle`, `Some`, `Ok`, and associated functions. [functions]

### 7.2 Closures (approved, 2026-11-21)
1. **Closures** *(v4 kept)*. [functions]
2. **Capture by copy** *(v4 kept)*: a copy, taken when the closure is made. [functions]
3. **Counters with Ref** *(v4 kept)*: a captured variable can't change (E0511). [functions]
4. **Ref.update** *(v4 kept)*. [library/collections]
5. **map and and_then** *(v4 kept)*: on `Option` and `Result`. [errors]
6. **Closures and recursion** *(v4 kept)*: a closure can't call itself. [functions]

### 7.3 Array helpers (approved, 2026-11-21)
1. **map** *(v4 kept)*. [collections]
2. **filter** *(v4 kept)*. [collections]
3. **fold** *(v4 kept)*. [collections]
4. **any and all** *(v4 kept)*. [collections]
5. **Sorting** *(changed)*: `sort` on numbers and strings, `sort_by`; floats aren't `Ord`: `sort_by(f64.total_order)`; sorting a struct needs `with Ord` (E0422). [collections; m168]

### 7.4 Maps and sets (approved, 2026-11-21)
1. **Map literals** *(changed)*: `Map { "ann": 31 }`, `Map {}`, read and change entries, `m[k] += v`; printing through `.debug()`. [collections; m178]
2. **Missing keys** *(v4 kept)*: `get` gives an `Option`; `m[k]` panics. [collections]
3. **Iterating a map** *(v4 kept)*: `for (k, v) of m`, in insertion order; `keys()`, `values()`. [collections]
4. **Sets** *(changed)*: `Set { 1, 2 }`, `has`, `insert`, `remove`. [collections; m178]
5. **Set operations** *(v4 kept)*: `union`, `intersect`, `minus`; `==` ignores order. [collections]
6. **Key types** *(changed)*: keys must be `Key`: numbers, strings, `bool`, `char`; your own type with `with Key` (E0422 without it); floats never (E0451). [collections; m167]
("collect_map and collect_set" moved to 9.2.)

---

## 8. Interfaces and generics

Interfaces come first: in v18 every bound is an interface.

### 8.1 Interfaces (approved, 2026-11-21)
1. **Interface declaration** *(v4 kept)*: and `Self` in it. [interfaces]
2. **Implementing an interface** *(changed)*: `impl Shape for Circle { … }`; methods with the right names don't make an implementation (E0422). [interfaces; m164]
3. **Where an impl lives** *(new)*: in the interface's module or the type's (E0459). [interfaces; m164]
4. **Default methods** *(v4 kept)*. [interfaces]
5. **Interfaces extending interfaces** *(new)*: `interface Pet: Named`; implementing `Pet` needs `Named`. [interfaces; m167]

### 8.2 Interface values (approved, 2026-11-21)
1. **Interface values** *(v4 kept)*: `Shape[]`. [interfaces]
2. **Method calls on interface values** *(v4 kept)*. [interfaces]
3. **Type patterns** *(v4 kept)*. [match-and-patterns]
4. **Interface conversion** *(changed)*: a `Circle[]` isn't a `Shape[]`; an interface value converts only to an interface its own extends. [interfaces; m223]
5. **Own methods and interface items** *(new)*: `c.area()` calls the type's own method, `Shape.area(c)` the interface's. [interfaces; m164]

### 8.3 Generic functions (approved, 2026-11-21)
1. **Generic functions** *(v4 kept)*: type arguments are inferred; E0412 when nothing fixes them. [generics]
2. **Type arguments at a use** *(new)*: `pick<string>([])`, `xs.map<string>(f)`. [generics; m177]
3. **Type bounds** *(changed)*: `T: Eq` for `==`, `T: Ord` for `<`, `T: Key` for map keys; several, `T: Ord + Key`; a type missing one is E0422 at the call. [generics; m167–168]
4. **Numeric bounds** *(v4 kept)*: `T: Num`, `T: Float`. [generics]
5. **Function bounds** *(new)*: `<F: fun(i64): i64>` takes the exact function. [m196]

### 8.4 Generic types (approved, 2026-11-21)
1. **Generic structs** *(v4 kept)*: `Pair<T>`; a bare `Pair` in a type is E0418. [generics]
2. **Generic enums** *(v4 kept)*: `List<T>`. [generics]
3. **Generic impl blocks** *(changed)*: `impl<T> Stack<T>`, and `impl<T: Num> Stack<T>` for a bound. [generics; m222]

### 8.5 Equality, ordering and printing (approved, 2026-11-21)
1. **Deep equality** *(changed)*: `==` compares deeply where `Eq` holds; what has no `==`. [interfaces; m167]
2. **with Eq, with Ord and with Key** *(new)*: derived from the fields; `Ord` brings `Eq`, `Key` brings `Eq`. [structs-and-enums; m165, m167–168]
3. **impl Eq and impl Key** *(changed; was "Custom equality")*: written by hand, hashing into a `Hasher`. [interfaces; m167]
4. **impl Ord** *(changed; was "Custom ordering")*: `cmp`, which `sort` then uses; W0108 when a derived `Eq` sits beside it. [interfaces; m168, m236]
5. **impl Display** *(changed; was "Custom printing")*: `show`, used by `println` and `"{x}"`. [interfaces; m170]
6. **impl Debug** *(new)*: a hand-written debug form. [m170]

### 8.6 Operator overloading (approved, 2026-11-21)
1. **Arithmetic operators** *(changed)*: `impl Add for Vec2`; without one it's E0404; `+=` through it. [interfaces; m171]
2. **Mixed operands** *(changed)*: `impl Mul<f64> for Vec2`, and `impl Mul<Vec2> for f64` for `2.0 * v`. [interfaces; m171]
3. **Index operators** *(v4 kept)*: `index`, `set_index`; `g[x, y]` is a tuple index. [interfaces]

### 8.7 Deriving (approved, 2026-11-21)
1. **with on your own interfaces** *(new)*: `struct Site { … } with Describe`, or `impl Describe for Site = derive;`. [structs-and-enums; m165]
2. **Derive blocks** *(changed)*: `derive Describe for i64 { … }`; items reached only through the interface. [m142, m165]
3. **Deriving for structs** *(v4 kept)*: `derive.fields`; a field no block covers is E0451. [m142]
4. **Deriving for enums** *(v4 kept)*: `derive.variant`, `derive.index`. [m142]
5. **Writing an item by hand** *(changed; was "A type's own item")*: deriving and writing one interface on one type is E0463. [m165]
6. **Overlapping blocks** *(v4 kept)*: E0452. [m142]
7. **derive.all and derive.fold** *(v4 kept)*. [m143–144]
8. **derive.build** *(v4 kept)*. [m142]

---

## 9. Iterators

### 9.1 Iterators (approved, 2026-11-21)
1. **Iterators** *(v4 kept)*: `iter()`, `chars()`, `bytes()`. [iterators]
2. **Chaining iterators** *(v4 kept)*: and `chain`. [iterators]
3. **enumerate** *(v4 kept)*. [iterators]
4. **zip** *(v4 kept)*. [iterators]
5. **Laziness** *(v4 kept)*: `xs.map(f)` now, `xs.iter().map(f)` lazily; `take`, `skip`. [iterators]
6. **More adapters** *(v4 kept)*: `take_while`, `skip_while`, `flat_map`. [iterators]

### 9.2 Using up an iterator (approved, 2026-11-21)
1. **collect, sum, count and find** *(v4 kept)*: and `min`, `max`, `position`. [iterators]
2. **collect_map and collect_set** *(moved from 7.5)*. [iterators]
3. **The loop's copy** *(new)*: `for x of it` works on a copy of the iterator. [iterators]

### 9.3 Your own iterators (approved, 2026-11-21)
1. **impl Iter** *(changed; was "Custom iterators")*: `impl Iter<i64> for Count { fun next(mut self): Option<i64> … }`; a type with only its own `next` can't be looped over (E0411). [iterators; m225]
2. **Iterators in generic code** *(new)*: `<I: Iter<i64>>`. [iterators]

---

## 10. Capabilities *(new chapter)*

Every program from 1.1 on has taken `console`. This chapter is about the rest of what `main` can
be given. `Net` can't run in the sandbox (no network) and is shown only as far as a refused
connection prints.

### 10.1 What main is given (approved, 2026-11-21)
1. **Capabilities in main**: `args: string[]`, `Console`, `Fs`, `Clock`, `Env`, `Entropy`, `Proc`, `Net`, by type, in any order. [capabilities]
2. **Each one once**: taking one twice, or something `main` can't be given, is E0304. [capabilities]
3. **Passing capabilities on**: as ordinary parameters; there are no globals. [capabilities]
4. **Arguments** *(moved from v4's playground use)*: `args: string[]`. [capabilities]

### 10.2 Files (approved, 2026-11-21)
1. **Fs and Dir**: `fs.cwd()`, `read_file`, `write_file`, `append_file`. [library/console-and-files]
2. **Folders**: `make_dirs`, `list`, `exists`, `remove_file`, `remove_dir`, each a `Result`. [library/console-and-files; m224]
3. **Confinement**: `..` and absolute paths are `Err("path leads outside the folder")`; `fs.dir(path)` opens another folder. [capabilities; m186]
4. **ReadDir**: `dir.read_only()` gives a folder with no writing method; `write_file` on it is E0415. [library/console-and-files; m237]
5. **A narrower Dir**: `dir.dir("data")`. [capabilities]

### 10.3 The console (approved, 2026-11-21)
1. **Reading input**: `console.read_line()`, a `Result<Option<string>, string>`; `None` at the end. [library/console-and-files; m228]
2. **stdout and stderr**: `eprintln`; `console.stdout_only()`. [capabilities; m187]

### 10.4 Clock, Env and Entropy (approved, 2026-11-21)
1. **Clock**: `now_ms()`, `monotonic_ms()` for measuring. [capabilities]
2. **Env**: `get(name)`, an `Option`; `env.only(["HOME"])`. [capabilities; m187]
3. **Entropy and random numbers**: `entropy.bytes(n)`, `random.from_entropy(entropy)`. [capabilities; library/numbers-time-random]

### 10.5 Other programs and the network (approved, 2026-11-21)
1. **Proc**: `proc.run(cmd, args)`, the program's exit code and output; never through a shell. [library/env-and-processes]
2. **Net**: `net.connect(addr)`; in the sandbox an `Err`, which is what prints. [library/net]

### 10.6 Faking a capability (approved, 2026-11-21)
1. **Capabilities are interfaces**: `impl Clock for FixedClock`. [capabilities]
2. **Using a fake**: a function taking `Clock` gets the fake. [capabilities]

---

## 11. Modules and tests (steps with several files)

### 11.1 Modules (approved, 2026-11-21)
1. **Multiple files** *(v4 kept)*. [modules-and-packages]
2. **import** *(v4 kept)*: `module.item`. [modules-and-packages]
3. **Import aliases** *(v4 kept)*. [modules-and-packages]
4. **Named imports** *(v4 kept)*. [modules-and-packages]

### 11.2 Visibility (approved, 2026-11-21)
1. **private** *(v4 kept)*. [modules-and-packages]
2. **Package visibility** *(v4 kept)*. [modules-and-packages]
3. **public** *(v4 kept)*. [modules-and-packages]
4. **Private fields** *(v4 kept)*: behind a constructor. [modules-and-packages]
5. **Re-exports** *(new)*: `public import a.b { X };`. [modules-and-packages]

### 11.3 Tests (approved, 2026-11-21)
1. **Test functions** *(v4 kept)*: `@test` and `assert`. [modules-and-packages]
2. **assert_eq and assert_ne** *(changed)*: the failure names the test's line. [m173]
3. **Running tests** *(v4 kept)*: Test. [tasks/testing]

### 11.4 Testing with capabilities (approved, 2026-11-21)
1. **A fresh folder**: `@test fun t(dir: Dir)` gets an empty folder of its own. [tasks/testing; m185]
2. **Fixed stand-ins**: a plain test's `Clock`, `Env` and `Entropy` are fixed, empty and seeded. [tasks/testing; m185]
3. **Fakes in tests**: 10.6's `FixedClock` in a test. [tasks/testing]
4. **Virtual time**: a test's `task.sleep(10_000)` costs nothing. (Moved after 12.1 if it needs `std.task` taught first.) [m203]

---

## 12. Concurrency *(rewritten)*

Tasks run on every core. Lessons print in an order they control (joins, channels), so each
step's output is the same every run.

### 12.1 Tasks and scopes (approved, 2026-11-21)
1. **scope and spawn**: `scope s { s.spawn(f(x)) }`. [tasks-and-scopes; m195]
2. **join**: `t.join()` gives `Ok(value)`. [tasks-and-scopes]
3. **A scope waits**: the body ends only when its tasks have; no task outlives it. [tasks-and-scopes]
4. **The root scope**: `main` takes `root: Scope`. [tasks-and-scopes]
5. **Tasks stay put**: a `Task` in an array or field is E0472. [tasks-and-scopes; m195]

### 12.2 Failure and cancellation (approved, 2026-11-21)
1. **All or nothing**: a task's panic or `Err` cancels the others, which run their `defer`s; the scope is `Err(Failure)`. [tasks-and-scopes; m195]
2. **Failure**: `f.task` and `f.kind`: `.Error(e)`, `.Panic(m)`. [tasks-and-scopes; m198]
3. **independent**: tasks fail alone. [tasks-and-scopes; m198]
4. **cancel**: `t.cancel("why")`. [tasks-and-scopes]
5. **limit**: `scope s limit 2`. [m198]

### 12.3 Deadlines (approved, 2026-11-21)
1. **within**: `scope s within 500 { … }`, and `.Deadline`. [tasks-and-scopes; m199]
2. **shield**: `shield within 100 { … }`. [m199]

### 12.4 Sendable (approved, 2026-11-21)
1. **What crosses to a task**: values cross as copies; a `Ref` is E0475. [tasks-and-scopes; m197]
2. **Sharing through a task**: what a `Ref` did for one task, a channel or an actor does for many. [channels-and-actors]

### 12.5 Channels (approved, 2026-11-21)
1. **Channels**: `Chan<T>.new(n)` gives `(Sender<T>, Receiver<T>)`; `0` hands each value over directly. [channels-and-actors; m200]
2. **Closing a channel**: `tx.close()`; `for v of rx` ends. [channels-and-actors]
3. **Each end its own job**: `rx.send(v)` is E0415. [channels-and-actors; m200]
4. **try_send and try_recv**: `.Sent`, `.Full(v)`, `.Closed(v)`; `.Ready(v)`, `.Empty`, `.Closed`. [channels-and-actors; m200]

### 12.6 select (approved, 2026-11-21)
1. **select** *(v4 kept)*. [channels-and-actors]
2. **Timeouts with after** *(v4 kept)*. [channels-and-actors]
3. **select with default** *(v4 kept)*. [channels-and-actors]
4. **Deadlock** *(changed)*: the report names each waiting task and its channel. [channels-and-actors; m200]

### 12.7 Actors (approved, 2026-11-21)
1. **Actor declaration** *(v4 kept)*. [channels-and-actors]
2. **Starting an actor** *(changed)*: `s.spawn(Counter { n: 0 })`. [channels-and-actors; m201]
3. **Messages as method calls** *(v4 kept)*: without a result, the caller goes on; with one, it waits. [channels-and-actors]
4. **Stopping an actor** *(changed)*: `stop`; the scope stops it at its end; there is no `join`. [channels-and-actors; m201]
5. **Actor fields**: a `Ref` field is E0475. [channels-and-actors]

---

## Left out of the course

Each for a reason, recorded so it isn't mistaken for a gap:

- **C interop**: `extern`, `[link]`, callbacks (`direct`, `spawned`, `realtime`), `extern blocking`, pinned handles, `Ring<T>`, `View<T>`/`MutView<T>`, the `ffi` permission: the sandbox refuses C. [concepts/c-interop; m207, m214–221]
- **Packages and `lugha.toml` beyond `[package]`, git packages**: the sandbox refuses them. [modules-and-packages]
- **The standard library modules** (`std.json`, `std.http`, `std.tls`, `std.crypto`, `std.toml`, `std.math`, `std.time`): the standard library page (O9). `std.random` appears in 10.4 and `std.task` in chapter 12 only as far as they need.
- **Network narrowing** (`net.only`, `allow_private`, `connect_only`, `listen_only`) **and TLS over any `Conn`**: they need a network. [m187, m184, m227]
- **`@test(integration)` and `--shuffle`**: the site's Test runs plain tests only.
- **Generic actors and actors as interface values**: past what a first course needs. [m202]
- **Runtime internals** (workers, the scheduler, helper threads, stacks, the allocator, hash seeding): nothing a program writes. [m204–213]
- **`include_bytes`/`include_str`**: for library authors.
- **The rest of derive blocks** (`for tuple`, `derive.variants`, `derive.build_variant`, `for handle`, `derive.address`).
- **Bit operators, wrapping and saturating arithmetic**: not taught.

## Dependency check

Every lesson, and each earlier lesson one of its steps uses. Read down: nothing points forward.

| Lesson | Relies on |
|---|---|
| 1.1 Hello, world | — |
| 1.2 Values and types | 1.1 |
| 1.3 Variables | 1.2 |
| 1.4 Operators and conversions | 1.3 |
| 2.1 Blocks and scopes | 1.3 |
| 2.2 if | 2.1 |
| 2.3 match | 2.2 |
| 2.4 Loops | 2.2, 2.3 |
| 2.5 Functions | 2.1, 1.3, 1.1 (the console) |
| 2.6 Return and recursion | 2.2, 2.4, 2.5 |
| 3.1 Arrays | 2.4 |
| 3.2 Strings and characters | 2.4, 3.1 |
| 3.3 Tuples and destructuring | 2.5, 2.3, 3.1 (`.debug()`) |
| 4.1 Structs | 1.3, 2.3, 2.5, 3.1 (`.debug()`) |
| 4.2 Methods | 2.5, 4.1 |
| 4.3 Enums | 2.3, 4.1, 2.6 |
| 4.4 Option | 4.3, 3.1, 3.2, 1.4 |
| 4.5 if let, while let and let else | 4.3, 4.4, 2.6 |
| 5.1 Copies | 2.5, 3.1, 4.1, 4.3 |
| 5.2 mut parameters | 5.1, 4.2 (`mut self`) |
| 5.3 Ref | 5.1, 4.2, 4.4 |
| 5.4 Memory and safety | 1.4, 3.1, 4.4, 5.1 |
| 6.1 Result | 4.3, 4.4 |
| 6.2 The ? operator | 6.1, 2.6 |
| 6.3 Panics | 4.4, 6.1, 2.6 |
| 6.4 defer | 2.1, 6.2, 6.3 (panics) |
| 7.1 Functions as values | 2.5, 4.3 |
| 7.2 Closures | 7.1, 5.3, 2.6 |
| 7.3 Array helpers | 3.1, 7.2, 4.1 (`with Eq` beside `with Ord`) |
| 7.4 Maps and sets | 3.3, 4.4, 4.1 (`with`) |
| 8.1 Interfaces | 4.2 |
| 8.2 Interface values | 8.1, 2.3 |
| 8.3 Generic functions | 2.5, 3.1, 8.1 |
| 8.4 Generic types | 4.1, 4.2, 4.3, 8.3 |
| 8.5 Equality, ordering and printing | 4.1, 7.3, 7.4, 8.1 |
| 8.6 Operator overloading | 4.2, 8.1 |
| 8.7 Deriving | 3.3, 6.1, 6.2, 8.3, 8.5 |
| 9.1 Iterators | 2.4, 3.2, 3.3, 7.2 |
| 9.2 Using up an iterator | 9.1, 4.4, 7.4 |
| 9.3 Your own iterators | 9.1, 8.1, 8.3, 5.2 (`mut self`) |
| 10.1 What main is given | 1.1, 2.5 |
| 10.2 Files | 10.1, 6.1, 6.2, 3.2 |
| 10.3 The console | 10.1, 4.5 (`while let`), 6.1 |
| 10.4 Clock, Env and Entropy | 10.1, 4.4 |
| 10.5 Other programs and the network | 10.1, 6.1 |
| 10.6 Faking a capability | 10.4, 8.1 |
| 11.1 Modules | 2.5, 4.1 |
| 11.2 Visibility | 11.1, 4.2 |
| 11.3 Tests | 2.5, 4.4 |
| 11.4 Testing with capabilities | 11.3, 10.2, 10.6 |
| 12.1 Tasks and scopes | 2.5, 6.1 (`join`'s `Result`) |
| 12.2 Failure and cancellation | 12.1, 6.3, 6.4 |
| 12.3 Deadlines | 12.2 |
| 12.4 Sendable | 12.1, 5.3 |
| 12.5 Channels | 12.1, 4.5, 4.3 (`.Sent`, `.Full`) |
| 12.6 select | 12.5 |
| 12.7 Actors | 4.2, 12.1, 12.4 |

Still appearing before it's taught, by design (readable without a lesson, not relied on):
- `console.println` in 1.1 before capabilities (chapter 10): 1.1's error teaches only that `main` takes it.
- `with Eq` in 4.1 before interfaces (8.5): read as "this type can be compared".

## Open, to settle while drafting

- **The skill and `mut` parameters disagree** (for `../lugha`): `concepts/functions.md` says a `mut` parameter "still changes only the copy"; at m238, `fun bump(mut c: Counter)` called as `bump(mut c)` changes the caller's variable (checked 2026-11-20). 5.2 follows the compiler.
- **Printing order in chapter 12**: tasks run on every core at m238, so the switch PRP decides whether the sandbox sets `LUGHA_WORKERS`; until then each step orders its output itself.
- **10.5's started programs** and **11.4's virtual time** need a sandbox check before their steps are final.
