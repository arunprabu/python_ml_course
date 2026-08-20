# Why Do We Use NumPy?

**NumPy (Numerical Python)** is a Python library used for working with numbers, arrays, and mathematical calculations efficiently.

Python already has lists, but NumPy provides **arrays** that are faster and more convenient when working with large amounts of numerical data.

> Runnable example for this note: [`ex25_numpy.py`](ex25_numpy.py)

## Why NumPy?

- **Fast calculations** — NumPy operations are much faster than manually looping through Python lists.
- **Arrays** — Easily work with one-dimensional and multi-dimensional arrays.
- **Mathematical operations** — Perform calculations on entire arrays without writing loops.
- **Statistical functions** — Easily calculate mean, median, standard deviation, variance, etc.
- **Data manipulation** — Filter, reshape, sort, combine, and transform numerical data.
- **Foundation for Data Science** — Libraries such as Pandas, SciPy, scikit-learn, and many machine learning tools rely heavily on NumPy.

### Simple Example

Without NumPy:

```python
scores = [85, 92, 78, 90]

total = sum(scores)
average = total / len(scores)

print(average)
```

With NumPy:

```python
import numpy as np

scores = np.array([85, 92, 78, 90])

print(np.mean(scores))
```

---

## What Actually Makes It Faster?

This is worth understanding once, because it explains every other rule in this note.

A Python **list** of 8 numbers does not store 8 numbers. It stores 8 *pointers* to 8 separate integer objects scattered around memory. Each object carries its own type information and reference count. To add 5 to every element, Python must follow each pointer, check the type, unbox the value, add, and build a new object — 8 times.

A NumPy **array** stores the 8 values as raw 64-bit integers in **one continuous block of memory**. NumPy hands that whole block to a compiled C loop, which walks straight through it with no type checks and no object creation.

```text
Python list:   [ptr] [ptr] [ptr] [ptr]  ->  scattered int objects, each boxed
NumPy array:   [85][92][78][90]         ->  one contiguous block of int64
```

Two consequences follow from this, and they are the source of most beginner surprises:

1. **Every element must share one type** (the `dtype`) — that is what makes the block uniform.
2. **The array has a fixed size** — there is no `.append()`, because growing it means allocating a new block.

## Creating Arrays

```python
np.array([85, 92, 78])        # from a Python list
np.zeros(3)                   # [0. 0. 0.]      — note: floats by default
np.ones(3)                    # [1. 1. 1.]
np.arange(0, 10, 3)           # [0 3 6 9]       — like range(), but an array
np.linspace(0, 1, 5)          # [0. 0.25 0.5 0.75 1.] — 5 evenly spaced points
np.arange(6).reshape(2, 3)    # [[0 1 2], [3 4 5]] — same data, new shape
```

## The Four Attributes to Check

```python
scores = np.array([85, 92, 78, 90, 65, 88, 72, 95])

scores.shape    # (8,)     tuple — one entry per dimension
scores.ndim     # 1        number of dimensions = len(shape)
scores.size     # 8        total number of elements
scores.dtype    # int64    the ONE type shared by every element
```

`shape` is **always a tuple**. `(8,)` has a trailing comma because that is Python's syntax for a one-element tuple — `(8)` would just be the number `8`. Not a typo.

### dtype Traps

`dtype` is inferred once, at creation, from everything you passed in. Because all elements must agree, one odd value silently changes the whole array:

| You write | You get | Why it matters |
| --- | --- | --- |
| `np.array([85, 92, 78])` | `int64` | whole numbers |
| `np.array([85, 92.5, 78])` | `float64` | one float **upcasts everything** |
| `np.array([85, "A+", 78])` | `<U21` (text) | maths now fails — and nothing warned you |

There is one more, and it catches people in marks-processing code:

```python
scores = np.array([85, 92, 78])   # dtype is int64
scores[0] = 90.7                  # stored as 90 — the .7 is truncated, no warning
```

The array cannot hold a float, so the value is silently cut down to fit. If you need decimals, create the array as floats from the start: `np.array([85, 92, 78], dtype=float)`.

## Vectorised Operations — No Loops

An operation applied to an array is applied to **every element**:

```python
scores + 5        # [ 90  97  83  95  70  93  77 100]
scores * 2        # [170 184 156 180 130 176 144 190]
scores > 80       # [True True False True False True False True]
```

Note the last one: comparing an array does **not** give a single `True`/`False`. It gives a **boolean array** of the same shape — one answer per element. That array is then useful on its own:

```python
scores[scores > 80]       # [85 92 90 88 95]   — keep only matching elements
(scores > 80).sum()       # 5                  — True counts as 1, so sum = a count
```

