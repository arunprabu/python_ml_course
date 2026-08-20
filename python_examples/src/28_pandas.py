# =============================================================
# SECTION 5: Introduction to Pandas
# =============================================================

print("\n--- Pandas Introduction ---")

try:
    import pandas as pd  # uv add pandas (or) pip install pandas

    # DataFrame — like a spreadsheet / SQL table
    #
    # Built here from a dict of lists: each KEY becomes a column name and each
    # LIST becomes that column's values. Every list must be the same length (5),
    # since they are the rows of one rectangular table — a short list raises
    # ValueError ("All arrays must be of the same length").
    #
    # Mental model: a DataFrame is a dict of Series that share one index.
    # A NumPy 2-D array is one block of ONE dtype; a DataFrame is column-wise, so
    # each column keeps its own dtype — that is how text and numbers coexist below.
    data = {
        "name": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
        "department": ["CS", "IT", "CS", "EC", "CS"],
        "math": [88, 72, 95, 60, 45],
        "python": [95, 78, 97, 55, 52],
        "dbms": [82, 68, 89, 70, 48],
    }
    df = pd.DataFrame(data)

    # The leftmost 0,1,2,3,4 column in the output is the INDEX — the row labels.
    # It is NOT a data column: it is not in df.columns and not counted in df.shape.
    # We never supplied one, so pandas auto-created a RangeIndex(0..4).
    print(f"DataFrame:\n{df}\n")

    # (5, 5) — same (rows, columns) convention as NumPy's .shape.
    # Here the match is a coincidence: 5 students and 5 columns.
    print(f"Shape: {df.shape}   (rows, columns)")

    # df.columns is a pandas Index object, not a list — list() converts it so it
    # prints as ['name', 'department', ...] instead of Index([...], dtype='str').
    print(f"Columns: {list(df.columns)}")

    # Basic exploration
    #
    # DOUBLE brackets are the thing to slow down on:
    #   df["math"]              -> one Series  (1-D, a single column)
    #   df[["math", "python"]]  -> a DataFrame (2-D, a list of columns)
    # The inner [ ] is just a Python list of column names, so the outer [ ] is
    # being handed one object. Selecting the 3 numeric columns keeps "name" and
    # "department" out of the stats.
    #
    # .describe() returns a summary table: count, mean, std, min, 25%, 50% (median),
    # 75%, max — one column per input column. It only summarises numeric columns.
    # NOTE: std here is the SAMPLE std (divides by n-1), so math shows 20.36 —
    # np.std() defaults to the POPULATION std (divides by n) and would say 18.21.
    # Same data, different convention; expect the two libraries to disagree.
    print(f"\nDescriptive stats:\n{df[['math', 'python', 'dbms']].describe().round(2)}")

    # Adding a computed column
    #
    # axis=1 works exactly as in NumPy: it collapses the COLUMNS, leaving one
    # number per row — each student's average across their 3 subjects.
    # (axis=0 would instead give one number per subject, averaged over students.)
    # Assigning to df["average"] creates a brand-new column, matched up by index.
    df["average"] = df[["math", "python", "dbms"]].mean(axis=1).round(2)

    # .apply() runs a plain Python function once per value in the Series.
    # It is the escape hatch for logic NumPy cannot vectorise (here: an if/else
    # producing text). Convenient, but it is a real Python loop underneath —
    # far slower than df["average"] >= 60 on large data, so prefer vectorised
    # operations when one exists and keep .apply() for genuinely custom logic.
    df["status"] = df["average"].apply(lambda avg: "PASS" if avg >= 60 else "FAIL")
    print(f"\nWith average and status:\n{df}")

    # Filtering rows — like SQL WHERE
    #
    # Two steps happening in one line:
    #   1. df["department"] == "CS"  -> a boolean Series [True, False, True, False, True]
    #      (the comparison is element-wise — it does NOT return a single True/False)
    #   2. df[<that boolean Series>] -> keeps only the rows where the value is True
    # This is called boolean masking, the same idea as scores[scores > 80] in NumPy.
    #
    # Watch the index in the output: rows keep their ORIGINAL labels 0, 2, 4 — they
    # are not renumbered. That is the point of an index; use .reset_index(drop=True)
    # if you actually want a fresh 0,1,2.
    cs_students = df[df["department"] == "CS"]
    print(f"\nCS students only:\n{cs_students}")

    # Same pattern, filtering on the computed column. Then [['name', ...]] selects
    # 3 columns of the filtered result — filter rows, then pick columns.
    passing = df[df["status"] == "PASS"]
    print(f"\nPassing students:\n{passing[['name', 'average', 'status']]}")

    # Grouping — like SQL GROUP BY
    #
    # Read it as three steps (split -> apply -> combine):
    #   .groupby("department")  splits the 5 rows into buckets: CS, EC, IT
    #   ["average"]             picks the column to aggregate within each bucket
    #   .mean()                 collapses each bucket to ONE number
    # Result is a Series indexed BY department (not 0,1,2), sorted alphabetically —
    # the grouping key became the index, which is why the output has a
    # "department" label above it and "Name: average" below it.
    dept_avg = df.groupby("department")["average"].mean().round(2)
    print(f"\nAverage by department:\n{dept_avg}")

    # Reading a CSV directly into a DataFrame
    #
    # One line replaces the whole open()/csv.DictReader/append loop from ex22, and
    # read_csv also INFERS a dtype per column: the marks arrive as int64 ready for
    # maths, not as the strings the csv module would hand back.
    # The path is relative to the folder you RUN python from (not to this file), so
    # run this from training_examples/. Needs data/students.csv with the columns
    # used below: student_id, name, department, marks_math, marks_python,
    # marks_dbms, marks_networks.
    print("\n--- Reading CSV into DataFrame ---")
    students_df = pd.read_csv("data/students.csv")

    # len(df) counts ROWS (a DataFrame iterates row-wise); len(df.columns) counts columns.
    print(f"Loaded {len(students_df)} rows, {len(students_df.columns)} columns")

    # .head(3) shows the first 3 rows — the standard "did this load correctly?" check
    # before touching a file you have not seen. .tail(3) does the same from the end.
    # If the table is wide, pandas hides middle columns as "..." rather than wrapping.
    print(f"\nFirst 3 rows:\n{students_df.head(3)}")

    # Compute average across all mark columns
    #
    # Naming the columns in a list keeps student_id out of the maths — an id is a
    # number to Python but averaging it is meaningless. Always select mark columns
    # explicitly instead of averaging "everything numeric".
    mark_cols = ["marks_math", "marks_python", "marks_dbms", "marks_networks"]
    students_df["average"] = students_df[mark_cols].mean(axis=1).round(2)

    # Chained ternary = if/elif/elif/else in one expression, read left to right and
    # STOPPING at the first true test. Order matters: the >= 85 test must come first,
    # because 90 satisfies >= 70 and >= 60 too and would otherwise be graded "B".
    students_df["grade"] = students_df["average"].apply(
        lambda x: "A" if x >= 85 else "B" if x >= 70 else "C" if x >= 60 else "F"
    )
    print(
        f"\nWith average and grade:\n{students_df[['name', 'department', 'average', 'grade']]}"
    )

    # Save result to CSV
    #
    # Selecting the 5 columns worth keeping — a report, not the full working table.
    output = students_df[["student_id", "name", "department", "average", "grade"]]

    # index=False is the important argument: by default pandas writes the index as a
    # nameless first column, so re-reading that file gives you a junk "Unnamed: 0"
    # column. Use index=False whenever the index is just auto-numbering.
    # NOTE: the data/output/ folder must already exist — to_csv will not create it.
    output.to_csv("data/output/pandas_results.csv", index=False)
    print("\nResults saved to data/output/pandas_results.csv")

except ImportError:
    print("Pandas not installed. Run: uv add pandas")
