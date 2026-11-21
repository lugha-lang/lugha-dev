# The course, rewritten for a beginner reading the screen (2026-11-21)

Every step's text, as the learner will read it, in course order. Code, outputs, step titles, Kind lines, objectives and Notes are unchanged; only the text and the error notes are new.
An **Error note** is shown in the box beside the step's first error, in place of lughac's own first paragraph; "More about" still opens lughac's full explanation.

Decisions for you are listed first. Lesson 1.1 and 2.1 step 2 are the versions we worked out together.

## Decisions for you

1. **4.5 step 6** dropped your sentence "Spelled right, `Empty` would be E0468, which asks for its dot, but `Emtpy` is no variant's name, so it's read as a binding." to stay within the word limit; the step now says a bare name is always a new binding. Keep it dropped, or put it back (something else would have to give).
2. **5.2 step 4** now explains E0508 with "Without `mut`, a parameter acts as a copy because the function can't change it, but a struct isn't actually copied: the function reads it where it is." That's true (spec L1348) and is why the call is refused, but it adds a layer under 5.1's "a parameter is a copy".
3. **6.1 step 3** keeps one pointer: the help line on screen offers `?`, so the text says "`?`, which comes in the next lesson".
4. **7.2 step 4** keeps "which `update` took by name in the Ref lesson", to say where `add_one` comes from.
5. **8.7 step 1** tells the learner that lines 5 to 17 are explained in the next steps; the code itself uses `derive` before it's taught (the Notes already suggest swapping steps 1 and 2).
6. Dropped asides that only said where things are taught or didn't explain the screen, among them: 1.1 step 4's `exit`/E0304 sentences, 12.6 step 3's E0438 sentence, 12.7 step 1's E0439 sentence, 11.3 step 1's E0434 mention. No objective names any of them.

# 1. Basics

## 1.1 Hello, world

### Step 1: The main function (read)

A Lugha program starts at `main`, the function that `fun` declares on line 2.
Line 1 is a doc comment, `/** … */`, a note about the function after it.
When the program starts, `main` is given the console as a parameter, named `console`, of type `Console`.
Line 3 prints through it, with `console.println`.
Press Run.

The output panel shows `Hello, world`, then "Exited with code 0".
That's the program's exit code: this `main` gives nothing back, so the program ends with 0 when it reaches the end of `main`.

### Step 2: Semicolons (fix)

Now there are two `console.println` lines, and line 2 has no `;` at its end.
Press Run.

This time the program doesn't run.
Lugha reads a line break the same as a space, so a statement ends at its `;`, not at the end of a line.
Without the `;`, line 2 runs on into line 3.
E0201 says so: it expected a `;` and found `console`, the first word of line 3.
`src/main.la:3:5` under it says where: the file, line 3, column 5.
Add the `;` at the end of line 2 and run again, or press Solve.

> **Error note (E0201):** Every statement ends with a `;`, and a line break doesn't end one. Line 2 has no `;`, so the statement runs on into line 3, and `console` is where the `;` should have been.

### Step 3: Comments (read)

`//` turns the rest of a line into a comment, as on line 2.
`/* … */` covers everything between its marks, even across lines, and these comments nest: line 3 opens one, and line 4 opens a second inside it.
Press Run.

Only `one` and `five` print.
The `*/` on line 4 closes the inner comment, so the outer one runs on to the `*/` on line 5, and lines 3 to 5 are all comment.
That's what lets you comment out code that already has a comment in it.

### Step 4: Exit codes (fix)

`main` can also give back a number: the program's exit code.
`: i32` on line 1 says so; `i32` is a type of whole number.
Line 3, `1`, has no `;`: the last line of a function's body, between its `{` and `}`, can be a value without a `;`, and that value is what the function gives back.
Press Run.

The output panel shows `checking the input`, then "Exited with code 1".
An exit code tells whatever started the program, such as a script, whether it worked: 0 means it did, and anything else means it failed.
Change line 3 to `0` and run again, or press Solve.

## 1.2 Values and types

### Step 1: Integer types (read)

Every value in Lugha has a type, and whole numbers have eight of them.
`i8`, `i16`, `i32` and `i64` can hold negative numbers, and `u8`, `u16`, `u32` and `u64` start at zero.
The number in each name is the type's size in bits.
`MIN` and `MAX` after a type's name are its smallest and largest values, and lines 2 to 5 print four of them.
Press Run.

Lines 2 and 3 print `-128` and `127`, the smallest and largest `i8`.
Line 4 prints `255`, the largest `u8`, and line 5 prints the largest `i64`.

### Step 2: Floating-point types (read)

Numbers with a fraction are floats, and there are two float types, `f32` and `f64`.
A number written with a point, like `2.0` on line 2, is an `f64`.
Line 3 is ten million billion written out in full, and line 4 prints `true`.
Press Run.

Line 2 prints `2.0`: a float always prints with its point, so you can tell it from a whole number.
Line 3's float is large enough to print with an exponent, `1.0e16`, which means 1.0 times 10 to the 16th.
Line 4's `true` is a `bool`, a type whose only values are `true` and `false`.

### Step 3: Integer literals (read)

However a whole number is written, it prints in plain decimal.
Line 2 groups its digits with `_`, and lines 3 to 5 write hex with `0x`, binary with `0b` and octal with `0o`.
Line 6 writes `017`, with a leading zero.
Press Run.

Warning W0107 comes first: a leading zero doesn't make a number octal, so `017` is seventeen.
Its location line points at line 6, and its help line suggests `0o17` for octal, or plain `17`.
A warning doesn't stop the program, so the numbers print after it.
Lines 2 to 5 give `1000000`, `255`, `10` and `15`, and line 6 gives `17`.

### Step 4: Float literals (fix)

Line 2 writes two hundred thousand with an exponent, as `2e5`: 2 times 10 to the 5th.
Press Run.

The program doesn't run.
`lughac` refuses `2e5` with E0107, "float literal needs a fractional part".
A number with an exponent is a float, and a float has to be written with a `.` and a digit after it, so `2e5` has to be `2.0e5`, as the help line says.
Write `2.0e5` on line 2 and run again, or press Solve.

> **Error note (E0107):** A number with an exponent is a float, and a float has to be written with a `.` and a digit after it. `2e5` has no `.`, so it's refused, and `2.0e5` is the float it was meant to be.

### Step 5: Characters and strings (fix)

Text has two types.
A `char` holds one character, in single quotes, as on line 2.
A `string` holds any text, in double quotes, and a `\` inside it starts an escape, such as `\t` for a tab on line 4.
`\u{…}` writes a character by its Unicode number in hex, in a `char` on line 3 and in a string on line 4.
The string that starts on line 5 runs on to line 6.
Press Run.

The program doesn't run, and E0102, "unterminated string", shows twice.
A string ends on the line it starts, so the string opened on line 5 never closes, and the `"` on line 6 is read as the start of another one.
The help line under each error gives the way to put a line break in a string: `\n`.
Join lines 5 and 6 into `"first line\nsecond line"` and run again, or press Solve.

## 1.3 Variables

### Step 1: Variable declaration (read)

Every value so far went straight into `console.println`.
`let` gives a value a name instead, and the name is a variable.
Line 2 gives `7` the name `width`.
Line 3 gives `3` the name `height`, and writes its type, `i64`, after a colon.
Line 4 uses the names where the values would go.
Press Run.

It prints `21`, `width` times `height`.
Line 2 has no type written, and doesn't need one: `lughac` works out a variable's type from its value.

### Step 2: Mutable variables (fix)

Line 2 declares `count` as `0`, and line 3 tries to give it a new value, `count + 1`, with `=`.
Giving a variable a new value is called assigning.
Press Run.

The program doesn't run: E0501 says "cannot assign to `count`: it is not mutable", at line 3.
A variable keeps the value it was given unless it's declared `let mut`, which makes it mutable, able to change.
The help line under the error says the same: `let mut count`.
Add `mut` after `let` on line 2 and run again, or press Solve.

> **Error note (E0501):** `count` was declared with `let`, so it keeps the `0` it was given, and line 3 can't give it a new value. A variable that changes is declared with `let mut`.

### Step 3: Assignment (fix)

Both `a` and `b` are `let mut` this time, and line 4 tries to set both to `0` in one go, with `a = b = 0`.
Press Run.

The program doesn't run: E0204 says "assignment is a statement, not an expression".
An expression gives a value, as `a + b` does, while a statement only does something.
An assignment is always a statement, so `b = 0` has no value for `a` to take.
The help line, "use `==` to compare", is for a different slip, `=` written by mistake for `==`, which compares two values; it doesn't apply here.
Split line 4 into two assignments, `a = 0;` and `b = 0;`, one per line, or press Solve.

> **Error note (E0204):** An assignment such as `b = 0` gives `b` a value but has no value of its own, so `a = b = 0` leaves nothing for `a` to take. Each assignment is a statement of its own.

### Step 4: Number literal types (fix)

A number written in the code, called a literal, takes its type from what's around it.
Nothing decides for line 2's `7`, so it gets `i64`, the default for a whole number; a number with a `.` gets `f64`.
Line 3 declares `height` as a `u8`, a whole number from 0 to 255, and line 4 multiplies it by `300`.
Press Run.

The program doesn't run: E0402 says "integer literal out of range for u8", pointing at line 4's `300`.
The `300` takes its type from `height` on the other side of the `*`, so it has to be a `u8`, which holds 0 to 255, as the help line says.
Arithmetic on two `u8`s gives a `u8`, so `scaled` is a `u8` too, and the result has to fit as well.
Change `300` to `30`, making 210, and run again, or press Solve.

> **Error note (E0402):** `300` is multiplied by `height`, a `u8`, so it has to be a `u8` too, and a `u8` holds only 0 to 255.

### Step 5: Shadowing (read)

There's another way to give a name a new value without `mut`: declare it again with `let`.
Line 3 declares `score` a second time, as the old `score` plus 5.
Line 5 declares it a third time, as a string.
Press Run.

Line 4 prints `15`.
The second `let` made a new variable that hides the first, which is called shadowing.
The new `score` exists from the end of its `let` line on, so `score + 5` on line 3 still reads the old one.
Line 6 prints `fifteen`: line 5 made a new variable again, so it can have a different type.
`let mut` can't do that, since assigning changes a variable's value but never its type.

### Step 6: Constants (read)

A value the whole program shares is a constant, declared with `const` outside any function, as on line 1.
A constant's type is always written, here `i64`.
Line 5 uses `MAX_SCORE` the way it would use a variable.
Press Run.

It prints `60`, `MAX_SCORE` minus `score`.
Nothing can assign to a constant: `MAX_SCORE = 5;` would be E0501, the error from step 2.
`let` isn't allowed outside a function, so a value the whole program shares is always a `const`, worked out once before `main` runs.

## 1.4 Operators and conversions

### Step 1: Integer division (read)

In the last lesson `height * 300` had to fit a `u8`, because arithmetic works on two numbers of the same type and gives that type.
So dividing two whole numbers gives a whole number.
Lines 2 and 3 divide whole numbers with `/`, and line 4 takes a remainder with `%`.
Line 5 divides two floats.
Press Run.

Line 2 prints `3`, without the half.
Line 3 prints `-3`: the fraction is dropped toward zero, not rounded down.
Line 4 prints `-1`, since a remainder takes its sign from the left side.
Line 5 prints `3.5`: the half is kept only when both sides are floats.

### Step 2: Conversion with as (fix)

Line 2 declares `total` as an `i32`, and line 3 tries to get half of it by dividing it by `2.0`.
Press Run.

The program doesn't run: E0401 says "float literal where i32 expected", pointing at the `2.0` on line 3.
The `2.0` takes its type from `total` on the other side of the `/`, as the `300` took its type from `height` in the last lesson, and a float can't be an `i32`.
So `total` has to become an `f64` first.
`as` converts a number to another type when nothing can be lost, and every `i32` has an exact `f64`.
`as` is worked out before `/`, so `total as f64 / 2.0` converts `total` and then divides.
Write `total as f64 / 2.0` in place of `total / 2.0` on line 3 and run again, or press Solve.

### Step 3: Narrowing conversions (fix)

`total` is `300`, an `i64`, and lines 3 and 4 convert it with `as` to a `u8` and an `f64`.
Lines 5 and 6 use methods, functions called on a value after a `.`.
Press Run.

The program doesn't run, and E0469 shows for each `as`.
`as` goes by the types, not the value: an `i64` can be too big for a `u8`, and some `i64` values are too large for an `f64` to hold exactly.
The help lines name methods that convert instead, with the target type in `<…>`, each named for what it does when a number doesn't fit.
`truncate<u8>()` keeps the lowest 8 bits, so `300` becomes `44`, and `round<f64>()` takes the nearest `f64`.
Line 5's `saturate<u8>()` stops at the largest `u8`, and line 6's `try_into<u8>()` gives an `Option`, a value that may be missing, and `is_some()` says whether it has one.
Put `total.truncate<u8>()` in place of `total as u8` on line 3 and `total.round<f64>()` in place of `total as f64` on line 4, or press Solve.

### Step 4: Integer overflow (read)

`level` is a `u8` holding 250.
Line 3 adds 5, which makes 255, the largest `u8`, and line 4 adds 10.
Press Run.

Line 3 prints `255`.
Line 4's sum, 260, doesn't fit in a `u8`, so the program stops there: it panics.
The panic's message, `integer overflow at src/main.la:4:27`, goes to stderr, the program's error output, and points at the `+` on line 4.
"Exited with code 101" is the code a panic exits with.
Whole-number arithmetic never keeps only the lowest bits the way `truncate` does, which would have turned 260 into 4: it stops instead.
Dividing a whole number by zero panics the same way.

### Step 5: Sizes in bytes (read)

Whole numbers have methods for sizes in bytes: `kb()` multiplies by 1024, `mb()` by 1024 twice, and `gb()` by 1024 three times.
Line 5 calls `kb()` on `pages`, a `u32`.
Press Run.

Line 2 prints `8192`, eight times 1024.
Line 3 prints `67108864`, 64 times 1024 times 1024.
Line 5 prints `3072`, and it's a `u32`, since the result keeps the type of the number the method is called on.

### Step 6: Comparison and logical operators (fix)

Comparisons such as `<=` and `<` give a `bool`.
Line 4 tries to check in one go that `age` is at least 18 and under 65, with `18 <= age < 65`.
Line 5 uses `!` for not and `||` for or.
Press Run.

The program doesn't run: E0203 says "`<=` and `<` can't be chained".
`18 <= age` gives a `bool`, and comparing that with `65` is never what was meant, so `lughac` refuses it.
The help line shows the way: two comparisons joined with `&&`, which means and; the parentheses it shows aren't needed.
`&&` and `||` stop as soon as the answer is known, so on line 5 `!member` is already `true`, and `age > 60` is never worked out.
Write `18 <= age && age < 65` on line 4 and run again, or press Solve.

# 2. Control flow and functions

## 2.1 Blocks and scopes

### Step 1: Block expressions (read)

In the first lesson, the last line of `main`, a value written without a `;`, was what `main` gave back.
Any block in braces works the same way.
Lines 2 to 6 are a block that declares `price` and `tax`, and the block's value goes into `total`.
Press Run.

Line 7 prints `46`.
A block's value is its last expression, written without a `;`, here `price + tax` on line 5.
An expression is any code that gives a value, such as `40` or `price + tax`.

### Step 2: Statements and () (fix)

Line 5 now ends with a `;`.
Press Run.

A `;` turns an expression into a statement, and a statement throws its value away: `price + tax;` works out `46` and drops it.
The block is left with no last expression, so it gives back `()`, a value that means nothing.

W0106 warns that `total` holds `()`, and its help names the fix: remove the semicolon.
E0422 on line 7 follows from that: `console.println` prints only values that have a text form, and `()` has none.
Its help suggests `.debug()`, but that would only print `()`: the fix is the `;`.

Remove the `;` on line 5 and run again, or press Solve.

> **Error note (E0422):** `console.println` needs a value with a text form, and `()` has none: it's what the block gave back once its last line ended in `;`.

### Step 3: Variable scope (fix)

Lines 2 to 5 are a block again, and `price` is declared inside it, on line 3.
Line 6, after the block's `}`, tries to print `price`.
Press Run.

The program doesn't run: E0301 says "cannot find `price` in this scope", at line 6.
A variable's scope is the part of the code where it exists, and a variable declared in a block ends at the `}` that closes it.
So `price` doesn't exist on line 6.
What's left of the block is its value, in `total`.
Print `total` on line 6 instead and run again, or press Solve.

> **Error note (E0301):** `price` was declared inside the block on lines 2 to 5, so it ends at the block's `}` on line 5. On line 6 there is no `price` to print.

## 2.2 if

### Step 1: if expressions (read)

Like a block, an `if` has a value: the value of whichever branch ran.
Lines 3 to 9 are one `if` that puts one of three strings into `advice`.
Line 3 checks `temperature > 30`, `else if` on line 5 checks a second condition when the first is false, and `else` on line 7 takes what's left.
Press Run.

It prints `stay inside`.
`temperature` is 31, so `temperature > 30` is true, line 4's string goes into `advice`, and the other branches are skipped.
Change `31` on line 2 to `25` or `10` and run again to see the other two.

### Step 2: Branch types (fix)

This `if` has two branches: line 4 gives a string, and line 6, in the `else`, gives `0`, a number.
Press Run.

The program doesn't run: E0403 says "`if` and `else` have different types", pointing at the `if` on line 3.
`advice` gets the type of the `if`, and an `if` has one type, so every branch has to give a value of that type.
`lughac` checks both branches before the program runs, even the one that won't be taken.
Change line 6 to a string, such as `"go out"`, and run again, or press Solve.

> **Error note (E0403):** Each branch of an `if` can give its value, so both have to give the same type. Line 4 gives a string and line 6 gives a number, and Lugha never turns one type into another on its own.

### Step 3: Boolean conditions (fix)

`unread` is `3`, and line 3 uses it as the `if`'s condition.
Press Run.

The program doesn't run: E0403 again, the code for a value of the wrong type, this time "expected bool, found i64", pointing at `unread` on line 3.
A condition must be a `bool`, and a number is never read as one, so the comparison with `0` has to be written out.
Write `unread > 0` on line 3 and run again, or press Solve.

> **Error note (E0403):** An `if`'s condition has to be a `bool`, `true` or `false`. `unread` is an `i64`, and a number is never read as a `bool`.

### Step 4: Braces and parentheses (fix)

Line 3 puts the condition in parentheses and leaves out the braces around the code that runs.
Press Run.

The program doesn't run: E0201 says "expected `{`, found identifier `console`", pointing at `console` on line 3.
Parentheses around a condition are optional, so `if (unread > 0)` means the same as `if unread > 0`.
Braces are not: the code after the condition is always a block in braces, even when it holds one line.
So is the code after `else`, unless it's another `if`.
Put line 3's `console.println` in braces and run again, or press Solve.

> **Error note (E0201):** The code after an `if`'s condition always goes in a block in braces. Line 3 has none, so `lughac` expected a `{` where `console` starts.

## 2.3 match

### Step 1: match expressions (read)

A `match` compares a value with a list of patterns.
Each arm, as on lines 4 to 7, is a pattern, then `=>`, then the value the `match` gives when that pattern matches.
The `_` on line 7 matches anything, so it catches every number the other arms don't.
Press Run.

It prints `Wednesday`.
`day` is `3`, so the arm on line 6 is the first whose pattern matches, and `name` becomes `"Wednesday"`.
Like an `if`, a `match` is an expression, and every arm must give the same type: a number in place of `"Tuesday"` would be E0401, "integer literal where string expected".
Change `3` on line 2 and run again to see the other arms.

### Step 2: Or-patterns (read)

An arm can also take more than one value.
Line 4 has two patterns, `6` and `7`, joined by `|`, and the arm matches when either does.
Press Run.

It prints `weekend`, since `day` is `6`.
Change `6` on line 2 to `7` and it still prints `weekend`, and any other number gives `weekday`.

### Step 3: Exhaustiveness (fix)

This `match` is on a string, `command`, with an arm for each of three commands, and `command` is `"stop"`.
Press Run.

The program doesn't run: E0417 says "non-exhaustive match: other values of `string` are not covered".
A `match` must cover every value `command` could hold, and `command` could be any string, not only the three the arms name.
It doesn't matter that `command` is `"stop"`: `lughac` checks the `match` before the program runs.
An integer has too many values to list as well, so a `match` on a string or an integer needs a last arm that catches the rest.
A `bool` doesn't need one, since `true` and `false` cover it.
Add the arm the help line names, `_ => 0,` as line 7 and run again, or press Solve.

> **Error note (E0417):** A `match` needs an arm for every value its subject could hold. `command` could be any string, and only three have arms, so a last arm such as `_` has to catch the rest.

### Step 4: Match guards (fix)

An arm can have a condition, called a guard, written after the pattern with `if`, as on lines 5 and 6.
There the pattern is a name, `t`, which matches any value and names it for the condition, and the arm matches only when the condition is true.
Press Run.

The program doesn't run: E0417 again, "non-exhaustive match: other values of `i64` are not covered".
Lines 4 to 6 cover every number, but `lughac` doesn't count arms with a guard, so it sees only `0` covered.
The help line asks for `_ => …` as the last arm, which has no guard and covers the rest.
A guard is also how an arm takes a span of numbers, such as 90 to 99, since a pattern can't.
Change line 6 to `_ => "above zero",` and run again, or press Solve.

> **Error note (E0417):** A `match` has to cover every value of `temperature`, and guarded arms don't count toward that, so every `i64` but `0` is left without an arm.

### Step 5: Unreachable arms (fix)

The arms from step 1 are here, with `_` moved to the top, as line 4, and `day` is still `3`.
Press Run.