This is called **boolean indexing** (or masking), and it replaces the usual `for` + `if` + `append` pattern entirely. Pandas uses exactly the same idea for filtering table rows.

## Statistics

```python
scores.mean()      # 83.12    (or np.mean(scores) — same thing)
scores.std()       # 9.83
np.median(scores)  # 86.5
scores.min(), scores.max(), scores.sum()
```

> **Careful:** `np.std()` computes the **population** standard deviation (divides by `n`). Pandas' `.std()` defaults to the **sample** version (divides by `n-1`). The same marks give 18.21 in NumPy and 20.36 in Pandas — the libraries disagree by convention, not by error. Use `np.std(x, ddof=1)` to match Pandas.

## 2-D Arrays and the `axis` Argument

A 2-D array is a matrix — rows and columns, like a spreadsheet:

```python
marks_matrix = np.array([
    [85, 92, 78, 90],   # Alice
    [72, 68, 75, 80],   # Bob
    [95, 88, 92, 91],   # Charlie
])

marks_matrix.shape   # (3, 4) — 3 rows, 4 columns; outermost dimension first
marks_matrix.ndim    # 2
```

Indexing takes one position per dimension:

```python
marks_matrix[0]      # [85 92 78 90]  — row 0, all of Alice's marks
marks_matrix[1, 2]   # 75             — row 1, column 2
marks_matrix[:, 1]   # [92 68 88]     — ALL rows, column 1 (one subject)
```

### The rule people get backwards

`axis` does **not** mean "the direction I want an answer for". It names the dimension that gets **collapsed** — consumed by the operation and then **removed from the shape**.

Read the axis numbers straight off `.shape`, which is `(3, 4)`:

| Call | Collapses | Shape change | Meaning |
| --- | --- | --- | --- |
| `.mean(axis=1)` | the `4` columns | `(3, 4)` → `(3,)` | one number per **row** → per student |
| `.mean(axis=0)` | the `3` rows | `(3, 4)` → `(4,)` | one number per **column** → per subject |
| `.mean()` | both | `(3, 4)` → `()` | a single scalar over all 12 values |

```python
marks_matrix.mean(axis=1).round(2)   # [86.25 73.75 91.5]   per student
marks_matrix.mean(axis=0).round(2)   # [84. 82.67 81.67 87.] per subject
marks_matrix.mean().round(2)         # 83.83                 everything
```

**Shortcut to remember: the axis you name is the axis you lose.**

**Sanity check when unsure:** the length of the answer equals the dimension you *kept*. Three students out, so that was `axis=1`.

The same rule applies to `.sum()`, `.max()`, `.min()`, `.std()` — and to Pandas, where `axis=1` again means "across the columns, one result per row".

### About `.round(2)`

`.round(2)` rounds **every element** of the result in one call, which is why no per-value `f"{x:.2f}"` formatting is needed. But it rounds the stored *number*, it does not format *text*:

- `84.0` still prints as `84.` (a float whose decimals are zero)
- NumPy pads with spaces to keep columns aligned: `[84.   82.67 81.67 87.  ]`
- Binary floats are approximate, so treat it as display-rounding, not an exact guarantee

## Two More Gotchas

**Ragged lists are an error.** Every inner list must be the same length, or there is no rectangle to build:

```python
np.array([[1, 2], [3]])
# ValueError: setting an array element with a sequence.
#             The requested array has an inhomogeneous shape...
```

**Slices are views, not copies.** A slice shares memory with the original, so writing to it changes the original:

```python
a = np.array([1, 2, 3, 4])
b = a[:2]
b[0] = 99
print(a)          # [99  2  3  4]   <- a changed too!

c = a[:2].copy()  # use .copy() when you want an independent array
```

This is deliberate — it is what makes slicing large arrays free. Just be aware of it. (Boolean indexing, by contrast, always returns a copy.)

## Quick Reference

| Task | Code |
| --- | --- |
| Create from list | `np.array([1, 2, 3])` |
| Dimensions / size / type | `a.shape`, `a.ndim`, `a.size`, `a.dtype` |
| Maths on all elements | `a + 5`, `a * 2`, `a ** 2` |
| Filter | `a[a > 80]` |
| Count matches | `(a > 80).sum()` |
| Statistics | `a.mean()`, `a.std()`, `np.median(a)`, `a.min()`, `a.max()` |
| Per row (2-D) | `a.mean(axis=1)` |
| Per column (2-D) | `a.mean(axis=0)` |
| Change shape | `a.reshape(2, 3)` |
| Independent copy | `a.copy()` |

### Simple way to remember

**NumPy → one type, one memory block, no loops.**

Everything else — the speed, the `dtype` rules, the missing `.append()` — follows from that.
