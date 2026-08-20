# Why Do We Use Pandas?

**Pandas** is a Python library used for working with **structured data**, such as tables, spreadsheets, and CSV files.

While NumPy is mainly designed for numerical arrays and mathematical calculations, Pandas makes it easier to work with data that has **rows, columns, and labels**.

> Runnable example for this note: [`ex26_pandas.py`](ex26_pandas.py) — and read [`NUMPY.md`](NUMPY.md) first, since Pandas is built on NumPy.

## Why Pandas?

- **Tabular data** — Work with data in rows and columns, similar to Excel.
- **Named columns** — Columns can have meaningful names like `Name`, `Age`, and `Salary`.
- **Read files easily** — Load data from CSV, Excel, JSON, SQL databases, etc.
- **Filter data** — Find rows that match specific conditions.
- **Handle missing data** — Detect, remove, or replace missing values.
- **Data analysis** — Calculate mean, sum, count, minimum, maximum, and other statistics.
- **Data cleaning** — Rename columns, remove duplicates, change data types, and transform data.

## Pandas DataFrame

The most commonly used object in Pandas is a **DataFrame**.

A DataFrame is similar to a table:

| Name    | Math | English | Science |
| ------- | ---: | ------: | ------: |
| Alice   |   85 |      92 |      78 |
| Bob     |   72 |      68 |      75 |
| Charlie |   95 |      88 |      92 |

We can create the same table using Pandas:

```python
import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Math": [85, 72, 95],
    "English": [92, 68, 88],
    "Science": [78, 75, 92]
}

df = pd.DataFrame(data)

print(df)
```

Output:

```text
      Name  Math  English  Science
0    Alice    85       92       78
1      Bob    72       68       75
2  Charlie    95       88       92
```

---

## The Two Objects: Series and DataFrame

Everything in Pandas is one of two things:

- **Series** — a single column. One-dimensional, with labels.
- **DataFrame** — a whole table. A **dict of Series that all share one index**.

That last sentence explains a lot. Because a DataFrame is column-wise (not one flat block like a NumPy array), **each column keeps its own dtype** — which is how text and numbers sit side by side in one table:

```python
df.dtypes
# name            str
# department      str
# math          int64
# python        int64
```

A NumPy 2-D array could not do this; it would force everything to become text.

### The Index Is Not a Column

In the output above, that leftmost `0 1 2` column is the **index** — the row labels. It is easy to mistake for data, so be clear:

- it is **not** in `df.columns`
- it is **not** counted in `df.shape`
- we never created it — Pandas auto-generated a `RangeIndex`

The index is what makes Pandas more than a spreadsheet: operations *align on it*. It comes back later when filtering and grouping.

## Creating a DataFrame

The dict-of-lists form is the most common: each **key** becomes a column name, each **list** becomes that column's values.

```python
df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie"],
    "math": [88, 72, 95],
})
```

Every list must be the same length — they are the rows of one rectangular table:

```python
pd.DataFrame({"a": [1, 2, 3], "b": [1, 2]})
# ValueError: All arrays must be of the same length
```

## Inspecting Data

Run these *before* trusting any file you did not create yourself:

```python
df.head(3)      # first 3 rows — the standard "did this load correctly?" check
df.tail(3)      # last 3 rows
df.shape        # (5, 5) — (rows, columns), same convention as NumPy
list(df.columns)  # ['name', 'department', 'math', ...]
df.dtypes       # the type of each column
df.info()       # dtypes + non-null counts + memory, all at once
df.describe()   # count, mean, std, min, 25%, 50%, 75%, max
```

`df.columns` is a pandas `Index` object, not a list — wrap it in `list()` when you just want to print names cleanly.

`describe()` only summarises **numeric** columns, so text columns are skipped automatically.

> **Careful:** the `std` in `describe()` is the **sample** standard deviation (divides by `n-1`). NumPy's `np.std()` uses the **population** version (divides by `n`). The same marks give 20.36 in Pandas and 18.21 in NumPy. Neither is wrong — they are different conventions.

## Selecting Columns — Single vs Double Brackets

This is the single most common beginner confusion:

```python
df["math"]              # a Series   (1-D — one column)
df[["math", "python"]]  # a DataFrame (2-D — a list of columns)
```

The inner `[ ]` is just an ordinary Python **list of column names**, so the outer `[ ]` is still being handed one object. Use double brackets whenever you want a table back — including for a single column: `df[["math"]]`.

### `.loc` and `.iloc`

```python
df.loc[0, "name"]              # 'Alice'  — by LABEL (index label, column name)
df.iloc[0, 0]                  # 'Alice'  — by INTEGER position
df.loc[df["math"] > 80, "name"]  # ['Alice', 'Charlie'] — condition + column together
```

Remember: **l**oc = **l**abel, **i**loc = **i**nteger.

## Filtering Rows — Like SQL `WHERE`

```python
cs_students = df[df["department"] == "CS"]
```

Two separate steps are happening on that line:

1. `df["department"] == "CS"` produces a **boolean Series**: `[True, False, True, False, True]`. The comparison is element-wise — it does **not** return a single `True`/`False`.
2. `df[<boolean Series>]` keeps only the rows where the value is `True`.

This is **boolean masking** — exactly the same idea as `scores[scores > 80]` in NumPy.

Combine conditions with `&` (and) / `|` (or), and **wrap each condition in brackets** — `&` binds tighter than `==` in Python:

```python
df[(df["department"] == "CS") & (df["math"] > 80)]
```

Use `&` and `|`, not the words `and`/`or` — those work on single values and raise `ValueError` on a Series.