Three W0102 warnings come first, "unreachable match arm", for lines 5, 6 and 7.
Arms are tried from the top, and `_` matches every number, so no value ever reaches the arms after it.
A warning doesn't stop the program, so it runs and prints `another day`, from line 4, though `day` is `3`.
Move the `_` arm from line 4 back to the end and run again, or press Solve.

## 2.4 Loops

### Step 1: while loops (read)

Where an `if` runs its block once, `while` checks its condition, runs its block if it's true, then checks again, until the condition is false.
`seconds` starts at `3`, and line 5 takes one off each time round.
`seconds -= 1` is short for `seconds = seconds - 1`, and `+=`, `*=` and the rest work the same way.
Press Run.

The loop on lines 3 to 6 runs three times, and line 4 prints `3`, `2` and `1`.
Then `seconds` is `0`, so `seconds > 0` is false, the loop ends, and line 7 prints `go`.

### Step 2: for loops over ranges (read)

`for` does the counting: `for i in 1..4` on line 2 runs its block once for each number in the range `1..4`, with `i` set to that number.
Press Run.

It prints `1`, `2` and `3`, and not `4`.
A range includes its first number and stops before its second, so `1..4` holds three numbers.

### Step 3: break and continue (read)

Both kinds of loop can be cut short from inside.
`continue` skips the rest of the block and goes on to the next turn, and `break` ends the loop.
Line 3 checks whether `i` is a multiple of 3, using `%` for the remainder and `==`, which checks that two values are equal, and if it is, line 4 skips it.
Line 7 ends the loop once `i` is over 7, though the range goes up to 9.
Press Run.

It prints `1`, `2`, `4`, `5` and `7`: `continue` skipped `3` and `6`.
When `i` reaches 8, `break` ends the loop before line 9 can print it.

### Step 4: loop and break with a value (read)

`loop` runs its block again and again until something leaves it, usually a `break`.
Like `if` and `match`, it's an expression, and `break n;` on line 6 ends it with `n` as its value, which goes into `first`.
Line 4 doubles `n` each time round, and line 5 checks whether it has passed 100.
Press Run.

It prints `128`, the first doubling of 1 to pass 100.
Only a `loop` gives a value this way: `break` with a value inside a `while` or `for` is E0514 and won't compile, because those loops can also end without reaching a `break`.

### Step 5: Loop labels (fix)

One `for` runs inside another: for each `row` on line 2, the loop on line 3 goes through each `col`.
Line 7 prints the pair, and `{row}` and `{col}` put each number into the text.
Line 5's `break` is meant to stop everything at the first pair whose product is 4.
Press Run.

It prints seven pairs.
Row 1 prints `1 1`, `1 2` and `1 3`.
Row 2 prints `2 1`, then `2 2` makes 4 and the `break` runs.
A `break` ends only the loop it's in, the inner one, so the outer loop goes on to row 3, which prints `3 1`, `3 2` and `3 3`.
To leave the outer loop, give it a label, a name followed by `:`, before its `for`, and write that name after `break`.
`continue outer;` works the same way, going on to the outer loop's next turn.
Add `outer:` before `for` on line 2 and `outer` after `break` on line 5, then run again, or press Solve.

## 2.5 Functions

### Step 1: Function declaration (read)

So far `main` has been the only function, and a new one is declared the same way, with `fun`.
Line 1 declares `area`: after its name come its parameters, `width` and `height`, each with its type, and after the `)` a `:` and its return type, the type it gives back.
Its body on line 2 gives back `width * height`, its last expression.
Line 6 calls `area` with `7` and `3`.
Press Run.

It prints `21`.
`area` comes first here, but the order of functions in a file doesn't matter, so `main` could be at the top instead.
`lughac` works out a `let`'s type from its value, but a function's parameter types are always written, and so is its return type when it gives a value back.
Leave the return type off, as `main` does on line 5, and the function gives back `()`, which means nothing.

### Step 2: Return values (fix)

`area`'s body is a block, so what it gives back is its last expression.
Line 2 now ends with a `;`.
Press Run.

The program doesn't run: E0503 says "`area` may end without returning a value of type i64", pointing at the name `area` on line 1.
Returning a value means giving it back.
Line 1 promises an `i64`, but the `;` makes `width * height` a statement, which throws its value away, so the body no longer gives one.
The help line says the same, "remove this semicolon to make it the result", though its location points at `area`: the semicolon is the one on line 2.
Remove the `;` on line 2 and run again, or press Solve.

> **Error note (E0503):** Line 1 says `area` gives back an `i64`, but the `;` on line 2 throws `width * height` away, so the body ends with no value to give back.

### Step 3: Expression bodies (read)

A body that is a single expression can be written after `=` instead of between braces, as on line 1.
Press Run.

It prints `21` again: `= width * height;` means the same as a body in braces holding `width * height`.
Here the final `;` ends the declaration, so it doesn't throw the value away the way the `;` in step 2 did.
The return type, `: i64`, is still written in this form.

### Step 4: Immutable parameters (fix)

`with_tax` takes a `price`, and line 2 tries to add a tenth to it.
Press Run.

The program doesn't run: E0501 says "cannot assign to `price`: it is not mutable", at line 2.
A parameter is like a variable declared with `let` and no `mut`: it can't be given a new value.
The help line suggests shadowing, from the Variables lesson.
`let mut price = price;` declares a new, mutable `price` from the parameter, and from the next line on, `price` means the new one.
Add `let mut price = price;` as a new line 2 and run again, or press Solve.

> **Error note (E0501):** `price` is a parameter, and a parameter can't be given a new value, as a `let` without `mut` can't. Declare a mutable copy first with `let mut price = price;`.

### Step 5: No overloading (fix)

Lines 1 and 3 both declare a function called `area`, one with two parameters and one with one.
Line 6 calls `area` with two numbers, and line 7 calls it with one.
Press Run.

The program doesn't run, and there are two errors.
E0302 says "`area` is defined more than once", at line 3: two functions can't share a name, whatever their parameters.
E0405 says "`area` takes 2 arguments but 1 was given", at line 7.
An argument is a value passed in a call, and line 7 reached the `area` on line 1, which takes two.
A parameter can't have a default value either, so each way of calling needs its own function.
Rename the second one `square_area` on lines 3 and 7 and run again, or press Solve.

> **Error note (E0302):** Line 1 already declares a function called `area`, so line 3 can't declare another, even with different parameters. Each function in a file needs its own name.

### Step 6: Passing the console (fix)

`greet`, on lines 1 to 3, prints a line with `console.println`, and `main` calls it on line 6.
Press Run.

The program doesn't run: E0301 says "cannot find `console` in this scope", at line 2.
`console` is a parameter of `main`, and a parameter belongs to its own function, the way a variable declared in a block belongs to that block.
A function prints only through a `Console` it's given.
So `greet` needs a `console: Console` parameter of its own, and `main` passes it the console it was given.
Write `console: Console` between the parentheses on line 1 and `console` between them on line 6, then run again, or press Solve.

> **Error note (E0301):** `console` is a parameter of `main`, so it exists only inside `main`. `greet` has no parameter called `console`, so on line 2 there is nothing by that name.

## 2.6 Return and recursion

### Step 1: Early return (read)

So far a function's value has been its last expression.
`return` ends a function straight away and gives back the value after it.
In `distance`, line 2 checks whether `to` is smaller than `from`, and if it is, line 3 returns `from - to` and the rest of the body is skipped.
Otherwise the function goes on to line 5, its last expression.
Press Run.

It prints `7` twice.
Line 9's call goes on to line 5, and line 10's returns on line 3.
`return to - from;` on line 5 would work too, but a function that reaches its end gives back its last expression without needing `return`.

### Step 2: Return checking (fix)

Now the body is two `if`s, on lines 2 and 5, each holding a `return`, and every call takes one of them, since `to` is either smaller than `from` or not.
Press Run.

The program doesn't run: E0503 says "`distance` may end without returning a value of type i64".
An `if` without an `else` never counts as returning, whatever its condition, so `lughac` sees a way to reach the `}` on line 8 with nothing to give back.
The help line gives two ways out: end the body with a value, or `return` on every path.
An `if` with an `else` would count when both branches return.
Replace lines 5 to 7 with `to - from` and run again, or press Solve.

> **Error note (E0503):** `distance` promises an `i64`, and `lughac` never counts an `if` without an `else` as returning, whatever its condition. So it sees a way past both `if`s to the `}` on line 8 with no value to give back.

### Step 3: Returning from a loop (fix)

A loop can hide the same problem.
`first_over` doubles `n` on line 4 until it passes `limit`, and returns it on line 6, from inside a `while true` loop.
The condition is always true, so the loop can only end at the `return`.
Press Run.

The program doesn't run: E0503 again, "`first_over` may end without returning a value of type i64".
`lughac` never counts a `while` loop as returning, even `while true`: as with the two `if`s in step 2, it doesn't look at the condition.
The help line names the way out: a `loop` that no `break` leaves does count, since the only way out is the `return`.
Its "spec §6" is the section of the Lugha specification that sets this rule.
Write `loop` in place of `while true` on line 3 and run again, or press Solve.

### Step 4: Recursion (read)

A function can also call itself, which is called recursion.
`factorial` on line 1 multiplies `n` by `factorial(n - 1)`, a call to itself.
One path has to give a value without calling the function again, or the calls never stop: here, when `n` is `1` or less, the `if` gives `1`.
The body is one `if` expression, so it uses the `=` form from the Functions lesson.
Press Run.

It prints `120`, which is 5 × 4 × 3 × 2 × 1.
`factorial(5)` calls `factorial(4)`, and so on down to `factorial(1)`, which gives `1` and makes no more calls.

# 3. Arrays, strings and tuples

## 3.1 Arrays

### Step 1: Array literals (read)

An array holds values of one type, in order.
Line 2 writes one as a list in square brackets.
Line 3 uses the other form, `[value; count]`: four elements, each a copy of `0`.
`.len` is the number of elements, written without parentheses, and lines 4 and 5 print it for each array.
Press Run.

The output panel shows `3` for `scores` and `4` for `zeros`, then "Exited with code 0".
`scores` has the type `i64[]`, an array of `i64`: nothing gives its numbers a type, so they're `i64`.

### Step 2: Printing arrays (fix)

Lines 4 and 5 now give `console.println` the arrays themselves.
Press Run.

This time the program doesn't run.
`console.println` prints only values that have a text form of their own, and an array has none.
The first E0422 says so for `scores` on line 4: `i64[]` doesn't implement `Display`, the text form `console.println` needs.
The second says the same for `zeros` on line 5.
Each help names the way out: `.debug()` gives an array's debug form, a string that shows its elements the way a programmer reads them, and `console.println` can print that.
Add `.debug()` after `scores` on line 4 and after `zeros` on line 5, then run again, or press Solve.

> **Error note (E0422):** `console.println` prints only values with a text form of their own, and an array has none. `.debug()` turns the array into a string that shows its elements.

### Step 3: Indexing (fix)

Line 2 declares `scores` with plain `let`.
Line 3 sets `scores[1]`, the element at index 1, to `88`: indexes count from `0`, so that's the second element.
Line 4 prints the first, `scores[0]`.
Press Run.

The program doesn't run.
E0501 says "cannot assign to `scores`: it is not mutable", at line 3.
Changing one element changes the array, so the array needs `let mut`, like any variable that changes, and the help shows it: `let mut scores`.
Add `mut` after `let` on line 2 and run again, or press Solve.

### Step 4: Bounds checking (fix)

Line 3 prints the first score, `scores[0]`.
Line 4 tries to print the last one with `scores[scores.len]`, and `scores.len` is `3`.
Press Run.

This program compiles and starts, and line 3 prints `70`.
Then line 4 asks for index 3, and there's no element there: the three elements are at indexes 0, 1 and 2.
The program panics, stopping with "index out of bounds: the length is 3 but the index is 3" and where it happened, `src/main.la:4:27`.
It exits with code 101.
The last index is always `.len - 1`.
Change line 4's index to `scores.len - 1` and run again, or press Solve.

### Step 5: push and clear (read)

An array can grow and shrink.
`push` on line 3 adds `"bread"` at the end of `list`, and `clear` on line 6 removes every element.
Both change `list`, so line 2 declares it with `let mut`.
Press Run.

Line 4 prints `["milk", "bread"]`: inside a debug form, a string keeps its quotes.
Line 5 prints `2`, the length after the `push`, and line 7 prints `0`, the length after the `clear`.

### Step 6: Empty arrays (fix)

Line 2 now starts `list` empty, with `[]`, and line 3 pushes a string into it.
Press Run.

The program doesn't run.
`[]` has no elements, so it says nothing about what the array will hold, and `lughac` works out a type only from what's written there, not from line 3.
E0412 says it "cannot infer the element type of `[]`" on line 2.
Its help shows the way out for an array of `i64`: write the type after a colon, as in `let xs: i64[] = [];`.
This list holds strings, so its type is `string[]`.
Add `: string[]` after `list` on line 2 and run again, or press Solve.

> **Error note (E0412):** `[]` has no elements to take a type from, and `lughac` won't work one out from the lines after it, so the array's type has to be written.

### Step 7: for … of loops (fix)

Line 3 tries to loop over `scores` with `for score in scores`, the way the Loops lesson counted over a range such as `0..3`.
Press Run.

The program doesn't run.
After `in`, `lughac` expects a range, so it reads `scores` as the start of one and looks for the `..` that should follow.
It finds `{` instead, and E0201 says "expected `..`, found `{`" at line 3, column 25.
A loop over an array uses `of` where a range uses `in`: `for score of scores` gives `score` each element in turn.
A `for … of` loop goes over the array as it was when the loop began.
So the loop's body may push onto a `let mut` array, and the loop still ends.
Change `in` to `of` on line 3 and run again, or press Solve.

> **Error note (E0201):** After `in`, a `for` loop expects a range like `0..3`, so `scores` reads as the start of one and `{` comes where `..` should be. A loop over an array uses `of` instead of `in`.

### Step 8: Changing elements in a loop (fix)

Line 2 declares `scores` with `let mut`, and line 4 tries to add 5 to each score as the loop goes through them.
Press Run.

The program doesn't run.
E0501 points at `score` on line 4, not at `scores`: "cannot assign to `score`: it is not mutable".
`score` is the loop variable, and a loop variable can't change.
The help suggests copying it into a `let mut`, but adding to a copy would leave the array as it was.
To change the elements, loop with `of mut`: then `score` is each element itself, so adding to it changes the array.
While a `for … of mut` loop runs, the array can't grow or shrink, and `scores.push(1)` inside it is E0507.
Add `mut` after `of` on line 3 and run again, or press Solve.

> **Error note (E0501):** `score` holds each element in turn, and in a plain `for … of` loop it can't be changed. With `of mut`, `score` is each element itself, and changing it changes the array.

### Step 9: Array concatenation and equality (read)

`+` on line 4 joins two arrays of the same type into a new one, and line 5 prints it.
Line 6 compares the result with `[1, 2, 3]`, using `==`.
Press Run.

Line 5 prints `[1, 2, 3]`.
Line 6 prints `true`, because `==` compares two arrays element by element, in order.

### Step 10: debug (read)

`debug(x)` on line 3 writes `x` to standard error, with the file and line, and then gives `x` back.
Standard error is a second output, kept apart from what `console.println` prints, for messages about the program, and the output panel shows it too.
`debug` needs no `Console`, so any function can use it, and because it gives back the value it can sit inside an expression, as `debug(price * 3) + 1` does.
Press Run.

Line 4 prints `31`.
The output panel shows the program's standard output first and its standard error after it, so the line `debug` wrote comes after `31`, though `debug` ran first.
That line is `[src/main.la:3] price * 3 = 30`, the file and line, the expression, and its value.
`debug` gave back `30`, so `total` is `30 + 1`.
`.debug()` gives back a string to print, and `debug(x)` writes the value out itself and gives back the value.

## 3.2 Strings and characters

### Step 1: String interpolation (read)

A string can hold values: line 4 puts `name` and `points` inside it, each in braces.
Each pair of braces is replaced by the value of what's inside it, written the way `console.println` would print it.
The braces can hold any expression, such as `points * 2` on line 5.
Press Run.

Line 4 prints `Amina has 7 points`, and line 5 prints `doubled: 14`.
A value with no text form of its own, such as an array, needs its `.debug()` inside the braces, as it does in `console.println`.

### Step 2: Format specifiers (read)

A `:` after the expression in braces starts a format specifier, which changes how the value is written.
Line 3 prints `share` as it is, and line 4 adds `:.2`, which asks for two decimals.
Lines 5 to 8 use other specifiers on whole numbers.
Press Run.

Line 3 prints `0.6666666666666666`, and line 4 rounds it to `0.67`; a precision like `.2` works only on floats.
Lines 5 and 6 ask for a width of 6 characters, shown inside the square brackets: `>` puts `42` at the end of the six, and `<` at the start.
On line 7, the `0` before the width 3 pads `7` with zeros, giving `007`.
On line 8, `x` writes `255` in hex, and `#` puts `0x` in front: `0xff`.

### Step 3: Escaping braces (fix)

Line 2 means to print the text `{name}`, braces and all.
Press Run.

The program doesn't run.
A single `{` in a string starts an interpolation, so `lughac` reads `name` as an expression and looks for a variable with that name.
There's none, and E0301 says "cannot find `name` in this scope", at line 2, column 29.
To write a brace itself, double it: `{{` gives `{`, and `}}` gives `}`.
Change `{name}` on line 2 to `{{name}}` and run again, or press Solve.

> **Error note (E0301):** Inside a string, `{name}` puts in the value of a variable called `name`, and this program has none. A brace meant as text is written twice.

### Step 4: String concatenation (fix)

`+` also joins two strings into a new one.
Line 4 tries to build a sentence with it, from `name`, `" has "` and `points`, which is an `i64`.
Press Run.

The program doesn't run.
E0404 says "cannot apply `+` to string and i64", at line 4.
`+` joins only strings, and a number never turns into a string by itself.
Braces in a string do turn it into text, so the number can go inside the string instead.
On line 4, drop `+ points` and change `" has "` to `" has {points}"`, then run again, or press Solve.

> **Error note (E0404):** `+` joins two strings, and `points` is a number, which `+` won't turn into text. Put it inside the string in braces instead.

### Step 5: String length (read)

A string's `.len` is read without parentheses, like an array's, and line 3 prints it for `Zoë`, a name of three letters.
Line 4 calls `char_count()`, a method, so it has parentheses.
Press Run.

Line 3 prints `4`, because `.len` counts bytes: a string's text is stored as UTF-8, where `Z` and `o` take one byte each and `ë` takes two.
Line 4 prints `3`, because `char_count()` counts characters.

### Step 6: Bytes (read)

Indexing a string counts in bytes too, like `.len`.
Line 3 prints `word[0]`, the first byte of `"hi"`, and the loop on lines 4 to 6 goes through `word` with `for … of`.
Press Run.

Line 3 prints `104`, not `h`: `word[0]` is a `u8`, a byte, and `104` is the byte that stands for `h`.
The loop gives the bytes in turn, so it prints `104` for `h` and `105` for `i`.

### Step 7: String methods (read)

Most work on a string goes through its methods.
Line 3 takes the spaces off both ends with `trim`, then cuts the result at each comma with `split`, which gives a `string[]`.
`join` on line 5 puts an array of strings back together, with `" + "` between them.
`contains` on line 6 and `starts_with` on line 7 each give a `bool`, and `lines` on line 8 splits a string at each `\n`.
Press Run.

Line 4 prints the three items, `["milk", "bread", "eggs"]`, and line 5 prints `milk + bread + eggs`.
Lines 6 and 7 print `true`.
None of these methods changes the string it's called on: `line` still has its spaces on line 7, so it's trimmed again there.
Line 8 prints `["one", "two"]`.

### Step 8: Slicing (read)

`slice(from, to)` gives the part of a string from byte `from` up to, but not including, byte `to`, counted like `.len`.
In `Zoë`, `Z` and `o` are bytes 0 and 1, and `ë` takes bytes 2 and 3.
Line 5 cuts at byte 3, inside `ë`, and prints only the `.len` of what it gets.
Press Run.

Line 3 prints `Zo`, and line 4 prints `ë`.
Line 5 prints `3`: `slice` panics only when the offsets are out of order or past `.len`, so the cut goes through and gives `Z`, `o` and half of `ë`.
Those 3 bytes end inside `ë` and aren't valid UTF-8.
The site can't show output that isn't valid UTF-8, so line 5 prints their length instead of the text.

### Step 9: The char type (read)

A single character has its own type, `char`, written in single quotes, as `'b'` on line 2.
`grade < 'c'` on line 3 compares two characters by their Unicode numbers.
Lines 4 to 8 call two of `char`'s methods, `is_digit()` and `to_upper()`.
Press Run.

Line 3 prints `true`, since `b` comes before `c`, and line 4 prints `true`, since `'7'` is a digit.
Line 5 prints `B`.
`to_upper()` works only within ASCII and Latin-1, so line 6 turns `'é'` into `É`.
Line 7's `'ß'` is in Latin-1 but stays `ß`, because its capital, `ẞ`, is outside Latin-1.
Line 8's Cyrillic `'ж'` is outside both, so it comes back unchanged.

## 3.3 Tuples and destructuring

### Step 1: Tuples (read)

A tuple groups a fixed number of values, and each can have its own type.
Line 2 makes one from a string and a number, in parentheses.
Like an array, a tuple has no text form of its own, so line 3 prints it through `.debug()`, and `console.println(item)` alone would be E0422.
Lines 4 and 5 read its elements by position, with `.0` and `.1`.
Press Run.

