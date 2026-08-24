# 21_pandas.py

# Comprehensive Pandas Examples

import pandas as pd
import numpy as np

print("Pandas Key Concepts Examples")

# 1. Creating Series and DataFrames

print("\n1. Creating Series and DataFrames")

# Series
s = pd.Series([1, 3, 5, 6, 8])
print("Series:", s)

# DataFrame from dict
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35], 'City': ['NYC', 'LA', 'Chicago']}
df = pd.DataFrame(data)
print("DataFrame:")
print(df)

# 2. Reading and Writing Data

print("\n2. Reading and Writing Data")

# Create sample data
df.to_csv('sample.csv', index=False)
df_read = pd.read_csv('sample.csv')
print("Read CSV:")
print(df_read)

# 3. Data Inspection

print("\n3. Data Inspection")

print("Head:")
print(df.head())

print("Info:")
print(df.info())

print("Describe:")
print(df.describe())

print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print("Index:", df.index.tolist())

# 4. Indexing and Selection

print("\n4. Indexing and Selection")

print("Column selection:")
print(df['Name'])

print("Multiple columns:")
print(df[['Name', 'Age']])

print("Row selection by label:")
print(df.loc[0])

print("Row selection by position:")
print(df.iloc[0])

print("Boolean indexing:")
print(df[df['Age'] > 25])

# 5. Data Cleaning

print("\n5. Data Cleaning")

# Add some missing data
df_dirty = df.copy()
df_dirty.loc[0, 'Age'] = np.nan
print("Data with NaN:")
print(df_dirty)

print("Drop NaN:")
print(df_dirty.dropna())

print("Fill NaN:")
print(df_dirty.fillna(0))

# 6. Data Operations

print("\n6. Data Operations")

df['Age_Double'] = df['Age'] * 2
print("Added column:")
print(df)

print("Mean age:", df['Age'].mean())

print("Value counts:")
print(df['City'].value_counts())

# 7. Grouping and Aggregation

print("\n7. Grouping and Aggregation")

# Add more data for grouping
df_extended = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 28, 32],
    'City': ['NYC', 'LA', 'Chicago', 'NYC', 'LA'],
    'Salary': [50000, 60000, 70000, 55000, 65000]
})

print("Group by City and mean:")
print(df_extended.groupby('City').mean())

# 8. Merging and Joining

print("\n8. Merging and Joining")

df1 = pd.DataFrame({'key': ['A', 'B', 'C'], 'value1': [1, 2, 3]})
df2 = pd.DataFrame({'key': ['A', 'B', 'D'], 'value2': [4, 5, 6]})

print("Merge:")
print(pd.merge(df1, df2, on='key'))

print("Concat:")
print(pd.concat([df1, df2]))

# 9. Time Series

print("\n9. Time Series")

dates = pd.date_range('2023-01-01', periods=5, freq='D')
ts = pd.Series(np.random.randn(5), index=dates)
print("Time Series:")
print(ts)

print("Resample monthly:")
print(ts.resample('M').mean())

# 10. Visualization

print("\n10. Visualization")

# Basic plot (would show in notebook)
try:
    df_extended.plot(x='Name', y='Salary', kind='bar')
    print("Plot created")
except:
    print("Plotting not available in this environment")

# 11. Performance Tips

print("\n11. Performance Tips")

# Vectorized operations are preferred
df_large = pd.DataFrame({'A': np.random.randn(1000), 'B': np.random.randn(1000)})

import time
start = time.time()
result = df_large['A'] + df_large['B']
end = time.time()
print("Vectorized operation time:", end - start)

# Cleanup

import os
for f in ['sample.csv']:
    if os.path.exists(f):
        os.remove(f)
        print(f"Removed: {f}")

print("\nCleanup complete!")