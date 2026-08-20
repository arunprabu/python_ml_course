# =============================================================
# SECTION 4: Introduction to NumPy
# =============================================================

print("\n--- NumPy Introduction ---")

try:
    import numpy as np  # uv add numpy (or) pip install numpy

    # NumPy array — like a typed, fast list for numbers
    scores = np.array([85, 92, 78, 90, 65, 88, 72, 95])

    # Prints space-separated, NO commas: commas = list, no commas = array.
    print(f"NumPy array:   {scores}")

    # <class 'numpy.ndarray'> — not a list, so no .append/.extend; size is fixed.
    print(f"Type:          {type(scores)}")

    # (8,) — .shape is always a tuple, one entry per dimension: 1-D with 8 items.
    # The trailing comma is single-element-tuple syntax, not a typo.
    print(f"Shape:         {scores.shape}")

    # int64 — one element type for the whole array (int32 on Windows).
    # Mixing types upcasts (floats) or falls back to strings; floats into an
    # int array are truncated silently.
    print(f"dtype:         {scores.dtype}")

    # # Element-wise operations — no loop needed!
    print(f"\nAdd 5 to all:  {scores + 5}")
    # print(f"Double all:    {scores * 2}")
    # print(f"Above 80:      {scores[scores > 80]}")  # boolean indexing

    # Statistical operations
    print(f"\nMean:    {np.mean(scores):.2f}")
    print(f"Std Dev: {np.std(scores):.2f}")
    print(f"Min:     {np.min(scores)}")
    print(f"Max:     {np.max(scores)}")
    print(f"Median:  {np.median(scores)}")

    # 2D array — like a matrix / spreadsheet
    marks_matrix = np.array(
        [
            [85, 92, 78, 90],  # Alice
            [72, 68, 75, 80],  # Bob
            [95, 88, 92, 91],  # Charlie
        ]
    )
    # The leading \n matters: a 2-D array prints across several lines, so print
    # it on its own line to keep the rows aligned.
    print(f"\n2D marks matrix:\n{marks_matrix}")

    # (3, 4) — 2 dimensions, outermost first: 3 rows then 4 columns. Inner lists
    # must be equal length or NumPy raises ValueError.
    print(f"Shape: {marks_matrix.shape}")

    # ---- axis: the one idea people get backwards --------------------------------
    # axis names the dimension that gets COLLAPSED, not the one you want an answer
    # for — the axis you name is the axis you lose:
    #   axis=1  removes the 4  ->  (3, 4) becomes (3,)  ->  one number per ROW    -> per student
    #   axis=0  removes the 3  ->  (3, 4) becomes (4,)  ->  one number per COLUMN -> per subject
    #   (none)  removes both   ->  (3, 4) becomes ()    ->  one scalar, mean of all 12 = 83.83
    # .round(2) rounds every element of the result array in one call (it rounds
    # the stored float, it does not format text — 84.0 still displays as "84.").

    # Alice (85+92+78+90)/4=86.25, Bob 73.75, Charlie 91.5
    print(f"Row averages (per student): {marks_matrix.mean(axis=1).round(2)}")

    # Subject 1 (85+72+95)/3=84.0, then 82.67, 81.67, 87.0
    print(f"Col averages (per subject): {marks_matrix.mean(axis=0).round(2)}")

except ImportError:
    print("NumPy not installed. Run: uv add numpy")