Line 3 prints `("milk", 2)`: in the debug form, the string keeps its quotes.
Line 4 prints `milk` without them, since `item.0` is the string itself.
Line 5 prints `2`.

### Step 2: Multiple return values (read)

A function can give back more than one value by returning a tuple.
`divmod` on line 1 gives back the quotient and the remainder of `a / b` together, so its return type is the tuple type `(i64, i64)`.
A tuple type lists each element's type, so step 1's `item` has the type `(string, i64)`.
Line 4 calls `divmod`, and `result` holds both values.
Press Run.

Line 5 prints `(3, 2)`: 17 divided by 5 is 3, with 2 left over.

### Step 3: Destructuring with let (fix)

Instead of `.0` and `.1`, a `let` can give each element of a tuple a name of its own.
Line 4 tries to name both parts of `divmod(17, 7)` with `let mut (weeks, days)`, so that line 5 can add a day.
Press Run.

The program doesn't run.
E0201 says "expected variable name, found `(`" at line 4, column 13, the `(` right after `mut`.
`mut` can't go before the parentheses: it goes inside them, before each name that will change, and here only `days` changes.
Change the start of line 4 to `let (weeks, mut days)` and run again, or press Solve.

> **Error note (E0201):** After `let mut`, `lughac` expects a variable name, so the `(` doesn't fit there. To make one of the names in parentheses changeable, put `mut` before that name, inside them.

### Step 4: Destructuring in loops (read)

The same parentheses work after `for`.
`people` on line 2 is an array of tuples, each a name and an age.
Line 3 gives the two elements of each tuple the names `name` and `age` as the loop reaches it.
Press Run.

The loop prints one line for each tuple: `Ann is 31`, then `Ben is 25`.

### Step 5: Tuple patterns (read)

A `match` can look inside a tuple too.
Line 2 puts `x` and `y` into one, so that a single `match` checks both.
Each arm's pattern is a tuple of patterns, and `_` inside one matches anything in that position: `(0, _)` on line 4 matches any point whose `x` is `0`, the origin included.
Arms are tried from the top, so `(0, 0)` on line 3 comes first, or the origin would land in the y-axis arm.
The `_` on line 6 covers every other case, as a `match` must.
Press Run.

Line 11's `describe(0, 4)` matches `(0, _)`, so it prints `on the y axis`.
Line 12's `describe(2, 3)` matches none of the first three arms and lands in `_`, so it prints `somewhere else`.

# 4. Structs and enums

## 4.1 Structs

### Step 1: Struct declaration (read)

A struct is a type you declare yourself, made of named fields.
Line 1 declares `Point`, a struct with two fields, `x` and `y`, each with its type.
It's declared at the top level, outside `main`, and it can be used as a type, like `i64`.
Line 4 builds a `Point`, giving each field a value by name, and `p.x` on line 5 reads the field `x`.
Press Run.

Line 5 prints `3`, the value of `p.x`, and line 6 prints `4`, the value of `p.y`.

### Step 2: Printing structs (fix)

Line 5 now gives `console.println` the struct `p` itself.
Press Run.

The program doesn't run.
A struct has no text form of its own, as an array has none, so E0422 says `Point` doesn't implement `Display`, at line 5.
The help names two ways out.
The first, `impl Display for Point { … }`, writes a text form for `Point`, with code that later lessons teach.
The second, `.debug()`, works for a struct as it does for an array.
A struct's debug form is its name, then each field and its value in braces, in the order `Point` declares them.
Add `.debug()` after `p` on line 5 and run again, or press Solve.

> **Error note (E0422):** `console.println` prints only values with a text form of their own, and a struct you declare has none until you write one. `.debug()` turns `p` into a string that shows its fields.

### Step 3: Struct literals (fix)

`Point { x: 3, y: 4 }` is a struct literal: the type's name, then a value for each field, in braces.
Line 4 now writes one with only `x`.
Press Run.

The program doesn't run.
A field has no default value, so a struct literal has to give every field one, in any order.
E0413 says "missing field `y` in `Point`", at line 4.
Add `, y: 0` after `x: 3` on line 4 and run again, or press Solve.

### Step 4: Field assignment (fix)

Line 5 changes one field with `p.x = 5`, and line 4 declares `p` with plain `let`.
Press Run.

The program doesn't run.
E0501 names `p` itself, not the field: "cannot assign to `p`: it is not mutable".
A field has no `mut` of its own, so changing a field changes the struct, and the variable that holds it needs `let mut`, as the help shows.
Add `mut` after `let` on line 4 and run again, or press Solve.

### Step 5: Struct update syntax (read)

Another way to get a changed point is to build a new one from the old.
Line 5 writes `x` and ends with `..p`, which takes every field not written, here `y`, from `p`.
`..p` has to come last, after the fields that are written.
Press Run.

Line 6 prints the new point, `Point { x: 10, y: 4 }`.
Line 7 prints `p` as it was, `Point { x: 3, y: 4 }`: `..p` copies from `p` and leaves it alone.

### Step 6: Struct equality (fix)

Line 6 compares two points with `==`.
Press Run.

The program doesn't run.
`==` and `!=` need a type that implements `Eq`, and E0422 says `Point` doesn't, at line 6.
The help's first way out is `with Eq` after `Point`'s declaration.
That gives `Point` both `==` and `!=`, and `==` then compares two points field by field.
Add `with Eq` after the `}` on line 1 and run again, or press Solve.

> **Error note (E0422):** `==` works on a struct only when its declaration asks for it, and `Point`'s doesn't. `with Eq` after the declaration lets two points be compared, field by field.

### Step 7: Struct literals in conditions (fix)

`Point` on line 1 now has `with Eq`, and line 5 checks with `==` whether `p` is the origin.
Press Run.

The program doesn't run.
In an `if` condition, the `{` after `Point` could start the struct literal or the `if`'s block.
E0205 says "struct literal in a condition must be in parentheses", at line 5.
Parentheses around the literal settle it, as the help shows: `(Point { … })`.
Put `Point { x: 0, y: 0 }` on line 5 in parentheses and run again, or press Solve.

## 4.2 Methods

### Step 1: Methods (read)

A method is a function that belongs to a type, declared inside an `impl` block for it, as on lines 3 to 5.
Its first parameter is `self`, the value the method is called on, written without a type.
Line 9 calls it with a dot, `p.length_squared()`, so inside the method `self` is `p`.
Press Run.

It prints `25`, which is `3 * 3 + 4 * 4`.

### Step 2: mut self methods (fix)

`self` can't change, like any parameter, so a method that changes the value it's called on takes `mut self` instead, as `shift` does on line 4.
Line 11 calls `shift` on `p`, and line 10 declares `p` with plain `let`.
Press Run.

The program doesn't run.
E0501 says "cannot call `mut self` method `shift` on `p`: it is not mutable", at line 11.
A `mut self` method changes the value it's called on, so `p` needs `let mut`, as it does when one of its fields is assigned.
Add `mut` after `let` on line 10 and run again, or press Solve.

> **Error note (E0501):** `shift` takes `mut self`, so calling it on `p` changes `p`, and `p` was declared with plain `let`. A value a method changes needs `let mut`, like one you assign to.

### Step 3: Associated functions and Self (read)

A function in an `impl` block without `self` is an associated function, and it's called on the type's name, as `Point.new(3, 4)` on line 10.
`new` is an ordinary name, chosen by whoever writes the type, and here it builds a `Point` from its two fields.
Inside the `impl`, `Self` stands for `Point`, both as a type and before a struct literal, as on line 4.
`origin` on line 6 calls `new` the same way, as `Self.new(0, 0)`.
Press Run.

Line 10 prints `Point { x: 3, y: 4 }`, and line 11 prints `Point { x: 0, y: 0 }`, the point `origin` builds.

### Step 4: Passing a value to its own mut method (fix)

`add` on line 4 is a `mut self` method that adds another point, `other`, to `self`.
Line 12 tries to add `p` to itself, with `p.add(p)`.
Press Run.

The program doesn't run.
E0508 says "cannot pass `p` to a `mut self` method called on `p`", at line 12.
The help says to copy it first: `let w = p;` makes a separate copy of `p`, and `w` can be passed instead.
Change line 12 to `p.add(w);`, then add `let w = p;` on a new line before it, and run again.
Or press Solve.

> **Error note (E0508):** `p.add(p)` gives `add` the same `p` it changes as `self`, and that isn't allowed. A copy made with `let` can be passed instead.

## 4.3 Enums

### Step 1: Enum declaration (read)

An enum is a type whose value is one of a list of variants.
`Shape` on lines 1 to 5 has three: a circle with a radius, a rectangle with a width and a height, or empty.
Each variant lists the types of the data it carries, if any, in parentheses.
A variant is built through its enum's name and a dot, as `Shape.Circle(2.0)` on line 8 and `Shape.Rect(1.0, 2.0)` on line 9.
A variant with no data, like `Shape.Empty` on line 12, has no parentheses.
Press Run.

Each line prints a variant's debug form, which is its name and its data, without the enum's name: `Circle(2.0)`, `Rect(1.0, 2.0)` and `Empty`.

### Step 2: Matching on enums (read)

A `match` can reach a variant's data: names in a pattern's parentheses are given the data, so `.Circle(r)` on line 9 names the radius `r`.
A variant in a pattern has a leading dot and no enum name before it, as on lines 9 to 11.
A name without a dot would be a new variable that matches anything, like `t` in `t if t < 0 =>`.
The arms must cover every variant: without the `.Empty` arm on line 11, E0417 would say "`.Empty` not covered".
Press Run.

Line 16 prints `12.56`, the area of a circle of radius 2.0.
Line 17 prints `2.0`, the area of a 1.0 by 2.0 rectangle.

### Step 3: Recursive enums (read)

A variant's data can be the enum itself.
`List` on lines 1 to 4 is either `Nil`, the end, or `Cons`, a number followed by the rest of the list.
`Cons` on line 3 has `List` as its second type, written the same way as `i64`.
Line 14 builds the list `1`, `2`, `3` by nesting: the innermost value is `List.Nil`, and each `Cons` puts one number in front of it.
`sum` on lines 6 to 11 adds each number to the sum of the rest, calling itself until it reaches `.Nil`, which gives 0.
Press Run.

Line 15 prints the nested debug form, `Cons(1, Cons(2, Cons(3, Nil)))`, and line 16 prints the sum, `6`.

## 4.4 Option

### Step 1: Option instead of null (read)

A value that may be missing has the type `Option`, an enum with two variants: `Some`, with the value inside, or `None`.
There's no null in Lugha, so an `Option` is how a missing value is written.
`find` on line 1 gives back a name's position in `names`, and there's no position when the name isn't there, so its return type is `Option<i64>`, an `Option` that holds an `i64`.
Line 4 returns `Some(i)` when the name is found, and line 7 gives `None` once the loop ends without it.
Unlike `Shape`'s variants, `Some` and `None` can be written without the enum's name in front.
Press Run.

An `Option` prints through `.debug()`, as `Shape` did.
Line 12 prints `Some(1)`, since `"Ben"` is at index 1, and line 13 prints `None`, since `"Dee"` isn't in the array.

### Step 2: Matching on Option (fix)

`Option` is an enum, so a `match` gets at the value inside, as it did for `Shape`.
Line 13 matches on what `find` gives back for each name, and `.Some(i)` on line 14 names the position `i`.
Press Run.

The program doesn't run.
A `match` has to cover every variant, and nothing here says what happens when a name isn't found.
E0417 says "non-exhaustive match: `.None` not covered", at line 13.
The missing arm is `.None`: `None` is built without a dot, but every variant in a pattern has its dot, `Some` and `None` included.
Add `.None => console.println("{wanted} isn't there"),` as a new line after line 14 and run again, or press Solve.

### Step 3: Typing None (fix)

`first_big` on line 2 starts as `None`, because no number over 6 has been found yet.
Line 5 sets it to `Some(n)` when the loop finds one.
Press Run.

The program doesn't run.
A bare `None` doesn't say what type a `Some` would hold, and, as with an empty array, `lughac` doesn't look ahead to line 5 for it.
E0412 says "cannot infer the type of `None`", at line 2.
The help shows the type written after a colon: `let x: Option<i64> = None;`.
Add `: Option<i64>` after `first_big` on line 2 and run again, or press Solve.

> **Error note (E0412):** A bare `None` says nothing about what a `Some` would hold, and `lughac` won't work it out from line 5, so the type has to be written.

### Step 4: unwrap_or, is_some and is_none (read)

`is_none()` on line 12 and `is_some()` on line 13 say which variant an `Option` is, as a `bool`, without a `match`.
`unwrap_or(-1)` gives the value inside a `Some`, or `-1` for a `None`.
Press Run.

Line 12 prints `true`, since `"Dee"` isn't found, and line 13 prints `true`, since `"Ben"` is.
Line 14 prints `1`, the value inside `Some(1)`, and line 15 prints `-1` for the missing name.

### Step 5: Parsing numbers (fix)

`parse_i64` reads a string that is only a whole number, with an optional `-` in front.
Its result is an `Option<i64>`: `Some` with the number, or `None` for text such as `"4.5"` or `"nine"`.
Line 3 parses `"41"`, and line 4 adds `1` to what it gave back.
Press Run.

The program doesn't run.
E0404 says "cannot apply `+` to `Option<i64>` and i64", at line 4: the number is still inside the `Option`.
`unwrap_or(0)` takes it out, with `0` standing in when the text isn't a number.
Add `.unwrap_or(0)` after `parse_i64(typed)` on line 3 and run again, or press Solve.

> **Error note (E0404):** `n` is an `Option<i64>`, not a number, so `+` can't add `1` to it. Take the number out first, with `unwrap_or`.

### Step 6: pop (read)

`pop` removes the last element of an array and gives it back in a `Some`, or gives `None` when the array is empty.
Like `push`, `pop` changes the array, so line 2 declares `stack` with `let mut`.
`stack` holds two numbers, and lines 3 to 5 pop three times.
Press Run.

Lines 3 and 4 print `Some(2)` and `Some(1)`, the last element first.
The third `pop` finds the array empty and prints `None`: popping an empty array isn't an error.
Line 6 prints the array, `[]`, empty now.

### Step 7: Checked arithmetic (fix)

`level` on line 2 is a `u8`, which holds 0 to 255.
Line 3 adds 5 to it, and line 4 adds 10.
Press Run.

Line 3 prints `255`.
Then line 4 panics with `integer overflow`, since 260 doesn't fit in a `u8`, and the program exits with code 101.
`checked_add` does the same addition and gives an `Option`: `Some` with the sum, or `None` where `+` would panic, so the program goes on.
On line 3, write `level.checked_add(5).debug()` in place of `level + 5`, and on line 4, `level.checked_add(10).debug()` in place of `level + 10`, then run again.
Or press Solve.

## 4.5 if let, while let and let else

### Step 1: if let (read)

A `match` with only one case worth handling can be written as an `if let`.
Line 3 tests one pattern, `.Some(n)`, against what `parse_i64` gives back for `typed`.
When it matches, the block on line 4 runs with `n` in scope, and otherwise the `else` block on lines 5 to 7 runs.
There's no `.None` arm to write, because an `if let` doesn't have to cover every case.
The `else` is optional, and without it nothing runs when the pattern doesn't match.
Press Run.

For `"12"` the pattern matches, and line 4 prints `12 doubled is 24`.
For `"twelve"`, `parse_i64` gives `None`, so line 6 prints `twelve isn't a number`.

### Step 2: while let (read)

`while let` repeats for as long as its pattern matches.
Line 3 pops from `stack` before each pass, and while `pop` gives a `Some`, `top` takes the element inside it.
Once the array is empty, `pop` gives `None` and the loop ends.
Press Run.

The loop prints `3`, `2` and `1`, from the last element to the first.
Line 6 then prints the array, `[]`, empty now.

### Step 3: let else (fix)

`let … else` is a `let` with a pattern: line 2 names the number inside `.Some(n)`, and when the pattern doesn't match, its `else` block runs.
Unlike `if let`'s `n`, which exists only inside its own block, this `n` stays in scope for the rest of the block, and line 5 uses it.
The whole `let … else` ends with the `;` on line 4.
Press Run.

The program doesn't run.
E0429 says "the `else` of a `let … else` must not finish", at line 2.
When the `else` block runs there's no `n`, so if the block ended normally, line 5 would run with no `n` to read.
The block has to leave instead, and the help lists ways to; here `return;` does it, ending `report` without a value.
Add `return;` as a new line after line 3 and run again, or press Solve.

> **Error note (E0429):** When `typed` isn't a number, the `else` block runs and there's no `n`, so the block must not go on to line 5. End it with `return;` so `report` stops there.

### Step 4: Nested patterns (read)

`describe` on line 7 takes an `Option<Shape>`, an `Option` that may hold a shape.
In `.Some(.Circle(r))` on line 9, the data inside the `Some` is matched with a pattern of its own, with its own dot.
That arm matches only a `Some` holding a circle, and names its radius `r`.
Lines 9 to 11 cover each shape inside a `Some`, and line 12 covers `.None`.
Line 18 pops the one circle from `shapes`, and line 19 pops again from the array, empty by then.
Press Run.

Line 18 prints `a circle of radius 1.5`, from the arm on line 9.
Line 19's `pop` gives `None`, so it prints `nothing`.

### Step 5: mut bindings (fix)

`count` on line 2 holds `Some(4)`, and the arm on line 4 names the number inside it `n`.
Line 5 adds 1 to `n`.
Press Run.

The program doesn't run.
E0501 says "cannot assign to `n`: it is not mutable", at line 5: names in a pattern can't change, like parameters.
The help suggests copying `n` into a `let mut`.
`mut` before the name in the pattern does that in one step, giving the arm its own copy to change, so `count` itself stays `Some(4)`, and line 10 prints it.
Change `.Some(n)` on line 4 to `.Some(mut n)` and run again, or press Solve.

> **Error note (E0501):** `n` is a name the pattern on line 4 gave the number inside `count`, and names in a pattern can't change, like parameters. `.Some(mut n)` gives the arm its own copy to change.

### Step 6: Names in patterns (fix)

`describe` matches on a `Shape`, and line 9's pattern is `Emtpy`, written without a dot.
Line 16 describes a circle.
Press Run.

A name without a dot in a pattern is always a new binding that matches any value, like `n` in `.Some(n)`, and that holds for a name on its own as an arm's whole pattern too.
`Emtpy` is misspelled, so it's no variant's name, and it catches every shape.
W0103 says "unused binding `Emtpy`", at line 9, and its help says a variant is written with a dot.
The two W0102 warnings mark the arms on lines 10 and 11 unreachable: line 9 comes first, so no shape gets past it.
So the circle prints `an empty shape`.
With its dot, a misspelling is an error instead: `.Emtpy` is E0415, "no variant `Emtpy` on `Shape`".
A bare name written on purpose, as in `other =>`, catches every value the arms above it didn't, and names it.
Write `.Empty` on line 9 and run again, or press Solve.

# 5. Value semantics

## 5.1 Copies

### Step 1: Copies (read)

Line 4 makes a `Point` named `a`, and line 5 assigns it to `b`.
Assigning a struct, an array or an enum gives the new variable a copy of its own, so `b` starts as a copy of `a`.
Line 6 changes `b.x` to `9`.
Press Run.

Line 7 prints `a`, and it still has `x: 1`: changing `b` didn't touch it, because they are two separate values.
Line 8 prints `b`, with `x: 9`.

### Step 2: Mutable copies (fix)

This time `a` on line 4 is declared `let mut`, and its copy `b` on line 5 is a plain `let`.
Line 6 changes `b.x`.
Press Run.

The program doesn't run.
`mut` belongs to a variable, not to its value, so `b` doesn't take its `mut` from `a`: it's a variable of its own and needs its own `mut`.
E0501 says so for line 6: `b` is not mutable, and its help suggests `let mut b`.
Add `mut` after `let` on line 5 and run again, or press Solve.

> **Error note (E0501):** `b` is a variable of its own, declared with a plain `let`, so line 6 can't change it. It doesn't take its `mut` from `a`, even though `b` started as a copy of `a`.

### Step 3: Copying arrays (read)

`xs` on line 2 is an array, and line 3 assigns it to `ys`.
Arrays follow the same rule as structs: `ys` starts as an array of its own, a copy of `xs`, not a second name for the same one.
Line 4 pushes `1` onto `ys`.
Press Run.

Line 5 prints `xs` as it was, `[5, 6]`, and line 6 prints `ys` with the `1` on its end.

### Step 4: Passing by value (fix)

`add_one` on line 1 takes an array, `xs`, and returns a new one with `1` pushed on.
A parameter written without `mut`, like `xs`, is a copy of what the caller passed, and the function can't change it.
So line 2 copies it into `ys`, line 3 pushes onto `ys`, and line 4 returns `ys`.
Line 9 calls `add_one`, and nothing keeps what it returns.
Press Run.

Line 10 prints `xs` as it was, `[5, 6]`: `add_one` changed only its own copy, and the array it returned was thrown away.
Through a plain parameter a function can't change its caller's values, so the caller keeps what it builds by assigning what it returns.
Make line 9 `xs = add_one(xs);` and run again, or press Solve.

### Step 5: Copies in a function call (read)

This is `add_one` again, and line 9 now keeps what it returns, as `zs`.
Line 10 prints `xs` and line 11 prints `zs`.
Press Run.

Line 10 prints `[5, 6]`, since `add_one` changed only its own copy, and line 11 prints `[5, 6, 1]`, the array it returned.

### Step 6: Copy-on-write (read)

Line 2 makes `big`, an array of a million zeros, and line 3 copies it into `copy`.
That copy takes the same time however long the array is, because at first `copy` shares `big`'s memory.
Line 4 writes to `copy`, and that's where `copy` gets a million numbers of its own.
This is called copy-on-write, and no program can tell it from a full copy.
Press Run.