### The Index Survives Filtering

```text
      name department  math
0    Alice         CS    88
2  Charlie         CS    95
4      Eve         CS    45
```

The rows kept their **original labels 0, 2, 4** — they are not renumbered. That is the index doing its job. If you want a fresh `0,1,2`, ask for it:

```python
cs_students = cs_students.reset_index(drop=True)
```

(`drop=True` throws the old index away instead of storing it as a new column.)

## Adding Computed Columns

```python
df["average"] = df[["math", "python", "dbms"]].mean(axis=1).round(2)
```

`axis=1` behaves **exactly as in NumPy**: it collapses the columns, leaving one number per row — each student's average. (`axis=0` would give one number per subject instead.) Assigning to `df["average"]` creates the column, matched up by index.

### `.apply()` — The Escape Hatch

```python
df["status"] = df["average"].apply(lambda avg: "PASS" if avg >= 60 else "FAIL")
```

`.apply()` runs a plain Python function once per value. It is the way out when your logic cannot be vectorised — but it is a real Python loop underneath and much slower than a vectorised expression. Prefer a built-in operation when one exists:

```python
df["status"] = df["average"].apply(lambda a: "PASS" if a >= 60 else "FAIL")  # slower
df["passed"] = df["average"] >= 60                                          # vectorised
```

**Chained ternaries** read left to right and stop at the first true test, so order matters:

```python
lambda x: "A" if x >= 85 else "B" if x >= 70 else "C" if x >= 60 else "F"
```

`>= 85` must come first — a 90 also satisfies `>= 70` and `>= 60`, and would be graded "B" if the tests were reordered.

## Grouping — Like SQL `GROUP BY`

```python
df.groupby("department")["average"].mean().round(2)
```

Read it as **split → apply → combine**:

| Step | What it does |
| --- | --- |
| `.groupby("department")` | splits the rows into buckets: CS, EC, IT |
| `["average"]` | picks the column to aggregate inside each bucket |
| `.mean()` | collapses each bucket to one number |

```text
department
CS    76.78
EC    61.67
IT    72.67
Name: average, dtype: float64
```

The result is a **Series indexed by department**, sorted alphabetically — the grouping key *became the index*. That is why "department" is printed as a heading above the values rather than as a column.

Several statistics at once:

```python
df.groupby("department")["average"].agg(["count", "mean", "max"]).round(2)
```

```text
            count   mean    max
department
CS              3  76.78  93.67
EC              1  61.67  61.67
IT              1  72.67  72.67
```

## Reading and Writing Files

```python
students_df = pd.read_csv("data/students.csv")
```

One line replaces the whole `open()` / `csv.DictReader` / append loop. `read_csv` also **infers a dtype per column**, so marks arrive as `int64` ready for maths — not as the strings the `csv` module hands back.

The path is relative to the folder you **run Python from**, not to the `.py` file.

```python
output.to_csv("data/output/pandas_results.csv", index=False)
```

`index=False` matters. By default Pandas writes the index as a nameless first column, and re-reading that file gives you a junk `Unnamed: 0` column. Use `index=False` whenever the index is just auto-numbering.

Also note: `to_csv` will **not** create missing folders — `data/output/` must already exist.

Other formats work the same way: `pd.read_excel()`, `pd.read_json()`, `pd.read_sql()`.

## Useful Everyday Operations

```python
df.sort_values("average", ascending=False)   # rank students
df["department"].value_counts()              # how many per department
df["math"].isna().sum()                      # count missing values
df.dropna()                                  # drop rows with missing values
df.fillna(0)                                 # replace missing with 0
df.drop_duplicates()
df.rename(columns={"math": "Mathematics"})
```

Most of these **return a new DataFrame** rather than editing in place — so assign the result:

```python
df = df.sort_values("average", ascending=False)   # without df = ..., nothing changes
```

## NumPy vs Pandas

| NumPy                                   | Pandas                                       |
| --------------------------------------- | -------------------------------------------- |
| Mainly works with arrays                | Mainly works with tabular data               |
| Uses numerical indexes                  | Supports named columns and indexes           |
| Excellent for mathematical calculations | Excellent for data analysis and manipulation |
| Usually contains the same type of data  | Can easily contain different data types      |
| `np.array()`                            | `pd.DataFrame()`                             |

### Simple way to remember

**NumPy → Numbers and Arrays**

**Pandas → Tables and Data Analysis**

Pandas *is* NumPy underneath — with labels bolted on. That is why `axis=1` means the same thing in both, and why boolean masking looks identical in both.

## Quick Reference

| Task | Code |
| --- | --- |
| Create | `pd.DataFrame({"col": [...]})` |
| Load CSV | `pd.read_csv("file.csv")` |
| First rows | `df.head()` |
| Size / names / types | `df.shape`, `df.columns`, `df.dtypes` |
| Summary stats | `df.describe()` |
| One column (Series) | `df["math"]` |
| Several columns (DataFrame) | `df[["math", "python"]]` |
| Filter rows | `df[df["math"] > 80]` |
| Two conditions | `df[(df["a"] > 1) & (df["b"] < 5)]` |
| New computed column | `df["avg"] = df[cols].mean(axis=1)` |
| Custom logic per value | `df["c"].apply(lambda x: ...)` |
| Group and aggregate | `df.groupby("dept")["avg"].mean()` |
| Sort | `df.sort_values("avg", ascending=False)` |
| Count categories | `df["dept"].value_counts()` |
| Save CSV | `df.to_csv("out.csv", index=False)` |