Line 5 prints `big[0]`, still `0`, and line 6 prints `copy[0]`, now `1`.

## 5.2 mut parameters

### Step 1: mut parameters (read)

`bump` on line 3 has a `mut` parameter, `c`.
A parameter without `mut` is a copy of what the caller passed, but through a `mut` parameter the function changes the caller's own variable.
Line 4 adds `by` to `c.n`.
Lines 9 and 10 call `bump`, and each writes `mut c` for that parameter.
`main`'s `c` goes to `bump`'s `c` because it's the first argument, not because the names match.
Press Run.

Line 11 prints `5`: each call changed `c` in `main`, the first adding `2` and the second `3`.

### Step 2: mut at the call (fix)

Line 9 now calls `bump(c, 2)`, with no `mut` before `c`.
Press Run.

The program doesn't run.
A call changes what it passes to a `mut` parameter, so the call has to say so: the `mut` is written at the call as well as on the parameter.
E0443 says the parameter is `mut` and "the call changes the place you pass".
A place is somewhere a value is kept: a variable, or a field or element of one.
Its help says to write `mut x`, with `x` a `let mut` variable or a part of one.
It works the other way too: `mut` before an argument whose parameter has no `mut` is also E0443.
Write `mut c` on line 9 and run again, or press Solve.

> **Error note (E0443):** `bump`'s parameter `c` is `mut`, so the call changes the variable it's given, and the call has to say so by writing `mut c` rather than `c`.

### Step 3: Mutable places only (fix)

Line 9 passes `c` as `mut`, and line 8 declares `c` with a plain `let`.
Press Run.

The program doesn't run.
A `mut` argument is changed by the call, so it has to be a place that can change: a variable declared `let mut`, or a field or element of one.
E0501 says it cannot pass `c` as `mut` because `c` is not mutable, and its help suggests `let mut c`.
An element works the same way: `bump(mut counters[1], 5)` changes the second counter in a `let mut` array.
Add `mut` after `let` on line 8 and run again, or press Solve.

> **Error note (E0501):** `bump` changes the variable passed to its `mut` parameter, so that variable has to be declared `let mut`, and `c` on line 8 is a plain `let`.

### Step 4: No aliasing (fix)

`add_to` on line 3 adds `other`'s count to `total`, its `mut` parameter.
Line 9 passes `c` as both arguments, to double its count.
Press Run.

The program doesn't run.
A `mut` parameter works on the caller's variable itself.
Without `mut`, a parameter acts as a copy because the function can't change it, but a struct isn't actually copied: the function reads it where it is.
So with `c` as both, `add_to` would change `c` through `total` and see that change through `other`.
E0508 says `c` can't be passed as `mut` and also as another argument, and its help says to copy it first, so the call reads a value that doesn't change.
Put `let w = c;` on a line before line 9 and pass `w` as the second argument, then run again, or press Solve.

> **Error note (E0508):** `total` changes `c` itself, and `other` reads `c` where it is, so `add_to` would see its own change to `total` through `other`. Copy `c` first and pass the copy as `other`.

## 5.3 Ref

### Step 1: Ref boxes (read)

A `Ref` is a box: a place that holds one value, read with `get` and replaced with `set`.
`Ref.new(1)` on line 2 makes a box holding `1`, and `a` names it.
Line 3 copies `a` into `b`, line 4 calls `set(5)` on `b`, and line 5 prints `a.get()`.
Press Run.

It prints `5`, though line 4 called `set` on `b`.
Copying a `Ref` copies only a handle to the box, not the box itself, so `a` and `b` name the same box:

```diagram
file = "diagram.svg"
alt = "a and b both point at one box, which holds 5"
```

Every other value you have met so far gives you a copy of your own when you copy it.

### Step 2: set without mut (read)

`count` on line 2 is a box declared with a plain `let`, and line 3 calls `set(3)` on it.
An array's `push` needs `let mut`, but `set` doesn't: it changes what's in the box, and `count` still names the same box.
Press Run.

Line 4 prints `3`.
`let mut` is needed only to point a name at another box.

### Step 3: get returns a copy (read)

Line 4 puts a `Point` in a box, line 5 takes it out with `get` into `p`, and line 6 changes `p.x`.
Line 7 prints what's in the box.
Press Run.

It prints `Point { x: 1, y: 2 }`, with `x` still `1`.
`get` gives a copy of what's in the box, so changing `p` never reaches the box.
To change the box, put a value back with `set`.

### Step 4: Updating a box (fix)

Line 5 tries to add `1` to `count` and put the result back in the box with `set`.
Press Run.

The program doesn't run, because `count` is the box, not the number in it.
E0404 says `+` can't be applied to `Ref<i64>` and `i64`: `Ref<i64>` is a box holding an `i64`, and `+` needs the `i64` inside.
The help under it is about comparing boxes, which line 5 doesn't do.
`count.set(count.get() + 1)` would work, and `update` does it in one call.
It takes a function that gets an `i64` and returns one, calls it with what's in the box, and puts back what it returns.
`add_one` on line 1 is such a function, and `update` takes it by name: `add_one(0)` would call it, but `add_one` alone hands over the function.
Write `count.update(add_one)` on line 5 and run again, or press Solve.

> **Error note (E0404):** `+` works on numbers, and `count` is a box holding one, a `Ref<i64>`. Take the number out with `get`, or change it with `update`.

### Step 5: Identity with is (fix)

`b` on line 3 is a copy of `a`, so the two name one box, and `c` on line 4 is a second box that also holds `1`.
Lines 5 and 6 compare them with `==`.
Press Run.

The program doesn't run.
Boxes have no `==`, so E0404 says it "cannot apply `==` to `Ref<i64>`", once for line 5 and once for line 6.
The help under each gives the two ways to compare boxes: `a.is(b)` says whether both name the same box, and `a.get() == b.get()` compares what's inside.
To see which names share a box, change `a == b` to `a.is(b)` on line 5 and `a == c` to `a.is(c)` on line 6, then run again, or press Solve.

> **Error note (E0404):** Boxes have no `==`, so `a == b` is refused. Compare them with `is` to ask whether they're the same box, or compare what `get` gives to ask whether they hold the same value.

### Step 6: Linked structures (read)

`Node` on line 1 links to the next node through its `next` field, an `Option<Ref<Node>>`: `None` at the end, or a box holding the next node.
Line 4 makes `second`, a box holding a node, and line 5 makes `first`, with that box as its `next`.
Line 6 then puts a new node, with value `20`, in `second` with `set`.
Line 7 takes the box out of `first.next`, and line 8 prints the value of the node in it.
Press Run.

It prints `20`, because `first.next` holds the same box as `second`.
A plain `Option<Node>` would also compile, but `first` would then hold its own copy of the next node, and the change on line 6 wouldn't reach it.

## 5.4 Memory and safety

### Step 1: Memory safety (read)

`numbers` on line 1 makes an array on line 2 and returns it.
Line 7 keeps that array in `kept`, after `numbers` has finished.
Press Run.

It prints `[1, 2, 3]`.
The array is still there after `numbers` has finished, because its memory is freed only once nothing holds it.
While `kept` holds it, it stays, so `kept` never points at freed memory.
Lugha also has no null, and reading past the end of an array stops the program.

### Step 2: Variable initialization (fix)

`total` on line 2 has a type but no value, and the loop on lines 3 to 5 adds each number to it.
Press Run.

The program doesn't run.
A `let` always gives its variable a value, so no line can read one that was never set.
E0201 stops at line 2: it expected `=` and found `;`.
Add `= 0` after `i64` on line 2 and run again, or press Solve.

> **Error note (E0201):** A `let` has to give its variable a value with `=`, and line 2 ends after the type, so `lughac` found `;` where the `=` should be.

### Step 3: Reference counting (read)

An array can outlive the function that made it, as in step 1, so its memory isn't freed when that function ends.
Instead, Lugha counts what holds it.
Every variable, field or element that holds an array, a string or a box counts as one of its holders, and when the last one lets go, its memory is freed.
Line 4 makes a new array of 100 numbers on every pass of the loop, a hundred thousand in all, and only `row` holds it.
`row` is last used on line 5, at the end of the pass, so each array is freed there, before the next is made.
Press Run.

It prints `10000000`, the lengths of all the arrays added up.
The program never had to say which arrays it was done with: the compiler puts in the counting.

# 6. Errors

## 6.1 Result

### Step 1: Ok and Err (read)

A function whose work can fail can return a `Result`, so its caller can tell whether it worked.
`divide` on line 1 returns a `Result<i64, string>`: an `i64` answer, or a `string` saying why there isn't one.
Line 3 returns that string in an `Err` when the divisor is zero, and line 5 wraps the answer in `Ok`.
Like `Some`, `Ok` and `Err` can be written without the enum's name in front.
`Ok(a / b)` on line 5 doesn't say what the error type is, and it doesn't need to: the return type on line 1 says it's `string`.
Lines 9 and 10 print a division that works and one that fails, through `.debug()`, as an `Option` prints.
Press Run.

Line 9 prints `Ok(5)`, and line 10 prints the `Err` with its message.

### Step 2: Matching on Result (read)

This is `divide` again.
The loop on line 9 tries the divisors `2` and `0`, and line 10 matches on each `Result`.
`.Ok(q)` on line 11 names the answer `q`, and `.Err(e)` on line 12 names the message `e`, each with its dot as in any pattern.
The `match` has to cover both: without the `.Err` arm it's E0417, "`.Err` not covered".
Press Run.

The first pass takes the `.Ok` arm and prints `10 / 2 is 5`, and the second takes the `.Err` arm and prints the message.

### Step 3: Results can't be ignored (fix)

`check_age` on line 1 gives `Ok(())` for an age that makes sense, and an `Err` saying why otherwise.
`()` in `Ok(())` is the value that means nothing: there's no answer to give back, only whether it worked.
Line 9 calls it with `150` as a statement, and nothing looks at what it gives back.
Press Run.

The program doesn't run.
Other values can be thrown away with a `;`, but a `Result` used as a statement would lose its `Err` without anyone looking, so it doesn't compile.
E0467 says this `Result<(), string>` is discarded.
Its help names ways to handle it, `match` among them, and `?`, which comes in the next lesson.
It also says to drop it on purpose with `let _ = …;`, and `let _ = check_age(150);` would print only `checked`.
Handle it with an `if let` that prints the error: make line 9 `if let .Err(e) = check_age(150) {`, then `console.println(e);` and a closing `}` on the next lines, and run again, or press Solve.

### Step 4: map_err (read)

`map_err` changes the error inside an `Err`, and leaves an `Ok` as it is.
It takes a function from the old error to the new one, passed by name the way `update` takes one: here `explain` on line 8, which puts more words around the message.
Line 11 divides 10 by 0, line 12 prints the result as it is, and line 13 prints it again after `map_err(explain)`.
Press Run.

Line 12 prints the `Err` with the message from `divide`, and line 13 prints it with `explain`'s words around that message.

### Step 5: ok, unwrap_or, is_ok and is_err (read)

Line 9's division works, and line 10's fails.
`ok()` on lines 11 and 12 turns a `Result` into an `Option`, dropping the error.
`unwrap_or` on lines 13 and 14 gives the answer, or `0` when the division failed.
`is_ok()` and `is_err()` on lines 15 and 16 tell whether a division worked or failed.
Press Run.

Lines 11 and 12 print `Some(5)` and `None`, and lines 13 and 14 print `5` and `0`.
Lines 15 and 16 both print `true`, since `good` worked and `bad` failed.

## 6.2 The ? operator

### Step 1: ? on Result (read)

`?` after a `Result` gives the value inside an `Ok`, or returns the `Err` from the function at once.
`average` on line 8 divides with `divide(total, count)?` on line 9, so `avg` is a plain `i64`, not a `Result`.
Line 10 prints what it divided, and line 11 wraps the answer back in `Ok`.
Lines 15 and 16 call `average` with a count of `2`, then `0`.
Press Run.

For the count of `2`, line 10 prints `divided 10 by 2`, and line 15 prints `Ok(5)`.
For `0`, the failed division returns its `Err` from `average` at line 9, so line 10 doesn't run, and line 16 prints the `Err`.

### Step 2: ? on Option (read)

In a function that returns an `Option`, `?` works on an `Option` the same way: it gives the value inside a `Some`, or returns `None`.
`sum_two` parses two strings with `parse_i64` on lines 2 and 3, and either `?` returns `None` when its string isn't a number.
Line 4 adds the numbers only when both parsed.
Press Run.

Line 8 prints `Some(5)`, and line 9 prints `None`, since `"three"` isn't a number.

### Step 3: Error types (fix)

`?` returns a failure from the function it's in, so the failure has to fit that function's return type.
`doubled` on line 1 returns a `Result<i64, string>`, and line 2 uses `?` on the `Option` that `parse_i64` gives.
Press Run.

The program doesn't run, because a `None` has no error for `doubled` to return in an `Err`.
E0424 says "`?` can't return here", and its help suggests a `match`.
`ok_or("not a number")` is shorter: it turns the `Option` into a `Result`, with that string as its error, so `?` works.
A `Result`'s error type has to fit as well: in a function like `doubled`, `?` on a `Result<i64, i64>` is also E0424, and `map_err` can change the error first.
Add `.ok_or("not a number")` before the `?` on line 2 and run again, or press Solve.

> **Error note (E0424):** The `?` on line 2 is on an `Option`, and a `None` has no error for `doubled` to return in its `Result`. Turn the `Option` into a `Result` first.

### Step 4: Errors in main (fix)

`main` on line 6 returns an `i32` exit code, and line 7 uses `?` on what `doubled("x")` gives.
Press Run.

The program doesn't run.
`main` gives back nothing or an exit code, never a `Result`, so a `?` in it has no way to return an `Err`.
E0424's help says to handle it with `match`.
Replace lines 7 to 9 with a `match` on `doubled("x")`, with no `;` after it, so that it's `main`'s last expression and its value is the exit code.
An arm can be a block: `{` after the `=>`, its lines, then the value on a last line without `;`, then `}`; no comma is needed after it.
The `.Ok(n)` arm's block prints `n` and ends with `0`.
The `.Err(e)` arm's block prints `"error: {e}"` and ends with `1`, a failure's exit code.
Write it and run again, or press Solve.

> **Error note (E0424):** `main` returns an exit code, not a `Result`, so the `?` on line 7 can't return an `Err`. Use a `match` instead.

## 6.3 Panics

### Step 1: panic (read)

`panic` stops the program with a message, as integer overflow and an out-of-bounds index did.
`check_age` on line 1 panics on line 3 when it's given a negative age.
Line 9 passes it `30`, and line 10 passes it `-1`.
Press Run.

Line 9 prints `30`.
Then the panic prints its message and where it happened, `src/main.la:3:9`.
`(stderr)` marks that line as written to stderr, the program's error output.
A panic isn't a value like an `Err` that the caller can match on: it ends the program, so line 11 never prints `done`.
The program exits with code 101.

### Step 2: unwrap and expect (read)

`unwrap` takes the value out of a `Some` or an `Ok`, and panics when there isn't one.
`expect` does the same, but panics with a message you give it.
Line 2 unwraps `parse_i64("42")`, which is `Some(42)`, so `n` is `42`.
Line 4 calls `expect` on `parse_i64("forty")`, which is `None`.
Press Run.

Line 3 prints `42`.
Then `expect` panics with its message, and the place the panic names, `src/main.la:4:32`, is line 4, where `expect` was called, so the place to look is in your own code.
`unwrap` would have panicked there too, with `unwrap on None`, and on an `Err` its message includes the error, such as `unwrap on Err: "division by zero"`.

### Step 3: Stack overflow (fix)

`sum` on line 6 adds up a list by calling itself on the rest of it, on line 9.
Lines 14 to 17 build a list of a million `1`s.
Every call to `sum` waits for the next one to finish, and each waiting call takes room on the stack, which is finite: a million don't fit.
Press Run.

The program panics with `stack overflow`, the one panic that can't say where it happened, and exits with code 101.
Walk a long list with a loop instead.
Replace lines 7 to 10, the `match`, with `let mut total = 0;` and `let mut rest = list;`, then `while let .Cons(head, next) = rest {` with `total += head;` and `rest = next;` inside and a closing `}`.
Each pass adds the first value left in the list, and `rest = next` moves on to the rest, so `sum` no longer calls itself.
End `sum` with `total`, with no `;`, as its value, and run again, or press Solve.

## 6.4 defer

### Step 1: defer (read)

`defer` sets a statement aside to run when the block it's in is left.
Line 3 defers a `console.println` that reads `n`, and line 4 changes `n` after it.
Press Run.

Line 5 prints first, `end of main: n is 2`.
The deferred line runs when `main` ends, after line 5, and reads `n` as it is then, so it prints `2` too.

### Step 2: defer and early returns (read)

A defer runs on every way out of its block, a `return` or a `?` included.
`average` prints `starting` on line 9 and defers a line printing `finished` on line 10, before line 11 divides with `?`.
Lines 16 and 17 call it with a count of `2`, then `0`.
Press Run.

For the count of `2`, `average` prints `starting`, then `finished` as it ends, and line 16 prints `Ok(5)`.
For `0`, the `?` on line 11 returns the `Err` at once, but line 10's `defer` was already reached, so `finished` still prints before line 17 prints the `Err`.
So cleanup written as a `defer` near the top of a function also runs when a later `?` returns early.

### Step 3: Defer order (read)

When a block has several defers, they run last first.
Lines 2 and 3 defer two lines in `main`.
Line 5's defer is inside the loop's body, so it belongs to the body, not to `main`, and runs at the end of each pass.
Press Run.

Each pass prints `pass {i}` from line 6, then `end of pass {i}` from its defer as the pass ends.
Then line 8 prints `end of main`, and as `main` ends its defers run last first: line 3's `second defer`, then line 2's `first defer`.

### Step 4: defer and panics (read)

A panic leaves blocks too, on its way to ending the program.
Line 2 defers a line printing `cleaning up`, and line 4 reads `ages[2]`, past the end of `ages`, which has two elements.
Press Run.

`cleaning up` prints first: as the panic leaves `main`, it runs `main`'s pending defer.
Then the panic gives the length and the index, and where it happened, and the program exits with code 101.

### Step 5: Deferred values (fix)

`close` on line 1 is cleanup that can fail, so it gives back a `Result`, and line 7 defers it.
Press Run.

The program doesn't run.
A deferred statement's value would go nowhere, so it must have type `()`, and `close` gives a `Result<(), string>`.
E0456 says so, and its help says to handle the error inside it or discard it on purpose, with an example of a block holding a `let _ =`.
A block with only `close(console, "notes");` in it wouldn't do: that's a `Result` used as a statement, E0467.
Make line 7 `defer { let _ = close(console, "notes"); }`, which drops the `Result` on purpose, and run again, or press Solve.

# 7. Closures and collections

## 7.1 Functions as values

### Step 1: Function types (read)

A function is a value too.
Its type is its signature without the names: `double` on line 1 is a `fun(i64): i64`, a function that takes an `i64` and gives back an `i64`.
Line 6 stores `double` in `f` without calling it, since there are no parentheses after it.
`apply` on line 3 takes a function, `f`, as its first parameter and calls it on `x`.
Press Run.

`10` comes from line 7, which calls `double` through `f`.
`42` comes from line 8, which passes `double` to `apply` by name, and `apply` calls it on `21`.
`<fun>` comes from line 9, which prints `f` itself through `.debug()`: that's a function's debug form.
Without `.debug()`, `console.println(f)` is E0422, as for an array.
Function values have no `==` either: `f == double` is E0404.

### Step 2: Arrays of functions (read)

Functions can sit in an array like any other value.
`steps` on line 6 holds three of them.
Its type, `(fun(i64): i64)[]`, needs the parentheses, because `fun(i64): i64[]` is a function that returns an array.
The loop on line 8 goes over them in order, and line 9 calls each one as `step(n)` and keeps the result in `n`.
Press Run.

`n` starts at `3`: `double` makes it `6`, `square` makes it `36`, and `negate` makes it `-36`, which line 11 prints.

### Step 3: Variants as functions (read)

A variant that carries data is a function value too: `Shape.Circle` takes an `f64` and gives back a `Shape`, so it's a `fun(f64): Shape`.
`apply_all` on line 6 takes such a function as `make`, and line 9 calls it on each size.
Lines 15 and 16 pass `Shape.Circle` and `Shape.Square` to it without calling them.
`Some`, `Ok` and `Err` are function values the same way, once a written function type says what they hold, as `wrap`'s type does on line 17.
Press Run.

Line 15 prints the two circles `apply_all` made, line 16 the one square, and line 18 `Some(2.0)`, from calling `Some` through `wrap`.
A struct's associated function, such as `Point.new`, is a value the same way.

## 7.2 Closures

### Step 1: Closures (fix)

A closure is a function written in place, without a name.
Line 4 passes the closure `fun(x) = x * 2`, which doubles its argument, to `apply`.
Line 5 stores a second closure, `fun(x) = x + 10`, in the variable `add_ten`.
Press Run.

The program doesn't run.
On line 4, `x` takes its type from `apply`'s parameter, a `fun(i64): i64`, but on line 5 nothing says what `x` is.
E0412 says so: it "can't infer the type of parameter `x`".
Its help gives both ways out: write the type, `x: i64`, or pass the closure where a function type is expected, as line 4 does.
The return type can be written too, as in a named function.
A longer body goes in braces, as in `fun(n: i64): string { … }`, and a closure that uses `return` needs its return type written, unless it's passed where a function type is expected.
Make line 5's closure `fun(x: i64): i64 = x + 10` and run again, or press Solve.

> **Error note (E0412):** A closure's parameter needs a type, either written or taken from where the closure is passed. Line 5 stores the closure in a variable, so nothing says what `x` is.

### Step 2: Capture by copy (read)

A closure can use the variables around it.
`scale` on line 3 uses `rate`, which is `2` at that point, and line 4 changes `rate` to `7` afterwards.
Line 5 calls `scale(5)`, and line 6 prints `rate`.
Press Run.

Line 5 prints `10`, not `35`: `scale` copied `rate` when line 3 made it, so line 4's change doesn't reach it.
Line 6 prints `7`, so `rate` itself did change.

### Step 3: Counters with Ref (fix)

`count` on line 2 is a `let mut` variable.
The closure `tick` on line 3 takes no parameters, and its body, in braces, adds `1` to `count`.
Lines 4 and 5 call `tick` twice, and line 6 prints `count`.
Press Run.

The program doesn't run.
`tick` copied `count` when line 3 made it, so `count += 1` could only change that copy, never the `count` that line 6 prints.
E0511 says so on line 3: "can't change `count`: closures capture by copy".
Its help says to return a new value instead, which works when only the closure needs the result.
Here `main` must see the count too, so put it in a `Ref`: the closure copies the handle, and the closure and `main` reach the same box.
Make line 2 `let count = Ref.new(0);`, line 3's body `count.set(count.get() + 1);`, and line 6 print `count.get()`, then run again, or press Solve.

### Step 4: Ref.update (read)

`update` takes a function, and a closure can be written right there instead of a named one like `add_one`, which `update` took by name in the Ref lesson.
Line 3 passes `update` the closure `fun(n) = n * 3`, and `n` takes its type from `update`'s parameter, a `fun(i64): i64`, as `x` did from `apply`'s.
Press Run.

`update` called the closure on the `10` in the box and put back the `30` it returned, which line 4 prints.

### Step 5: map and and_then (read)

`map` on an `Option` calls its closure on what a `Some` holds and gives back a new `Some` with the result, and leaves a `None` as it is.
On a `Result`, `map` works the same way on an `Ok` and leaves an `Err` as it is, the other way round from `map_err`.
`and_then` takes a closure that returns an `Option` or a `Result` itself, so the closure decides whether the answer is a success or a failure.
Line 9 writes its closure's return type, `Result<i64, string>`: a closure that gives back `Ok` or `Err` to a `Result`'s `and_then` needs it written, or `lughac` stops with E0412.
Press Run.

Line 2 prints `Some(42)`: `parse_i64("21")` gives `Some(21)`, and `map` doubles it.
Line 3 prints `None`, since `"x"` isn't a number.
Lines 6 and 7 print `Ok(5)` and `Err("no")`: only the `Ok` changed.
Line 8 prints `None`, because the closure returns `None` for `-3`.
Line 9 prints `Err("too small")`, because `good` holds `4`, which isn't more than `9`.

### Step 6: Closures and recursion (fix)

Line 2 stores a closure in `fact`.
For `n` above `1`, the closure multiplies `n` by `fact(n - 1)`, calling `fact` again.
Press Run.

The program doesn't run.
A closure has no name of its own, so it can't call itself.
`fact` is only the variable that will hold the closure, so the `fact(n - 1)` inside it refers to nothing yet.
E0301 says so: "cannot find `fact` in this scope", pointing at that call on line 2.
A named function can call itself, so write `fact` as one.
Move line 2 above `main` as `fun fact(n: i64): i64 = if n <= 1 { 1 } else { n * fact(n - 1) };`, or press Solve.

## 7.3 Array helpers

### Step 1: map (read)

Arrays have a `map` too, and it takes a closure, as `Option`'s does.
It calls the closure on each element and gives back a new array of the results.
Line 3 doubles each price, and line 4 turns each one into a string, so `labels` is a `string[]`.
Line 7 prints `prices` after both.
Press Run.

Lines 5 and 6 print the two new arrays.
Neither `map` changed `prices`: line 7 prints it as it was.

### Step 2: filter (read)

`filter` also takes a closure, one that returns a `bool`, and keeps the elements for which it's `true`, in order, in a new array.
Line 3 keeps the even numbers.
`filter` and `map` both give back arrays, so one can follow the other: line 5 keeps the evens, then squares them.
Press Run.

Line 4 prints the evens, `[2, 4, 6]`, and line 5 their squares.

### Step 3: fold (read)

To turn a whole array into one value, use `fold`.
It starts from the value you give it, calls its closure with the result so far and each element in turn, left to right, and gives back the last result.
Line 3 starts from `0` and adds each number.
Line 4 starts from the first number and keeps the larger of the two each time.
Press Run.

Line 5 prints the sum, `22`, and line 6 the largest number, `9`.

### Step 4: any and all (read)

`any` and `all` take the same kind of closure as `filter`, but give back one `bool`.
`any` on line 3 asks whether some age is under 18.
`all` on line 4 asks whether every age is under 18, and on line 5 whether every age is above `0`.
Press Run.

Line 3 prints `true`, because `17` is under 18.
Line 4 prints `false`, because `34` and `52` aren't.
Line 5 prints `true`, since every age is above `0`.

### Step 5: Sorting (fix)

`sort` gives back a new array in ascending order.
Lines 4 and 5 sort numbers and strings, and line 7 sorts `Person`s.
Press Run.

The program doesn't run.
`sort` needs a type that is `Ord`, one with an order of its own, and `Person` has none.
E0422 says so on line 7: "`Person` doesn't implement `Ord`".
Of the two ways its help offers, the one for now is `with Ord` after the declaration: as `with Eq` gives `==`, it gives an order, by the fields in the order they're declared, here by `name` first.
To sort by age, `sort_by` takes the rule as a closure instead, one that says whether `a` comes before `b`.
It keeps people of the same age in their order.
Floats have `<` but no order of their own: `[1.5, -2.0, 0.5].sort()` is E0451, and its help says "sort them with `xs.sort_by(f64.total_order)`", which gives `[-2.0, 0.5, 1.5]`.
Change `people.sort()` on line 7 to `people.sort_by(fun(a, b) = a.age < b.age)` and run again, or press Solve.

> **Error note (E0422):** `sort` needs to know how two values compare, which a type says by being `Ord`. `Person` isn't, so add `with Ord` after its declaration, or sort with `sort_by` and a rule of your own.

## 7.4 Maps and sets

### Step 1: Map literals (read)

A map holds values under keys, written `Map { key: value }`, and keeps its keys in the order they were added.
`ages` on line 2 is a `Map<string, i64>`.
`ages["ann"]` on line 3 reads a value, and line 4 adds a key by assigning to it.
Line 5 changes a value where it is, with `+=`.
An empty `Map {}` takes its type from where it's used, as `[]` does: on line 7, from the type written after `none_yet`.
A map prints through `.debug()`, as an array does.
Press Run.

Line 3 prints `31`.
Line 6 prints the map after lines 4 and 5: `"cy"` is added at the end, and `"bo"` is now `41`.
Line 8 prints the empty map.

### Step 2: Missing keys (read)

`get` on line 3 gives an `Option`: `Some` with the value, or `None` when the key isn't there, as on line 4.
`has` on line 5 only asks whether the key is there.
Line 6 reads a missing key with `[…]`.
Press Run.

Lines 3 to 5 print `Some(31)`, `None` and `false`.
Then line 6 panics: the program stops with `no key "dee" in the map` and the line it happened on, and exits with code 101.
When a key may be missing, use `get` or `has`.

### Step 3: Iterating a map (fix)

A map can be looped over like an array: each entry is a tuple of key and value, in the order the keys were added.
Line 3 loops with `of mut`, and line 4 means to double each price where it is.
Lines 6 to 8 print each entry, and line 9 prints `values()`, the map's values in the same order.
Press Run.

The program doesn't run.
A map isn't changed through its loop: the loop visits a copy of its entries.
E0442 says so on line 3: "`for … of mut` can't change a `Map<string, i64>` in place".
Its help says what to do: loop over the keys, with `keys()`, and assign through each one.
The E0501 on line 4, "cannot assign to `price`", follows from the first error: its help about match bindings can be ignored, since the error goes once line 3 is fixed.
Make line 3 `for item of prices.keys() {` and line 4 `prices[item] *= 2;`, then run again, or press Solve.

### Step 4: Sets (read)

A set holds distinct values, written `Set { a, b }`, without colons, and keeps them in the order they were added.
`has` on line 3 asks whether a value is in it, and `insert` on lines 4 and 5 returns `true` only when the value is new.
`remove` on line 6 returns `true` when there was something to remove.
Maps have `remove` too, giving back the removed value as an `Option` on line 9, and both have `clear`, which empties them, as line 10 does for `ages`.
Press Run.

Line 3 prints `true` for `"red"`.
Line 4 prints `true`, since `"green"` is new, and line 5 `false`, since `"red"` was already there.
Line 6 prints `true` for removing `"blue"`, and line 7 shows what's left, in the order it was added.
Line 9 prints `Some(40)`, the value `"bo"` had, and line 11 the emptied map.

### Step 5: Set operations (read)

`union` on line 4 gives the values in either set.
`intersect` on line 5 keeps the ones in both, and `minus` on line 6 keeps the ones in `a` that aren't in `b`.
Line 7 compares two sets written in different orders, and line 8 two maps.
Press Run.

Lines 4 to 6 print the three new sets.
Lines 7 and 8 both print `true`: `==` compares what the two hold and ignores the order.

### Step 6: Key types (fix)

Keys can be integers, strings, `bool`s and `char`s.
A map or set finds each key by its hash, a number worked out from the key, and by `==`.
`grid` on line 4 is a map with `Point`s as keys, for the cells of a grid, and lines 5 to 7 use `Point`s to set and read cells.
Press Run.

The program doesn't run.
A key's type must be `Key`, which gives it the hash and the `==`, and `Point` isn't.
E0422 says so at each line that uses a `Point` as a key, lines 4 to 7: "`Point` doesn't implement `Key`".
Each help offers `with Key` after `Point`'s declaration, which gives it what a key needs, as `with Eq` gives a struct `==`.
A float is never a key: `Map { 0.25: "small" }` is E0451, whose help gives the reason, "`NaN != NaN`, so a float key could never be found again".
Add `with Key` after the `}` on line 1 and run again, or press Solve.

> **Error note (E0422):** A map's keys must be `Key`, so the map can find each one again by its hash and `==`. `Point` isn't, and `with Key` after its declaration makes it one.

# 8. Interfaces and generics

## 8.1 Interfaces

### Step 1: Interface declaration (read)

An interface names a set of methods that different types can share.
`Shape` on lines 1 to 4 lists two, with their signatures and no bodies.
`Circle` implements it with `impl Shape for Circle` on lines 8 to 11, which gives each method its body.
Line 15 calls them with a dot, as for any method.
An interface's methods can use `Self` for the type that implements it, as in `fun bigger(self, other: Self): bool`.
Press Run.

Line 15 prints the circle's name and area, from the two methods `Circle`'s `impl` wrote.

### Step 2: Implementing an interface (fix)

`describe` on line 13 takes any `Shape`: its parameter's type is the interface, so it takes a value of any type that implements it.
Line 16 passes it a `Circle`.
This time `Circle`'s methods on lines 8 to 11 are in a plain `impl Circle`, with the same names and signatures as `Shape`'s.
Press Run.

The program doesn't run.
Having methods with the right names isn't enough: a type implements an interface only through an `impl Shape for …` block.
E0422 says so on line 16, where the `Circle` is passed: "`Circle` doesn't implement `Shape`".
Its help names the block to add.
An `impl Shape for Circle` that leaves a method out is E0422 too, at the block, and its help names the missing method.
Change `impl Circle` on line 8 to `impl Shape for Circle` and run again, or press Solve.

> **Error note (E0422):** `describe` takes a `Shape`, and `Circle` isn't one until an `impl Shape for Circle` block says so. Methods with the same names in a plain `impl Circle` don't count.

### Step 3: Where an impl lives (fix)

An `impl` is written in the module that declares the interface or the one that declares the type; a module is one part of a program, and every program so far has been a single module.
`Display` is the interface `console.println` prints through, and its method is `show`.
Lines 1 to 3 implement it for `bool`, to print `true` as `yes`.
Press Run.

The program doesn't run.
`Display` and `bool` both come with the language, so no `impl` in this program can implement one for the other.
E0459 says so at line 1: "this `impl Display for …` must be written in the module that declares `Display`".
For a type you declare yourself, `impl Display` is allowed.
Use an interface of your own instead.
Change line 6 to print `true.label()`, `show` on line 2 to `label`, and line 1 to `impl Label for bool {`.
Then, above line 1, declare an interface `Label` with one method, `fun label(self): string;`, and run again, or press Solve.

> **Error note (E0459):** An `impl` must be written in the module that declares the interface or the one that declares the type. `Display` and `bool` both come with the language, so this program can't implement one for the other.

### Step 4: Default methods (read)

An interface can give a method a body, which is then its default.
`describe` on line 3 has one, and it calls `area` on `self`.
`Circle`'s `impl` on lines 9 to 11 has no `describe`, so line 19 uses the default.
`Square`'s `impl` writes its own on line 15, which line 20 calls.
Press Run.

The first line comes from the default, with the circle's area, and the second from `Square`'s own `describe`.

### Step 5: Interfaces extending interfaces (fix)

`Pet` on line 5 extends `Named`: `interface Pet: Named` means every `Pet` is a `Named` too.
Line 11 implements `Pet` for `Dog`, and line 17 calls both `name` and `sound`.
Press Run.

The program doesn't run.
Implementing `Pet` doesn't implement `Named` for you, so `Dog` has `sound` but no `name`.
E0415 says so first, at the call on line 17: "no method `name` on `Dog`".
E0422 gives the cause, on line 11: "`Dog` implements `Pet` but not `Named`, which `Pet` extends".
Each interface gets its own block: `name` written inside `impl Pet for Dog` is E0422, "`name` isn't an item of `Pet`".
The help's first way, `with Named`, is E0462 here: `with` asks for an interface built from derive blocks, as `Eq` is, and `Named` has none.
The second way, an `impl Named for Dog` block, is the fix.
Above line 11, add an `impl Named for Dog` block with `fun name(self): string = "dog";` in it, and run again, or press Solve.

> **Error note (E0415):** `Dog` has no `name` method: `impl Pet for Dog` gives it `sound`, but `name` belongs to `Named`, and nothing implements `Named` for `Dog` yet.

## 8.2 Interface values

### Step 1: Interface values (fix)

An interface is also a type, and a `Shape` value can hold a value of any type that implements `Shape`.
Line 17 puts a circle and a square in one array, and line 18 prints it.
Press Run.

The program doesn't run.
An array takes its type from its first element, so this one is a `Circle[]`, and a `Square` can't go in it.
E0403 says so at the square on line 17: "expected Circle, found Square".
A value becomes a `Shape` only where a `Shape` is expected, so write the array's type.
Line 18 will then print each `Shape` through its debug form, which is the value inside it.
Add `: Shape[]` after `shapes` on line 17 and run again, or press Solve.

> **Error note (E0403):** An array takes its type from its first element, so line 17's array is a `Circle[]`, and a `Square` doesn't fit. Written as a `Shape[]`, it turns each element into a `Shape`.

### Step 2: Method calls on interface values (read)

`s.area()` on a `Shape` runs the `area` of the type inside it.
The loop on lines 19 to 21 adds up `s.area()` for a circle and a square, each with its own `area`.
A `Shape` has only its methods, though: `shapes[0].r` would be E0410, "no field `r` on `Shape`", and its help says to use a type pattern to reach the value inside.
Press Run.

`7.0` is the circle's area, `3.0`, plus the square's, `4.0`.

### Step 3: Type patterns (fix)

To reach the value inside a `Shape`, `match` on the type it holds.
`c: Circle` on line 18 matches when `s` holds a `Circle`, and names it `c`, a `Circle` with its fields.
`_: Square` on line 19 matches a square without naming it, since its arm doesn't need it.
Press Run.

The program doesn't run.
Any type that implements `Shape` could be inside, even one written later, so the `match` needs a `_` arm even with an arm for each type here.
E0417 says so at the `match` on line 17: "non-exhaustive match: `_` not covered".
Add `_ => "something else",` as a new line after line 19 and run again, or press Solve.

### Step 4: Interface conversion (fix)

An interface value converts only to an interface its own extends: with the last lesson's `Pet: Named`, a `Pet` converts to a `Named`, but converting it to another interface `Dog` implements is E0422.
`total` on line 16 takes a `Shape[]`, and line 20 passes `circles`, a `Circle[]`.
Press Run.

The program doesn't run.
A value becomes a `Shape` one at a time, never as an array or an `Option` around it.
E0403 says so at the call on line 20: "expected Shape[], found Circle[]".
An array's type is fixed where it's built, so make `circles` a `Shape[]` there.
Add `: Shape[]` after `circles` on line 19 and run again, or press Solve.

> **Error note (E0403):** `total` needs a `Shape[]`, and `circles` is a `Circle[]`. Each `Circle` can become a `Shape`, but an array of them can't, so give the array its type where it's built.

### Step 5: Own methods and interface items (read)

A type can have a method of its own and an interface's item with the same name.
`Circle` has its own `area` on line 8, in a plain `impl Circle`, and `Shape`'s `area` on line 12, in `impl Shape for Circle`.
Line 17 calls `c.area()`, and line 18 calls `Shape.area(c)`, naming the interface.
Press Run.

Line 17 prints `1.0`: `c.area()` runs the type's own method, `self.r * self.r`.
Line 18 prints `3.0`: `Shape.area(c)` runs the interface's item.
A `Shape` value holding `c`, such as `s` after `let s: Shape = c;`, runs the interface's item too: `s.area()` gives `3.0`.

## 8.3 Generic functions

### Step 1: Generic functions (read)

Some functions do the same thing whatever type they're given.
Taking the first element works the same for an `i64[]` as for a `string[]`, so writing it twice would repeat the same body.
A generic function is written once, with a type parameter standing for the type: `T` in `first<T>` on line 1.
`T` is used wherever that type goes, so `first` takes a `T[]` and gives back an `Option<T>`.
Each call fills `T` in from its argument: line 11 uses `first` with `i64` and line 12 with `string`, and neither is written.
`empty` on line 8 takes no arguments, so line 13's `: string[]` fills `T` in, and without it the call is E0412.
Press Run.

Line 11 prints `Some(3)`, line 12 `Some("tea")`, and line 14 the empty `string[]` that `empty` gave back.

### Step 2: Type arguments at a use (fix)

Line 9 calls `first` with an empty array, which has no element to fill `T` in from.
Press Run.

The program doesn't run.
E0412 says so at the `[]` on line 9: "cannot infer the element type of `[]`".
Its help writes the type on a variable, as line 13 did in the last step, but here the array goes straight into `first`, so the type goes on the call instead.
A type argument can be written where the function is used, in angle brackets after its name: `first<string>([])` makes `T` a `string`.
Methods take them the same way: for an `i64[]` called `xs`, `xs.map<string>(fun(p) = "{p} coins")` says `map` gives a `string[]`.
Make line 9's call `first<string>([])` and run again, or press Solve.

### Step 3: Type bounds (fix)

`first` only passed its `T` along, which any type allows.
`count_of` counts how often `wanted` is in `xs`, and compares two `T`s with `==` on line 4.
Press Run.

The program doesn't run.
Not every type has `==`, so a `T` has none until the function says it needs one.
E0404 says so on line 4, "cannot apply `==` to T", and its help gives the fix: declare `T: Eq`.
That's a bound, an interface `T` must implement: `Eq` for `==`, `Ord` for `<` and `sort`, `Key` for map keys, or one of your own, like `T: Shape`.
Several bounds join with `+`, as in `T: Ord + Key`.
Calling a bounded function with a struct or enum of your own that misses one is E0422 at the call: `count_of` on a `Point` without `with Eq` says "`Point` doesn't implement `Eq`".
Add `: Eq` after `T` on line 1 and run again, or press Solve.

### Step 4: Numeric bounds (fix)

Arithmetic on a `T` needs a bound too: `T: Num` allows it, along with `==`, `<`, and an integer literal where a `T` goes.
So `total` starts its sum from `0` on line 2 and adds up `i64`s and `f64`s alike.
`half` on line 9 multiplies by `0.5`, a float literal, but a `Num` can be an integer type too.
Press Run.

The program doesn't run.
A `T` that is `Num` may be an integer type, and `0.5` can't be one.
E0401 says so at the `0.5` on line 9: "float literal where T expected".
`T: Float` is met only by `f32` and `f64`, and allows everything `Num` does as well as float literals.
Change `Num` to `Float` on line 9 and run again, or press Solve.

> **Error note (E0401):** `T: Num` lets `T` be an integer type, and `0.5` can't be an integer, so a float literal can't stand for a `T` here. `T: Float` allows it.

### Step 5: Function bounds (read)

A function type can be a bound too: `F: fun(i64): i64` on line 3 takes any function of that signature.
`twice` calls `f` two times, and line 6 passes it the named function `double`, line 7 a closure.
A bound doesn't give a closure its parameter types, the way a parameter of a function type does, so line 7 writes `n: i64`: `fun(n) = n + 1` there is E0412.
Press Run.

Line 6 prints `20`, `5` doubled twice, and line 7 prints `7`, `5` plus one twice.

## 8.4 Generic types

### Step 1: Generic structs (fix)

A struct can take a type parameter as a function does: `Pair<T>` on line 1 holds two values of one type, `T`.
Line 6 builds a pair of numbers and line 7 a pair of strings, and `T` comes from the fields, as it came from a function's arguments.
In a type, though, a generic struct is written with its argument, as in `Pair<i64>`.
Line 3 writes a bare `Pair` as a type twice, for `p` and for what `swap_pair` gives back.
Press Run.

The program doesn't run.
E0418 says so at both of line 3's `Pair`s: "`Pair` takes 1 type argument but 0 were given".
`swap_pair` is called with both pairs, so it has to be generic itself.
The `Pair { … }` after `=` stays as it is: it takes `T` from its fields, as line 6 does.
On line 3, add `<T>` after `swap_pair` and write `Pair<T>` for the parameter's type and the return type, then run again, or press Solve.

### Step 2: Generic enums (read)

Enums take type parameters in the same place.
`List<T>` on lines 1 to 4 is a recursive enum, a list that can hold any type: a `Cons` holds one element and the rest of the list, and `Nil` ends it.
Line 14 builds a list of strings, and `size` on line 6, generic itself as `swap_pair` was, counts it.
`Option<T>` is declared this way too.
Press Run.

Line 15 prints the list through its debug form, and line 16 its size, `2`.

### Step 3: Generic impl blocks (read)

Methods for a generic type go in an `impl` block that names its parameter after `impl`, as `impl<T> Stack<T>` on line 3 does.
There `T` stands for the element type, and `Self` for `Stack<T>`.
Line 23's `Stack<i64>` fills in `T` for `Stack.new()`, as `: string[]` did for `empty`.
A second block, `impl<T: Num> Stack<T>` on line 18, adds a bound, so `total` exists only for stacks of numbers.
Press Run.

Line 26 prints `Some(4)`, the last item pushed.
Line 27 prints `7`: `total`'s `0` is a `T`, as `Num` allows, and the fold adds `3` and `4` to it.
Line 30 prints `Some("tea")`.
Calling `total` on `words` would be E0419, "`string` doesn't satisfy `Num`", the code for a built-in type that misses a bound.

## 8.5 Equality, ordering and printing

### Step 1: Deep equality (read)

`==` reaches into a value's parts, so line 4 compares two `Point`s field by field, which `with Eq` on line 1 allows.
Arrays compare element by element, as on lines 5 and 6, and `Some(a)` equals `Some(b)` when `a` equals `b`.
Line 7 divides zero by zero, which gives a float that isn't a number, `NaN`, and line 8 compares it with itself.
A `Ref` box, a function and an interface value have no `==`, and nor does an array or an `Option` that holds one.
Press Run.

Lines 4 to 6 print `true`: the parts match on lines 4 and 5, and `[3]` and `[4]` differ on line 6, which uses `!=`.
Line 8 prints `false`: `NaN` is equal to nothing, itself included.
`==` works on a value only when each of its parts has `Eq`: comparing two arrays of `Point`s, with no `with Eq` on `Point`, is E0422, naming `Point`.

### Step 2: with Eq, with Ord and with Key (read)

`with` after a declaration asks for an interface built from the fields.
`with Eq` compares them, `with Ord` orders by the fields, in the order they're declared, and `with Key` hashes them so the type can be a map key or a set value.
`Ord` and `Key` both extend `Eq`, so `Version` on line 1 has `==` too, and so does `Tag` on line 2.
Line 6 prints a sorted copy and leaves `versions` as it was.
Line 7 compares two versions with `<`, line 8 checks one for equality, and line 9 puts two equal tags in a set.
Press Run.

Line 6 prints the sorted copy.
`major` is declared first, so it decides first: 1.9 and 1.10 sort before 2.0.
Between those two, `minor` decides, and 9 comes before 10.
Lines 7 and 8 print `true`, and line 10 prints `1`: the set on line 9 keeps one of the two equal tags.

### Step 3: impl Eq and impl Key (fix)

A type can decide what equal means for itself by writing `Eq` by hand.
`impl Eq for User` on lines 3 to 5 counts two users as equal when their `id`s are, whatever their names.
Line 10 compares two of them, and line 11 puts both in a set.
Press Run.

The program doesn't run.
A set value must be `Key`, and `User` is only `Eq`.
E0422 says so at the set on line 11: "`User` doesn't implement `Key`".
Its help offers `with Key`, but that would hash every field, `name` too, so two users equal by `id` would hash differently, and equal values must hash the same.
So `Key` is written by hand as well.
Its one method, `hash`, gets `h`, a `Hasher` that works out the hash.
`hash` adds to `h` the same fields `eq` compares: here `h.add(self.id);`.
After line 5, add an `impl Key for User` block with `fun hash(self, mut h: Hasher) { h.add(self.id); }` in it, and run again, or press Solve.

### Step 4: impl Ord (fix)

`Ord` written by hand is one method, `cmp`, which gives back `Ordering.Less`, `Ordering.Equal` or `Ordering.Greater`.
`cmp` on line 4 orders versions by `major` alone, so 1.9 and 1.10 count as one release line, and `sort` on line 17 uses it, as do `<`, `<=`, `>` and `>=`.
`Version` gets `==` from `with Eq` on line 1, and lines 20 and 21 compare 1.9 and 1.10 both ways.
Press Run.

The program runs, after a warning on line 1, W0108: "`Version`'s `==` and `<` can disagree".
Its help says to write `impl Eq for Version` so that `==` compares what `cmp` compares.
Line 17 prints the sorted array.
Line 20 prints `false`, since the derived `==` compares `minor` too.
Line 21 prints `false`, since `cmp` finds neither less: `==` says the two differ, while `cmp` finds them equal.
Remove `with Eq` from line 1, and after line 1 add an `impl Eq for Version` block with `fun eq(self, other: Version): bool = self.major == other.major;`, then run again, or press Solve.

### Step 5: impl Display (read)

`console.println` and `"{x}"` print a value through `Display`, one method, `fun show(self): string`.
`impl Display for Version` on lines 3 to 5 shows a version as `v1.10`.
Line 9 prints one, and line 10 puts one in a string.
Line 11 prints an array of versions through `.debug()`.
Press Run.

Line 9 prints `v1.10` through `show`, and line 10 puts the same text in the string.
A debug form never uses `Display`: the array on line 11 shows each `Version` with its fields.

### Step 6: impl Debug (read)

A debug form can be written by hand too, with `impl Debug for Version` and its one method, `debug`, on lines 3 to 5.
Line 9 prints a version's debug form, line 10 an array's, and line 11 an `Option`'s.
Press Run.

The hand-written form is used wherever a `Version`'s debug form is, inside the array and the `Option` too.

## 8.6 Operator overloading

### Step 1: Arithmetic operators (fix)

An operator on a type of your own goes through an interface: `+` through `Add`, whose one method is `add`.
`-`, `*`, `/` and `%` go through `Sub`, `Mul`, `Div` and `Rem` the same way, and a leading `-` through `Neg`.
`Vec2` has an `add` of its own, in a plain `impl Vec2` on lines 3 to 5, and line 10 adds two `Vec2`s.
Press Run.

The program doesn't run.
As for any interface, a method with the right name isn't enough: `+` needs an `impl Add` block.
E0404 says so on line 10, "cannot apply `+` to Vec2", and on line 11, "cannot apply `+=` to Vec2".
Both helps name the block to write, `impl Add<…> for Vec2`; `Add` alone means a `Vec2` on both sides, which is what's needed here.
With it, `b += a` on line 11 works too, as `b = b + a`.
Change `impl Vec2` on line 3 to `impl Add for Vec2` and run again, or press Solve.

> **Error note (E0404):** `+` on a type of your own needs an `impl Add` block. `Vec2` has an `add` method, but in a plain `impl Vec2`, which doesn't count.

### Step 2: Mixed operands (read)

`Add` alone means `Add<Vec2>`, with a `Vec2` on both sides; `Mul<f64>` says the right-hand operand is an `f64`.
A type can have one block for each right-hand type: `Mul<f64>` on line 3 scales the vector, and `Mul<Vec2>` on line 7 gives a number.
For a number before `*`, `impl Mul<Vec2> for f64` on line 11 makes `2.0 * v` work too: its `mul` on line 12 turns the operands round and uses line 3's block.
`Mul` and `f64` both come with the language, yet line 11's block is allowed, since a block like this may also live where its right-hand type, `Vec2`, is declared.
Press Run.

Lines 17 and 18 print the same scaled vector.
Line 19 prints `5.0`, from line 7's block.
Line 20 calls `mul` by name, which picks the same block as `v * 2.0`.
The right-hand operand picks a block by its exact type: `v * 2` would be E0404, "no `impl Mul` of `Vec2` takes this operand", since `2` is an integer.

### Step 3: Index operators (read)

`[ ]` is an operator too, but unlike `+` it needs no interface: it goes through two methods of the type's own, `index` and `set_index`.
`set_index` makes `grid[1, 0] = 5` on line 17 write a value, and `index` makes line 19 read it back.
`set_index` takes `mut self`, so `grid` needs `let mut`, as an array does.
Several indexes, as in `grid[1, 0]`, arrive as one tuple, which lines 5 and 10 take apart as `x` and `y`, and a single index is a plain parameter, such as `at: i64`.
They're ordinary methods too: lines 20 and 21 call `set_index` and `index` by name, with the tuple written out.
Press Run.

Line 19 prints `5` and line 21 prints `9`, and line 22 shows where each value landed in `cells`.

## 8.7 Deriving, steps 5 to 8

### Step 5: Writing an item by hand (fix)

A type can write an interface by hand, with an `impl` block, instead of deriving it.
`Author` on line 21 asks for `Describe` with `with`, and `impl Describe for Author` on lines 23 to 25 writes its own.
Press Run.

The program doesn't run.
A type gets each interface one way, from the blocks or by hand, never both.
E0463 says so on line 21: "`Author` both derives and implements `Describe`".
Its help says to keep one.
Keep the `impl`: it then replaces the blocks for `Author`, and `Book` keeps them.
Remove `with Describe` from line 21 and run again, or press Solve.

### Step 6: Overlapping blocks (fix)

A block can take type parameters, as line 9 does: it covers `T[]` for every `T` that has `Describe`.
Line 13 adds a block for `i64[]`.
Line 20's `[1, 2, 3]` is an `i64[]`.
Line 21's `[[1], [2]]` is an `i64[][]`, an array of `i64[]`s, so line 9 covers it with `i64[]` as its `T`.
A block must also be in the module that declares its interface: `derive Display for i64` in this file would be E0452 too, as `impl Display for bool` is E0459.
Press Run.

The program doesn't run.
Each type gets its items from exactly one block, and lines 9 and 13 both cover `i64[]`.
E0452 says so on line 13: "two `derive Describe` blocks cover `i64[]`".
Its help says to remove or narrow one of them.
Remove lines 13 to 15 and run again, or press Solve.

### Step 7: derive.all and derive.fold (read)

`Gauge` on line 1 has two items, and the struct block on line 15 writes both.
Line 7 writes `i64` where the interface says `Self`, since the block is for `i64`; line 16, in the struct block, keeps `Self`.
`derive.all(self, other, near)` on line 16 calls `near` on each pair of matching fields and is `true` when every call is, stopping at the first `false`.
`near` gets the field's name and the two values; there is no `ctx`.
`derive.fold(self, 0, add_up)` on line 17 starts from `0` and passes the running result through `add_up` once per field, as `sum`.
`Reading` on line 20 asks with `with Gauge`.
Press Run.

Both lines show `45` for `a`, `20` plus `25`.
The first is close: each field is within 1 of the other reading's.
The second isn't, since `20` and `23` are 3 apart.

### Step 8: derive.build (read)

An interface item can take no `self`, as `parse` on line 2 does, and it's called on a type, as `T.parse(s)` on line 26.
`derive.build(s.split(","), field)` on line 21 builds a struct one field at a time, calling `field` on line 13 once per field with `F` set to that field's type: `string` for `title` and `i64` for `pages`.
`field` gets the split parts as `ctx`, then the field's name, its position from 0, and the number of fields.
Line 17 parses one part with `F`'s own `parse`, so each field is read at its own type.
The first `Err` stops it and is the result; otherwise it's `Ok` with the struct.
Press Run.

`"Dune,412"` parses into a `Book`.
`"Dune,many"` stops at `pages`, with the `i64` block's `Err`.
`"Dune"` splits into one part, so `field` gives back its own `Err`.

### Step 1: with on your own interfaces (fix)

`with Eq` and `with Key` asked for interfaces the language knows how to build from a type's fields.
An interface of your own can be built from a type's fields too, if it has `derive` blocks that say how.
`Describe` on lines 1 to 3 is one, and its blocks on lines 5, 9 and 15 cover `i64`s, strings and every struct.
The next steps explain lines 5 to 17; this step needs only lines 19 to 24.
`tell` on line 21 takes any `T: Describe`, and line 24 passes it a `Book`.
Press Run.

The program doesn't run.
A struct gets an interface from the interface's blocks only when it asks, as it does for `Eq`, and `Book` on line 19 doesn't ask.
E0422 says so at the call on line 24: "`Book` doesn't implement `Describe`".
`impl Describe for Book = derive;` on a line of its own asks the same way.
Add `with Describe` after the `}` on line 19 and run again, or press Solve.

> **Error note (E0422):** `tell` needs a `Describe`, and `Book` gets one from the interface's `derive` blocks only when it asks, with `with Describe` after its declaration.

### Step 2: Derive blocks (read)

A derive block says, in one place, how a type gets an interface's items.
Line 5 says how every `i64` gets `Describe`, and line 9 does the same for `string`.
`tell` on line 13 takes any `T: Describe`, so lines 16 and 17 call it with either.
A block's items are reached through the interface: through a bound such as `tell`'s, or by naming it, as `Describe.describe(7)` on line 18 does.
Press Run.

Line 16 prints through the `string` block, and lines 17 and 18 through the `i64` block.

### Step 3: Deriving for structs (fix)

`derive Describe for struct` on line 15 covers every struct that asks.
Inside it, `derive.fields(self, (), part)` calls `part` once per field, in order, and gives back an array of the results.
`part` on line 13 is passed to `derive.fields` as a function value, and gets `derive.fields`'s second argument as `ctx`, then the field's name and value.
Here `ctx` is `()`, nothing.
`part` is generic over one `F: Describe`, since each field has its own type.
Line 19's `Book` now has a `price`, an `f64`.
Press Run.

The program doesn't run.
A struct gets `Describe` only when each of its fields does, and no block covers `f64`.
E0451 says so on line 19, where `Book` asks: "`price` is `f64`, which no `derive Describe` block covers".
A struct's `describe` is reached only through the interface: `Book { … }.describe()` is E0415.
After line 11, add a `derive Describe for f64` block with `fun describe(self): string = "{self}";` in it, and run again, or press Solve.

> **Error note (E0451):** `Book` asks for `Describe`, so each of its fields needs it too, and no `derive` block covers `price`, an `f64`.

### Step 4: Deriving for enums (read)

`derive Describe for enum` on line 15 covers every enum that asks, as `Shape` does on line 22.
`derive.variant(self, (), part)` on line 17 gives a tuple: the variant's name, and an array of what `part` returns for each payload.
Each payload has no name of its own, so `part` gets the variant's name, unused here.
`Dot` has no payloads, so its array is empty.
`derive.index(self)` on line 18 is the variant's position in the enum, counting from 0.
Press Run.

Each line starts with that position, then the variant's name and its payloads, each described by the `i64` or `string` block.

# 9. Iterators

## 9.1 Iterators

### Step 1: Iterators (read)

Besides arrays, `for … of` steps through iterators: an iterator hands out its values one at a time.
Line 2 loops over `range(1, 4)`, an iterator over the same numbers as the range `1..4`.
Line 5 loops over `"hé".chars()`, the string's characters, and line 8 over `"hé".bytes()`, its bytes.
Line 11 makes an iterator over an array's items with `iter()`, and line 12 loops over it.
Press Run.

The first loop prints `1` to `3`.
The second prints the two characters, `h` and `é`.
The third prints three bytes: `104` is the `h`, and `195` and `169` are the `é`, one character but two bytes.
The last loop prints the array's items, `10` and `20`.

### Step 2: Chaining iterators (read)

Iterators have `map` and `filter` too, and each gives back another iterator, so they line up one after another.
Line 2 starts from `range(1, 10)`, the numbers 1 to 9, keeps the multiples of 3 with `filter`, and squares them with `map`.
`collect()` at the end of the line puts the results in an array.
On line 4, `chain` gives the values of `[1, 2].iter()`, then those of `[3, 4].iter()`, and `collect()` gathers them too.
Press Run.

The first line is the squares of 3, 6 and 9.
The second holds both arrays' items in one array.

### Step 3: enumerate (read)

`enumerate()` pairs each value with its position, counting from 0.
Line 3 loops over `names.iter().enumerate()`.
Each item it gives has two fields, `i` for the position and `value` for the value, and line 4 prints both.
Press Run.

Each name prints after its position, from `0: Ann` to `2: Cy`.

### Step 4: zip (read)

`zip` walks two iterators side by side and gives a tuple for each pair of values.
Line 4 zips `names` with `ages`, and the loop takes each tuple apart into `name` and `age`.
`names` has three names, but `ages` has only two numbers.
Press Run.

Two lines print, one for `Ann` and one for `Ben`.
`Cy` isn't printed: `zip` stops at the end of the shorter one.

### Step 5: Laziness (read)

On an array, `map` runs its closure at once and makes a new array.
Line 2 calls `map` on `[1, 2, 3].iter()` instead, with a closure that prints `doubling` and the number before doubling it.
Line 6 prints `made the iterator`.
Line 7 takes two values from `doubled` with `take(2)` and collects them.
Line 8 starts from a range of numbers up to a billion, keeps the multiples of 7, passes over one with `skip(1)` and takes three with `take(3)`.
Press Run.

`made the iterator` comes first: `map` on an iterator runs nothing yet.
The closure runs only when line 7 pulls values, so `doubling 1` and `doubling 2` come next, then `[2, 4]`.
`take(2)` pulls only two, so `3` is never doubled.
The last line is `[21, 28, 35]`: `skip(1)` passed over 14, the first multiple of 7, and `take(3)` stopped pulling once it had three.
That's why line 8 can start from a range up to a billion.

### Step 6: More adapters (read)

A few more helpers give back an iterator, like `map` and `filter`.
Arrays don't have `take_while`, `skip_while` or `flat_map`, or `take` and `skip` (`xs.take(2)` is E0415, "no method `take` on `i64[]`"), so lines 3, 4 and 6 call `.iter()` first.
On line 3, `take_while` takes values while its closure holds, and stops at the first that fails.
On line 4, `skip_while` skips values while its closure holds.
On line 6, `flat_map` turns each word into an iterator over its characters, and gives their values in turn.
Line 7 collects `"hi".bytes()`, the bytes of a string.
Press Run.

The first line is `[3, 5]`: `take_while` stops at the `9`.
The second is `[9, 4, 8]`: once `9` fails, `skip_while` stops checking, so `4` comes through too.
The third is each word's characters, with their quotes: a `char` keeps them in its debug form, as a string does.
The last is the bytes of `hi`, as `u8` numbers.

## 9.2 Using up an iterator

### Step 1: collect, sum, count and find (read)

Some helpers use an iterator up: they pull its values and give back one answer instead of another iterator.
Line 2 makes `scores`, an iterator over four numbers, and every line after it uses the same `scores`.
Lines 3 and 4 add the values up with `sum()` and count them with `count()`.
`find` on line 5 gives the first value its closure returns `true` for, as an `Option`, since there may be none.
`min`, `max` and `position` on lines 6 to 8 give an `Option` for the same reason.
Line 9 ends a `filter` with `collect()`, another of these helpers.
Press Run.

Each helper works on its own copy of the iterator, so every line starts again from `7`.
The sum is `23`, and `count()` still finds four values.
`find` gives `Some(9)`, the first score above 8, and `min` and `max` give `Some(3)` and `Some(9)`.
`position` gives `Some(2)`: `9` is at position 2, counting from 0.
The last line holds the scores above 5.

### Step 2: collect_map and collect_set (read)

An iterator can end in a set or a map instead of an array.
`collect_set()` on line 3 keeps each name once, in the order first seen.
`collect_map()` on line 5 needs tuples of a key and a value, as `scores` on line 4 holds.
Press Run.

The set holds `"ann"` once, then `"bo"`.
In the map, `"ann"` comes twice: it keeps its first place, and its later value, `3`, wins.

### Step 3: The loop's copy (read)

Line 2 makes `it`, an iterator over three numbers.
The loop on lines 3 to 5 goes through every value, and lines 6 and 7 use `it` again afterwards.
Press Run.

The loop prints `1` to `3`.
A loop like line 3's, `for x of it`, works on a copy of the iterator, as a helper does, so `it` is unchanged after the loop.
That's why `count()` on line 6 still finds three values, and `take(1)` on line 7 still starts from `1`.

## 9.3 Your own iterators

### Step 1: impl Iter (fix)

A type becomes an iterator by implementing the interface `Iter<T>`, whose one method is `fun next(mut self): Option<T>`, giving `Some` with the next value or `None` at the end.
A `for … of` calls `next` until it gets `None`.
Here `Countdown`'s `next`, on lines 4 to 10, is in a plain `impl Countdown`.
Line 14 loops over a `Countdown` (a struct literal after `of` needs its parentheses), and line 17 filters one.
Press Run.

The program doesn't run: a method named `next` isn't enough.
E0411 on line 14 says it "cannot iterate over `Countdown`", and its help names what a loop needs: `impl Iter<T> for Countdown`.
Without that `impl`, `Countdown` has no `filter` either: E0415 on line 17.
E0412 follows from it: with no `filter`, nothing says what type the closure's `n` is.
Change `impl Countdown` on line 3 to `impl Iter<i64> for Countdown` and run again, or press Solve.

> **Error note (E0411):** A loop needs a type that implements `Iter<T>`. `Countdown` has a `next` of its own but no `impl Iter<i64> for Countdown`, so line 14 can't loop over it.

### Step 2: Iterators in generic code (read)

`Iter<i64>` is an interface, so it can be a bound on a type parameter.
`total` on line 13 takes any `I` that is an `Iter<i64>`, and its loop on lines 15 to 17 adds up the values.
Line 22 passes it a `Countdown` from 4, line 23 a `range` from 1 to 4, and line 24 a `map` over an array's iterator: three different iterators, each an `Iter<i64>`.
Press Run.

The `Countdown` gives 4, 3, 2 and 1, which add up to `10`.
The range gives 1 to 4, also `10`.
The `map` gives `20` and `30`, so the last line is `50`.

# 10. Capabilities

## 10.1 What main is given

### Step 1: Capabilities in main (read)

Every program so far has taken `console: Console` and printed its output through it.
Files, the clock, environment variables, randomness, other programs and the network are reached the same way: through a value `main` is given, called a capability.
`debug` and `panic` write to standard error without one.
`main` takes the ones it needs as parameters, matched by type, with any names, in any order: `Console`, `Fs`, `Clock`, `Env`, `Entropy`, `Proc` and `Net`, and `string[]` for the program's arguments.
Line 1 takes a `Clock`, then the `Console`.
Line 2 reads the clock with `monotonic_ms()`, a time for measuring how long something takes, and line 4 reads it again.
Press Run.

`hello` prints from line 3.
Then `true`: the second reading, on line 4, is no earlier than the first.

### Step 2: Each one once (fix)

Line 1 asks for two consoles, `console` and `out`.
Press Run.

The program doesn't run.
E0304 on line 1 lists everything `main` can take, each at most once: `string[]`, the capabilities, and the root `Scope`, which concurrent code uses.
It also says `main` returns `()` or `i32`, and its help shows a `main` that fits.
A parameter `main` can't be given at all, such as `n: i64`, is E0304 too.
Remove `, out: Console` from line 1 and run again, or press Solve.

> **Error note (E0304):** `main` is given its parameters when the program starts, matched by type, and it can take each capability only once. Line 1 asks for a `Console` twice, as `console` and `out`.

### Step 3: Passing capabilities on (read)

`timed` on line 1 takes a `Console` and a `Clock` as ordinary parameters.
`main` on line 8 is given both, and passes them on to `timed` on line 9.
There are no global `println`, clock or file functions: a function reaches these only through a capability it's given.
Press Run.

`timed` prints `working on the report` through the console it was given.
Then `true`: `took`, the time it measured with the clock, isn't below 0.

### Step 4: Arguments (read)

`args: string[]` on line 1 holds what the program was started with: its own path first, then any arguments.
Line 2 prints how many there are.
Lines 3 to 6 print a usage line and return exit code 1 when no name follows the path.
Line 7 greets each name, skipping the path with `skip(1)`.
Here the program starts with no arguments after its path.
Press Run.

The first line is `1`: `args` holds only the path.
So the program prints the usage line, and the panel shows "Exited with code 1".
In the Playground, the input tab passes arguments: with `Ann Ben` it prints `3`, `hello, Ann` and `hello, Ben`.

## 10.2 Files

### Step 1: Fs and Dir (read)

`main` on line 1 takes `fs: Fs`, the capability for files.
`fs.cwd()` on line 2 gives the folder the program runs in, as a `Dir`, a value whose methods work on the files in it.
Line 3 reads `notes.txt` with `read_file`, which gives a `Result<string, string>`: the file's text, or an error message.
Line 4 prints the text with `console.print`, which adds no line break of its own, and line 5 prints the error.
Each run starts without a `notes.txt`.
Line 7 writes the file with `write_file`, replacing anything already in it, and line 8 adds to its end with `append_file`.
Lines 9 to 12 read and print it again.
Press Run.

The first line comes from line 5: line 3 got an `Err`, holding the system's own message for the missing file.
`Ok(5)` twice comes from lines 7 and 8: each gives `Ok` with the number of bytes written, a word and its line break.
Then the file's text, `milk` and `eggs`, from line 10.

### Step 2: Folders (read)

Folders are made and removed through a `Dir` too, and every method that can fail gives a `Result`, so `tidy` on line 1 returns one and uses `?` after each call.
`make_dirs` on line 2 makes `out` and `out/logs` at once, and line 3 writes a file in `out/logs`.
`list` on line 4 gives the names in a folder, and `exists` on line 5 a `bool`.
Lines 6 and 7 remove the file and then the folder, which must be empty, and line 8 lists `out` again.
Press Run.

The first line is the names in `out`, `["logs"]`, in an `Ok`.
`true` says the file was there.
After the two removals, `out` is empty: `Ok([])`.

### Step 3: Confinement (read)

Line 3 reads `../secret.txt`, which climbs out of `dir`'s folder, and line 4 an absolute path, `/etc/hostname`.
Line 5's `src/../lugha.toml` goes into `src` and back, so it stays inside.
`fs.dir` on line 6 opens another folder, by any path, as a `Dir` of its own, and line 7 writes a file in it.
Press Run.

The first two lines are `Err("path leads outside the folder")`: lines 3 and 4 were refused, without the file being read.
`true` is line 5's read, which worked.
`Ok(2)` is line 7 writing two bytes into `/tmp`, through the `Dir` that `fs.dir` opened: reaching outside a `Dir` takes the `Fs` itself.

### Step 4: ReadDir (fix)

`count_lines` on line 1 takes a `ReadDir`, a folder that can only be read, and line 10 passes it `dir.read_only()`.
A `ReadDir` has `read_file`, `list`, `exists` and the other reading methods, and none that writes, makes, renames or removes anything.
Line 3 writes a file through it.
Press Run.

The program doesn't run: this is caught before it starts, while step 3's paths were an `Err` as it ran.
E0415 on line 3 says there's "no method `write_file` on `ReadDir`", and its help says "a `ReadDir` only reads; take a `Dir` to write".
So a `ReadDir` parameter shows that `count_lines` only reads.
Remove line 3 and run again, or press Solve.

> **Error note (E0415):** A `ReadDir` has only reading methods, so it has no `write_file`, and line 3 tries to write through one.

### Step 5: A narrower Dir (read)

Line 9 makes the folder `data`, and `here.dir("data")` on line 10 opens it as a `Dir` of its own, confined to that folder.
`save` on line 1 gets only `data`: line 2 writes a file in it, and line 3 writes `../escape.txt`, in its parent.
Lines 14 and 15 check from `here` which files were written.
Press Run.

`Ok(())` is line 9 making `data`.
Then `save` gives the same `Err` as in step 3: `../escape.txt` would land in `here`, but from `data` it climbs out of the folder, so `save` stops at line 3's `?`.
`true` and `false` come from lines 14 and 15: `count.txt` was written, and `escape.txt` never was.

## 10.3 The console

### Step 1: Reading input (read)

The `Console` reads too: `console.read_line()` gives the next line of the program's input, without its `\n`.
It's a `Result<Option<string>, string>`: `Ok(Some(line))` for a line, `Ok(None)` once the input has ended, and an `Err` when it can't be read.
The `while let` on line 4 keeps reading as long as `read_line` gives a line, and stops at the end of the input or at an `Err`.
Line 5 counts the lines, and line 6 adds each one up as a number, or 0 when it isn't one.
Here the program starts with no input.
Press Run.

The first `read_line` is already `Ok(None)`, so the loop never runs, and line 8 prints `0 lines, total 0`.
In the Playground, the input tab gives a program its input: with `3`, `4` and `10` on three lines it prints `3 lines, total 17`.

### Step 2: stdout and stderr (read)

A program has two outputs: standard output, where `println` writes, and standard error, where `eprintln` writes, for messages about the run rather than its results.
`noisy` on line 1 writes one line to each, and line 7 calls it with the console.
Line 8 passes `noisy` a narrower `Console`, `console.stdout_only()`, whose `eprint` and `eprintln` do nothing and which has no input to read.
`console` itself still writes to both.
Press Run.

Both calls print `result: 42`.
The panel shows standard output first and standard error after it, so the note, marked `(stderr)`, comes last, though the first call wrote it.
There's only one note: the second call's `eprintln` went through `stdout_only()`, so it did nothing.

## 10.4 Clock, Env and Entropy

### Step 1: Clock (read)

A `Clock` tells the time two ways.
`now_ms()` on line 2 is the current time, in milliseconds since the start of 1970 (UTC).
`monotonic_ms()` on lines 4 and 9 counts from no particular moment but never goes back, so the difference between two readings is how long the loop on lines 6 to 8 took.
Line 10 prints the loop's total.
Press Run.

The first `true` is line 3: the current time is past mid-November 2023.
`2999997` is the loop's total.
The last `true` is line 11.
How long the loop took changes from run to run, so line 11 prints only whether it's at least 0.

### Step 2: Env (read)

An `Env` reads the program's environment variables, the named settings a program is started with.
`get(name)` gives an `Option<string>`: `Some` with the value, or `None` when the variable isn't set or can't be read as text.
Line 9 asks whether `PATH` is set, and line 10 asks for a variable nobody sets.
`greeting` on line 1 matches on `env.get("USER")`, and line 11 prints what it gives.
`env.only(["HOME"])` on line 12 gives a narrower `Env` that reads only `HOME`, and line 13 asks it for `PATH`.
Here the program runs with `PATH` set and `USER` not set.
Press Run.

`true` is line 9: `PATH` is set.
`None` is line 10.
`USER` isn't set, so `greeting` takes its `None` arm.
The last `None` is line 13: through `narrow`, every variable but `HOME` looks unset, `PATH` too.

### Step 3: Entropy and random numbers (read)

An `Entropy` gives random bytes from the system: `entropy.bytes(16)` on line 4 is 16 of them, the kind for keys and tokens.
For random numbers, line 1 imports `std.random`: an `import` makes a module, a named group of functions, usable in this file, here the standard library's `random`, which lines 6, 9 and 10 use as `random.`.
`random.from_entropy(entropy)` on line 6 makes a generator, an `Rng`, seeded from the system.
`rng.between(1, 7)` on line 7 is a whole number from 1 up to 6.
`rng` is `let mut` because every `Rng` method takes `mut self`: each call changes the generator, so the next call gives its next number.
`random.seeded(42)` on lines 9 and 10 seeds two generators from the same number instead.
Press Run.

`16` is the key's length, from line 5.
The first `true` is line 8: the roll is from 1 to 6.
The second is line 11: generators with the same seed give the same numbers in the same order, so the two rolls are equal.

## 10.5 Other programs and the network

### Step 1: Proc (read)

A `Proc` starts other programs.
`proc.run(cmd, args)` on line 2 runs `echo` with two arguments, `hello` and `$HOME; rm -rf /`.
It gives an `Ok(ProcessOutput)`, with the program's exit `code`, its `stdout` and its `stderr`.
`run_with` on line 4 also writes to the program's input, here two lines for `sort`.
Line 6 starts `sh` as an ordinary program, with `-c` and `exit 3` as its arguments.
Line 8 names a program that doesn't exist.
Press Run.

The first line is `echo`'s exit code, `0`, then its output, with `$HOME; rm -rf /` exactly as written.
Each argument goes to the program as it is, with no shell in between, so `$HOME` isn't replaced and `;` doesn't start a second command.
`apple,pear` is `sort`'s output, its lines joined by line 5.
Line 7 prints `3`: any exit code counts as `Ok`, so `unwrap` on line 6 gets the output.
Line 8's program couldn't be started, so the last line is an `Err`, holding the system's own message.

### Step 2: Net (read)

A `Net` reaches the network: `net.connect("example.com:80")` on line 2 opens a connection to a host and port, and gives `Ok(Conn)` or an `Err`.
The programs on this site run without a network.
Press Run.

So the connection is an `Err`, and line 4 prints it after `can't connect:`: the system's own message, saying the name `example.com` couldn't be looked up.

## 10.6 Faking a capability

### Step 1: Capabilities are interfaces (fix)

Each capability is an interface, so a type of your own can implement it.
`FixedClock` on line 1 is a clock that always says the same time, and `impl Clock for FixedClock` on lines 3 to 6 gives it `now_ms` and `monotonic_ms`.
Line 11 puts one in a variable of type `Clock`, an interface value.
Press Run.

The program doesn't run.
E0422 on line 3 says the `impl` "doesn't match `Clock`", and its help names what's missing: "no method `local_offset`".
Besides the two methods shown earlier, `Clock` has a third, `local_offset`: the local time's offset from UTC at a moment, in seconds.
An `impl` has to write every method the interface doesn't give a default for.
After line 5, add `fun local_offset(self, ms: i64): Result<i64, string> = Ok(0);`, an offset of 0, and run again, or press Solve.

> **Error note (E0422):** `impl Clock for FixedClock` has to write every method of `Clock`, and `Clock` has three. Lines 4 and 5 write `now_ms` and `monotonic_ms`, but nothing writes `local_offset`.

### Step 2: Using a fake (read)

`greeting` on line 9 takes a `Clock`, works out the hour in UTC from `now_ms()` on line 10, and picks a greeting on line 11.
It only calls `now_ms()`, so any `Clock` will do.
Lines 15 and 16 give it a `FixedClock` at 08:00 and at 14:00 UTC on 1 January 2026, and line 17 the real clock `main` was given.
Press Run.

The fake at 08:00 gives `good morning`, and the one at 14:00 `good afternoon`.
The real clock's answer depends on when the program runs, so line 18 prints only whether it's one of the two, and it is: `true`.

# 11. Modules and tests

## 11.1 Modules

### Step 1: Multiple files (read)

A program can be split across several files, and each file is a module.
`src/shapes.la`, in the file list, is the module `shapes`: a module's name is the file's path from the folder `main.la` is in, without `.la`.
It declares the struct `Square` on line 1 and two functions on lines 3 and 5.
Line 1 of `src/main.la`, `import shapes;`, loads that module and binds the name `shapes`, and lines 4 to 6 reach its items through that name, with `shapes.` in front.
Nothing in `shapes.la` needs marking for this: an item with no marking can be used by every file of the same program.
Press Run.

The output panel shows `a square of side 3.0`, from `shapes.describe` on line 5, then `9.0`, the area from `shapes.area` on line 6.

### Step 2: import (fix)

`src/main.la` is the same as before without its `import` line, and `src/shapes.la` hasn't changed.
Press Run.

This time the program doesn't run.
Having `shapes.la` in the project isn't enough: without the `import`, nothing in `main.la` binds the name `shapes`.
E0305 comes first: it can't find the type `shapes.Square` on line 2.
The two E0301 errors say the same about `shapes` in the calls on lines 3 and 4: nothing in scope is called `shapes`.
Add `import shapes;` as a new line 1 of `src/main.la`, with an empty line after it, and run again, or press Solve.

> **Error note (E0305):** `shapes.Square` names a type in the module `shapes`, but this file has no `import shapes;`, so the name `shapes` means nothing here.

### Step 3: Import aliases (fix)

The name an import binds can be changed with `as`: line 1 of `src/main.la`, `import shapes as geo;`, binds the module as `geo`.
That's how one file can use two modules that would otherwise bind the same name.
Line 5 calls `geo.area`, but line 4 still writes `shapes.Square`.
Press Run.

The program doesn't run.
With `as geo`, only `geo` is bound in this file, and `shapes` isn't, so E0305 can't find the type `shapes.Square` on line 4.
Change `shapes.Square` to `geo.Square` on line 4 and run again, or press Solve.

> **Error note (E0305):** With `import shapes as geo;`, this file knows the module only as `geo`, so `shapes.Square` names nothing here.

### Step 4: Named imports (read)

An import can also list items after the module's name, and those are written without the module's name in front.
Line 1 lists `Square`, so line 4 builds one as plain `Square`.
`area as square_area` brings in `area` under the name `square_area`, which line 5 calls.
`shapes.describe` on line 6 still works, since the import binds `shapes` as well.
Press Run.

The output panel shows `9.0` from line 5, then `a square of side 3.0` from line 6.

## 11.2 Visibility

### Step 1: private (fix)

`private` in front of an item keeps it inside its own module.
In `src/shapes.la`, line 7 declares `square` as `private`, and `area` on line 3 calls it from inside the module.
Line 6 of `src/main.la` calls `shapes.square` directly.
Press Run.

The program doesn't run.
`main.la` is another module, so it can't reach `square`: E0313 says "`square` is private to module `shapes`", at line 6 of `src/main.la`.
Its help says only `shapes` can use it, and that removing `private` would share it.
There's no need here: `main.la` can call `area`, which calls `square` from inside `shapes`.
Change line 6 of `src/main.la` to print `shapes.area(s)` and run again, or press Solve.

> **Error note (E0313):** `square` is marked `private` in `shapes.la`, so only code in that file can call it, and `main.la` is a different module.

### Step 2: Package visibility (read)

Without `private`, an item is visible in every module of its package, not only its own.
A package is what a `lugha.toml` describes: this one, in the file list, names the package `geometry`, and both `.la` files belong to it.
A program without a `lugha.toml` is one package too.
So `src/main.la` can build a `shapes.Square` on line 4, read its `side` field on line 5 and call `shapes.area` on line 6.
Press Run.

The output panel shows `3.0`, the `side` that line 5 reads, then `9.0` from `shapes.area` on line 6.

### Step 3: public (fix)

`public` makes an item visible to other packages too, the ones that import its module.
Line 3 of `src/shapes.la` declares `unit` as `public`, but it returns a `Square`, and line 1 declares `Square` with no keyword.
This program is one package, with no other package to import it.
Press Run.

The program doesn't run, even with no other package here.
Another package could call `unit` but couldn't name the `Square` it returns, so a `public` declaration's parameter and return types must be `public` too.
E0318 says so, at line 3 of `shapes.la`.
Its help gives two ways out: make `Square` `public`, or drop `public` from `unit`.
Either would build here, since `main.la` is in the same package, but making `Square` `public` keeps `unit` usable by other packages.
The field `side` can stay without one: `main.la`, in the same package, reads it on line 5, though another package couldn't.
Add `public` before `struct Square` on line 1 of `shapes.la` and run again, or press Solve.

> **Error note (E0318):** `unit` is `public`, so another package could call it, but it couldn't name the `Square` it gets back, since `Square` isn't `public`. A `public` function's parameter and return types must be `public` too.

### Step 4: Private fields (fix)

A field can be `private` too, and then only its own module can set or read it.
In `src/range.la`, line 1 makes both of `Range`'s fields `private`.
`Range.new`, on lines 4 and 5, puts the smaller number in `lo`: it swaps `a` and `b` when `a` is larger.
Line 4 of `src/main.la` builds a `Range` with a literal instead, with `lo` above `hi`.
Press Run.

The program doesn't run.
It's E0313 again, this time for a field: "`hi` is private to module `range`", at line 4 of `src/main.la`.
Outside its module, a struct literal needs every field it sets to be visible, and the error names `hi`, one of the two private fields this literal sets.
The help says to build the `Range` with one of `Range`'s functions, which here means `new`.
Change line 4 of `src/main.la` to `let r = range.Range.new(5, 1);` and run again, or press Solve.

### Step 5: Re-exports (fix)

A module in a folder is named with a dot: `src/geo/square.la` is the module `geo.square`, and it declares `Square` and `area`, both `public`.
Line 1 of `src/shapes.la` imports both, with no keyword in front of `import`.
`src/main.la` imports only `shapes`, and uses the two as `shapes.Square` on line 4 and `shapes.area` on lines 5 and 6.
Press Run.

The program doesn't run.
The names an import brings in are private to the module that imports them, here `shapes`, so each use in `main.la` is an E0313, on lines 4, 5 and 6.
Each help says to remove `private`, though there's none to remove: an import's names are private without one.
`public` in front of the import makes the two part of `shapes`, visible to every package, as if `shapes` declared them `public`.
Add `public ` at the start of line 1 of `shapes.la` and run again, or press Solve.

> **Error note (E0313):** `shapes.la` imports `Square` and `area` on line 1, but an import's names stay private to the module that imports them, so `main.la` can't reach them through `shapes`.

## 11.3 Tests

### Step 1: Test functions (read)

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

### Step 2: assert_eq and assert_ne (fix)

`assert` only says that it failed, so line 6 of `test/shapes_test.la` uses `assert_eq(a, b)` instead, which fails unless `a` and `b` are equal.
`assert_ne` on line 13 fails if they are equal.
When `assert_eq` fails, it shows both values, the first as left and the second as right.
When `assert_ne` fails, it shows the value both have.
In `src/shapes.la`, `area` on line 3 multiplies the side by `2.0`.
Press Test.

`area_of_three` is `FAILED`, and the line under it gives the panic: "assert_eq failed: left 6.0, right 9.0".
`area` gave 6.0, and the test expects 9.0.
`at shapes_test.la:6:5` is line 6 of the test file, where `assert_eq` was called.
`bigger_side_bigger_area` is `ok`, since the two areas still differ, and the last line counts 2 tests: 1 passed, 1 failed.
A square's area is its side multiplied by itself, not by `2.0`.
Change `2.0` to `s.side` on line 3 of `src/shapes.la` and press Test again, or press Solve.

### Step 3: Running tests (fix)

`largest`, on lines 5 to 13 of `src/shapes.la`, should give the largest of an array of squares, or `None` for an empty one.
The test file checks both: `largest_of_none` on line 4 gives it an empty array, and `largest_of_two` on line 10 gives it two squares.
Press Test.

`largest_of_none` is `FAILED`, with the panic "index out of bounds: the length is 0 but the index is 0" at line 6 of `src/shapes.la`.
That line reads `squares[0]` before checking that there is one.
Each test runs as its own process, so `largest_of_two` still runs, and it's `ok`.
The last line, "2 tests: 1 passed, 1 failed", counts the whole run.
Run builds the program without its tests, so only Test runs them.
After line 5 of `src/shapes.la`, add `if squares.len == 0 { return None; }` on three lines and press Test again, or press Solve.

## 11.4 Testing with capabilities

### Step 1: A fresh folder (read)

A test can take capabilities as parameters too, matched by type: `Console`, `Dir`, `Clock`, `Env`, `Entropy` and `Net`.
It can't take `Fs`: it takes `dir: Dir` instead, a folder made for that test alone.
`counts_lines_in_a_fresh_folder`, on line 11, takes one, and line 12 checks that it's empty.
Line 13 writes a file there, and lines 14 and 15 check `count_lines` on it and on a file that isn't there.
Press Test.

The Tests tab shows the test `ok`: its folder held nothing until line 13, and the program's own files aren't in it.
Tests in `src` are named by package and module, and tests in `test/` by their path.
With no `lugha.toml` of its own, a program on this site is the package `playground`, so this test's name starts `playground.main.`.

### Step 2: Fixed stand-ins (read)

A test's `Clock`, `Env` and `Entropy` are stand-ins too, not the real ones.
Its `Clock`, on line 6, is fixed: `now_ms()` is `946684800000`, midnight UTC on 1 January 2000, and `monotonic_ms()` is `0`.
Its `Env`, on line 12, is empty, so even `PATH` is `None`.
Its `Entropy`, on line 17, is seeded, which means it gives the same bytes on every run: line 18 checks the four it gives this test, and another test would get other bytes.
Press Test.

All three tests are `ok`, and the last line counts 3 passed and 0 failed.

### Step 3: Fakes in tests (fix)

`greeting`, on lines 1 to 4, says `good morning` before 12:00 UTC and `good afternoon` after.
`FixedClock`, on lines 6 to 12, is a `Clock` whose time is whatever its `at` field holds.
The test on line 19 takes the test's `Clock` and expects `greeting` to say `good afternoon`.
Press Test.

`afternoon` is `FAILED`: the test's `Clock` is the fixed stand-in, at midnight UTC on 1 January 2000, so `greeting` says `good morning`.
The panic under it shows both values, left "good morning" and right "good afternoon", from `assert_eq` on line 20.
To test the afternoon, give `greeting` a `FixedClock` set to an afternoon hour: `1767276000000` is 14:00 UTC on 1 January 2026.
Make line 19 `fun afternoon() {`, with no parameter, and line 20 `assert_eq(greeting(FixedClock { at: 1767276000000 }), "good afternoon");`, and press Test again, or press Solve.

### Step 4: Virtual time (read)

`task.sleep(ms)`, from the module `std.task` that line 1 imports, pauses for that many milliseconds.
On this site each test has 5 seconds to run, and the test on line 8 sleeps for 10 seconds on line 9.
Press Test.

The test is `ok` at once.
A test runs on virtual time, where sleeping takes no real time, so the 10 seconds pass without any waiting.

# 12. Concurrency

## 12.1 Tasks and scopes

### Step 1: scope and spawn (read)

A task is a function call that runs at the same time as the rest of the program, and it starts in a scope.
A scope is a block, `scope s { … }` on lines 4 to 7, and `s` is its handle, the name its tasks are started through.
Line 5 starts a task with `s.spawn(square(7))`, and line 6 waits for the task's answer with `join`.
`join` gives `Ok` with the answer, and `unwrap` takes it out.
A scope is an expression: its value is a `Result`, `Ok` with what its body gives, which line 8 prints.
Press Run.

The output panel shows `Ok(49)`: the task worked out `square(7)`, line 6 unwrapped it as the body's value, and the scope gave that back in `Ok`.

### Step 2: join (read)

Lines 11 and 12 start two tasks, which run at the same time, each adding up the numbers from 0 to below its `n`.
`t.join()` waits for a task to finish, and when it has finished normally, gives `Ok` with what the task returned.
Lines 13 and 14 print what `join` gives for each task.
A task can be joined more than once: line 15 joins both again and adds their answers up as the body's value.
Press Run.

The first two lines are `Ok` with each task's sum, from lines 13 and 14.
The third, from line 17, is the scope's value: `Ok` with the two sums added up.

### Step 3: A scope waits (read)

`slow` on line 3 sleeps for 200 milliseconds with `task.sleep`, then prints.
Outside a test, it really sleeps: virtual time is only for tests.
Line 10 starts `slow` as a task and never joins it, and line 11 prints at once, at the end of the scope's body.
Line 13 prints after the scope.
Line 9 keeps the scope's value in `r` without using it: a scope gives a `Result`, and a `Result` used as a statement is E0467.
Press Run.

`the body is done` comes first, from line 11, while the task is still asleep.
The scope doesn't end with its body: it waits for every task it started, so `the task is done` comes next.
Only then does the scope end, and line 13 prints `the scope is done`.

### Step 4: The root scope (read)

`main` can also take `root: Scope`, by type like a capability, as on line 8.
It's a scope as long as the program, and the program waits for its tasks before it ends.
Line 9 starts `later` in it, and line 10 is `main`'s last line.
Press Run.

`main returns` comes first: `main` reaches its end while `later` is still asleep.
The program doesn't end there: `the task finishes` comes next, and "Exited with code 0" only after it.

### Step 5: Tasks stay put (fix)

`s.spawn` gives back a `Task`, a handle on the task it started.
Line 5 keeps two tasks in an array, and line 6 joins them from it.
Press Run.

The program doesn't run.
A `Task` or a `Scope` is kept in a local or passed as an argument, and nothing else: it isn't returned, or put in an array, a field or a closure.
So each place this code holds a task in a value is an E0472, "a scope or task handle can't be stored in a value": the array on line 5, then `ts[0]` and `ts[1]` on line 6.
Each help says the same: keep the handle a local, and finish the tasks inside the scope that started them.
Replace line 5 with `let a = s.spawn(square(2));` and `let b = s.spawn(square(3));`, and line 6 with `a.join().unwrap() + b.join().unwrap()`, and run again, or press Solve.

## 12.2 Failure and cancellation

### Step 1: All or nothing (read)

A task that returns a `Result` fails when it gives an `Err`, and a task that panics fails too.
Line 17 starts `worker`, which would sleep two seconds, and line 18 starts `check(-1)`, which gives an `Err` after a tenth of a second.
`worker` defers a line on line 4, and prints another on line 6 if it gets that far.
Press Run.

`body waits` comes first, from line 19, while both tasks sleep.
By default a scope is all or nothing: when `check` fails, the scope cancels `worker`, which stops in its sleep and runs its `defer` on the way out, so `worker cleans up` comes next.
`worker finished` never prints.
The scope's value is an `Err`, so line 21 prints `true`.

### Step 2: Failure (read)

A scope's `Err` holds a `Failure`, with the failing task's name in `f.task` and how it failed in `f.kind`.
`f.kind` is `.Error(e)` for a task that gave `Err(e)`, `.Panic(m)` for one that panicked, and `.Deadline` for a scope that ran out of time.
`report` on line 13 matches on it.
Lines 25 to 33 give `report` three scopes: one whose task fails with an `Err`, one whose task panics, and one whose task is fine.
A task is named after the function it calls, so the first two are `check` and `crash`.
Press Run.

The first line comes from the `.Error(e)` arm on line 17, with `check`'s message as `e`.
The second comes from the `.Panic(m)` arm on line 18: a panic's message ends with where it happened, so `m` ends with `at src/main.la:8:9`, the `panic` on line 8.
The third scope's task is fine, so its value is `Ok`, and line 15 prints `all done`.

### Step 3: independent (read)

`independent` after the scope's name, as on line 13, lets each task fail alone: when one fails, the others run on and the scope stays `Ok`.
Line 14 starts `crash`, which panics at once, and line 15 starts `slow`, which takes 200 milliseconds.
Lines 16 and 17 join each.
A join gives `Err` when the task didn't finish normally, with why it stopped.
Press Run.

The first line, from line 16, is `crash`'s join: `Err` with `Panicked` and the panic's message.
The second, from line 17, is `Ok(7)`: `slow` finished though `crash` failed first.
The third is the scope's value, `Ok(())`.
The line marked `(stderr)` is the panic's message again, as ``task `crash` panicked: …``.
In step 2, a scope that wasn't `independent` reported the failure in its value; an `independent` scope stays `Ok`, so it prints each failure to standard error instead, once the task has stopped.

### Step 4: cancel (read)

`t.cancel(why)` stops one task, with a reason.
Line 11 starts `wait_long`, which would sleep five seconds and defers a line on line 4.
Line 13 cancels it a tenth of a second later, and line 14 joins it.
Press Run.

`stopped waiting` comes first: the task stops in its sleep and runs its `defer`.
The join on line 14 gives `Err(Cancelled(Requested("no longer needed")))`: the task was cancelled on request, with the reason given on line 13.
Cancelling one task doesn't fail the scope, so its value, on the last line, is `Ok(())`.

### Step 5: limit (read)

`limit 2` after the scope's name, as on line 10, lets at most two of its tasks run at once: a third `s.spawn`, on line 13, waits until one of them has finished.
Lines 11 to 14 start four `job`s, each 200 milliseconds long.
Line 9 reads the clock before the scope and line 17 after it, and line 19 prints whether the scope took at least 400 milliseconds.
Press Run.

`Ok(100)` is the scope's value, the four answers added up.
Two at a time, four jobs take at least two rounds of 200 milliseconds, so line 19 prints `true`.
Without `limit 2` all four run at once, in about 200 milliseconds, and it prints `false`.

## 12.3 Deadlines

### Step 1: within (read)

`within 500` after a scope's name, as on lines 9 and 14, gives it a deadline: 500 milliseconds from when it starts.
If the scope is still running then, its body and tasks are cancelled, and its value is an `Err` whose `f.kind` is `.Deadline`, unless a task failed first.
The first scope's task takes 100 milliseconds, and the second's would take three seconds.
Line 13 prints the first scope's value, and the `match` on lines 18 to 25 prints a line for each way the second can end.
For a deadline, `f.task` names the scope, by its handle `s`, not a task.
Press Run.

The first scope finishes in time, so line 13 prints `Ok` with the text its task gave back.
The second is cut off at 500 milliseconds, so line 21 prints `s ran out of time`.

### Step 2: shield (fix)

`save` on line 3 prints `saving`, sleeps 200 milliseconds on line 5, standing in for the saving, then prints `saved` and `after saving`.
Line 11's scope has a deadline of 100 milliseconds, and line 14 prints whether its value is an `Err`.
Press Run.

`saving` prints, then the deadline cancels `save` in its sleep on line 5, so `saved` never prints.
The scope ran out of time, so its value is an `Err`, and line 14 prints `true`.
`shield within 500 { … }` holds cancellation off for its block, for at most 500 milliseconds, so that work which shouldn't stop halfway can finish.
The cancellation that was held off applies after the block, so `after saving` still won't print.
Put lines 5 and 6 inside `shield within 500 {` and a closing `}`, and run again, or press Solve.

## 12.4 Sendable

### Step 1: What crosses to a task (read)

A spawned call's arguments are worked out first, by the caller, and the task gets copies of them, as any function call does.
Line 12 starts `ship` with `order`.
`ship` can't change its parameter, so line 4 copies it into `copy`, and line 5 changes that.
Line 15 prints what the task gave back, and line 16 prints `order.qty` afterwards.
Press Run.

The first line is the scope's value, `Ok` with the text `ship` gave back, where its copy is down to 2.
The second is `3`: `ship` changed only its copy, and `order.qty` is still `3`.
Numbers and strings are `Sendable`, which means they can cross to a task this way, and so are arrays, structs and enums made of them.
So is a `Console`, which is why tasks have been given `console`.
A `Ref` isn't: passing one to a task is E0475.

### Step 2: Sharing through a task (fix)

Copies of a `Ref` share one box.
`bump` on line 1 adds 1 to the number in a box, lines 8 and 9 hand the same box to two tasks, and line 11 prints the number afterwards.
Press Run.

The program doesn't run.
A `Ref` isn't `Sendable`: two tasks would share its box, and a `Ref` belongs to one task.
So each line that passes `count` to a task is an E0475, on lines 8 and 9.
The help names two ways to share a changing value between tasks, an actor or copies sent through a channel, and both come later in this chapter.
This fix needs neither: each task can give back its answer, and the scope can add them up.
Make line 11 `console.println(r.debug());`.
Replace lines 8 and 9 with `let a = s.spawn(bump(count));`, `let b = s.spawn(bump(count));` and `a.join().unwrap() + b.join().unwrap()`.
Make line 6 `let count = 0;`.
Replace lines 1 to 3 with `fun bump(n: i64): i64 = n + 1;`.
Or press Solve.

> **Error note (E0475):** `count` is a `Ref`, and both tasks would get the same box, so they could change it at the same time. A `Ref` stays with one task, so it can't be passed to `s.spawn`.

## 12.5 Channels

### Step 1: Channels (read)

A channel carries values from one task to another, in order.
`Chan<i64>.new(4)` on line 9 makes one that holds up to four `i64`s, and gives its two ends: a `Sender<i64>`, `tx`, and a `Receiver<i64>`, `rx`.
`produce` on line 1 sends three squares with `out.send`, and closes the channel on line 5 when it's done.
`rx.recv()` on lines 12 to 15 waits for the next value and gives `Some(v)`, or `None` once the channel is closed and empty.
Press Run.

The first three lines are the squares, each in `Some`, in the order `produce` sent them.
The fourth `recv` gives `None`: three values came, then the close.
The last line is the scope's value, `Ok(())`.
Here the channel never fills; when one is full, `send` waits for room.
A channel made with `Chan<i64>.new(0)` holds no values, so each `send` waits until a receiver takes the value.

### Step 2: Closing a channel (fix)

`for v of rx` on line 12 receives every value until the channel is closed and empty, and line 13 adds them up.
This `produce` sends five squares and doesn't close the channel.
A channel stays open until a sender closes it, even after `produce` returns.
Press Run.

`55` never prints.
After the fifth value, `main` waits for another, but `produce` has finished and nothing will send again.
That's a deadlock, a wait that can never end, and the program stops with a panic on standard error: `panic: deadlock: every green thread is waiting`, a green thread being one of the program's tasks, `main` included.
The line under it names who waits and where: `main`, to receive on the channel made at line 8, column 20.
The panic ends the program with exit code 101.
Once the channel is closed, the loop ends after the last value.
Add `out.close();` after line 4, at the end of `produce`, and run again, or press Solve.

### Step 3: Each end its own job (fix)

Line 2 makes a channel and its two ends, `tx` and `rx`, and line 3 sends through `rx`.
Press Run.

The program doesn't run.
E0415 says there's "no method `send` on `Receiver<string>`", on line 3, and its help says why: only a `Sender` can `send`, and `rx` is the `Receiver` end.
Each end has only its own methods, so a function given a `Receiver` can only receive, and one given a `Sender` can only send and close.
Change `rx.send` to `tx.send` on line 3 and run again, or press Solve.

> **Error note (E0415):** `rx` is the `Receiver` end of the channel, and a `Receiver` has no `send` method: only the `Sender` end, `tx`, can send.

### Step 4: try_send and try_recv (read)

`try_send` and `try_recv` never wait: they say what happened instead.
`try_send` gives `.Sent`, `.Full(v)` when there's no room, or `.Closed(v)` when the channel is closed, the last two giving `v` back.
`try_recv` gives `.Ready(v)`, `.Empty` when nothing has come, or `.Closed` when the channel is closed and empty.
The channel on line 2 holds one value, and lines 3 to 9 try each case, closing it on line 7.
Press Run.

`Sent` comes from line 3, since the channel had room for `1`.
`Full(2)` comes from line 4: `1` still fills the channel, so `2` comes back.
Line 5 gives `Ready(1)`, and line 6 gives `Empty`, since nothing else was sent.
After line 7 closes the channel, line 8's `try_send` gives `Closed(3)`, and line 9's `try_recv` gives `Closed`.

## 12.6 select

### Step 1: select (read)

With two channels, a `recv` on one would wait there while the other already has a value.
`select` on line 18 waits on both and takes whichever is ready first.
Each arm names a channel operation, then `=>` and what to do, as a `match` arm does.
On line 19, `f` is the `Option` that `fruit.recv()` gave, in scope only in that arm.
`send_late` on line 3 waits `first` milliseconds, then sends a word every 200, so `apple` comes at 100, `saw` at 200, `pear` at 300 and `drill` at 400.
Press Run.

Each pass of the loop takes the word that's ready, so the four words print in the order they were sent, and the last line is the scope's `Ok(())`.
When both channels have a value ready at once, `select` picks one of them, so a program shouldn't depend on which; the sleeps here keep the words apart.

### Step 2: Timeouts with after (read)

The `select` in step 1 waits as long as it takes, and an `after` arm puts a limit on that.
Here `slow` sleeps for half a second before it sends.
`after(200)` on line 19 runs if no other arm could go on within 200 milliseconds.
Each pass of the loop is a new `select`, so the 200 milliseconds start again, and the loop either gets the message or prints `still waiting`.
Press Run.

Two waits of 200 milliseconds end before the message arrives, so `still waiting` prints twice.
The third pass gets `done`, and line 17 ends the loop.
The last line is the scope's `Ok(())`.

### Step 3: select with default (read)

An `after` arm still waits up to its limit.
A `default` arm runs when no other arm can go on at once, so a `select` with one never waits.
Arms can send too: `tx.send(i)` on line 5 goes on when the channel has room.
Press Run.

The channel holds one value, so the first send goes through and prints `queued 1`.
Nothing receives in the loop, so the channel stays full, and the next two sends fall to `default` on line 6, which prints `full, dropped 2` and `full, dropped 3`.
Line 9 then receives the one value that went through, `Some(1)`.

### Step 4: Deadlock (fix)

This program waits on plain `recv`s, which can wait forever, as a `select` without `after` or `default` can.
`ping` on line 1 waits for a message, then sends one to `pong`, and `pong` on line 7 does the same the other way round.
Press Run.

Only the panic prints.
Each waits for the other first, so neither goes on, and when every task is waiting, the program panics with a deadlock, on standard error.
The report under it names each waiting task and where the channel it waits on was made: `pong` on the channel from line 15, and `ping` on the one from line 14.
The panic ends the program with exit code 101.
Something has to send first: after line 15, add `to_ping.send("start");` and run again, or press Solve.

## 12.7 Actors

### Step 1: Actor declaration (read)

An actor is a task that keeps its own state, and other tasks reach it only by calling its methods.
`actor Counter` on line 1 declares the state, the field `count` on line 2, and the methods, as a struct and its `impl` would together.
Inside the methods `self` is the state, and `add` takes `mut self`, so line 5 can change `count`.
Line 13 starts the actor in the scope with the state's first value, as a task is started, and gives back a handle, `c`.
Lines 14 to 16 call the actor's methods through `c`, and the scope stops the actor once its body is done.
Press Run.

`5` comes from line 16: the actor added 2 and 3 to its `count`, which started at 0.
The last line is the scope's value, `Ok(())`.

### Step 2: Starting an actor (read)

An actor starts in a scope, as a task does: `main` takes the root scope on line 11, and line 12 starts a `Counter` in it with `root.spawn`.
Line 13 copies the handle into `d`, and line 14 sends `add(5)` through the copy.
Press Run.

The output panel shows `15`: copies of a handle reach the same actor, so `d.add(5)` shows up in `c.get()` on line 15.

### Step 3: Messages as method calls (read)

Calling a method on a handle sends the actor a message, and the actor handles its messages one at a time, in the order they came.
`log` on line 6 returns nothing and takes 300 milliseconds, so `l.log(...)` on lines 18 and 19 is sent and `main` goes on at once, without waiting for it to be handled.
`all` on line 11 returns a value, so line 21 waits for the answer.
Line 17 reads the clock, and lines 20 and 22 check how long `main` has waited at each point.
Press Run.

Line 20 prints `true`: the two `log` calls took `main` less than 300 milliseconds, so it didn't wait for them.
By the time `all` is handled, both messages to `log` before it have been, so line 21 prints both lines.
Line 22 prints `true` too: `main` waited at least the 600 milliseconds the two `log` messages took.
The last line is the scope's value, `Ok(())`.

### Step 4: Stopping an actor (read)

An actor runs until it's stopped, and its scope stops it once the scope's body is done, which is how the actors in steps 1 and 3 ended without a `stop`.
`a.stop()` on line 11 stops it sooner, after the messages already sent; an actor has no `join`.
Line 10 calls `show` before the stop, and line 12 calls it on the stopped actor.
Line 8 keeps the scope's value in `ok`, though this time it turns out to be an `Err`.
Press Run.

`5` comes from line 10.
A call to a stopped actor panics where it's made, here in the scope's body, so line 12 prints nothing.
A panic in the body fails the scope too, so line 14 prints an `Err` with a `Failure`.
Its `task` is the scope, `s`, and its `kind` is a `Panic` with the message "actor `Divider` has stopped", then where the call was made, line 12.

### Step 5: Actor fields (fix)

`Tally` on line 1 keeps its total in a `Ref` box, declared on line 2.
`add` on line 4 takes plain `self` and changes the number in the box, and line 13 starts the actor with `Ref.new(0)`.
Press Run.

The program doesn't run.
An actor's fields, and its methods' parameters and results, must be `Sendable`, and a `Ref` isn't.
So E0475 points at the field's type on line 2: `Tally` "can't hold or exchange a `Ref<i64>`".
The help's first way is already followed: the state is in an actor, and only the box has to go.
An actor's own methods can change its fields with `mut self`, as `add` did in step 1, so the box isn't needed.
Make line 13's `Ref.new(0)` a plain `0`.
Make line 8 `fun get(self): i64 = self.total;`.
Make line 5 `self.total += n;` and line 4 `fun add(mut self, n: i64) {`.
Make line 2 `total: i64,`.
Or press Solve.
