# Pandas - Python Data Analysis Library

## What is Pandas?

Pandas is a powerful Python library for data manipulation and analysis. It provides data structures and operations for working with structured data, making it easy to clean, transform, and analyze data.

**Key Components:**

- **DataFrame**: 2-dimensional labeled data structure (like a spreadsheet or SQL table)
- **Series**: 1-dimensional labeled array (like a column in a DataFrame)
- **Index**: Immutable sequence used for indexing and alignment
- **Rich I/O capabilities**: Read/write data from various formats (CSV, Excel, SQL, JSON, etc.)

Pandas is built on top of NumPy and integrates seamlessly with the scientific Python ecosystem.

## Key Features

### DataFrame - The Core Data Structure

```python
import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['NYC', 'LA', 'Chicago']
})
```

### Series - 1D Data Structure

```python
# Create Series
s = pd.Series([1, 3, 5, 6, 8], name='values')
```

### Key Capabilities

- **Data alignment and integrated handling of missing data**
- **Reshaping and pivoting of data sets**
- **Label-based slicing, indexing, and subsetting**
- **Group by operations and data aggregation**
- **Merging and joining of data sets**
- **Time series functionality**
- **Hierarchical indexing**

## Key Use Cases

### 1. Data Analysis and Exploration

Pandas is the go-to tool for exploratory data analysis:

- Loading and inspecting datasets
- Data cleaning and preprocessing
- Statistical analysis
- Data visualization

### 2. Data Cleaning and Preprocessing

Handle real-world messy data:

- Missing value imputation
- Outlier detection and removal
- Data type conversions
- String operations

### 3. Data Transformation

Reshape and transform data for analysis:

- Pivoting and melting
- Grouping and aggregation
- Merging multiple datasets
- Feature engineering

### 4. Time Series Analysis

Built-in tools for temporal data:

- Date/time indexing
- Resampling and frequency conversion
- Rolling window operations
- Time zone handling

### 5. Financial Data Analysis

Stock prices, economic indicators, portfolio analysis.

### 6. Business Intelligence

Sales data analysis, customer segmentation, KPI tracking.

### 7. Machine Learning Pipelines

Data preparation for ML models:

- Feature selection and engineering
- Train/test split preparation
- Data normalization

## Installation

### Using pip

```bash
pip install pandas
```

### Using conda

```bash
conda install pandas
```

### Verify Installation

```python
import pandas as pd
print("Pandas version:", pd.__version__)
```

## How to Use Pandas

### 1. Data Structures

#### Series Creation

```python
import pandas as pd
import numpy as np

# From list
s1 = pd.Series([1, 2, 3, 4, 5])

# From numpy array
s2 = pd.Series(np.random.randn(5))

# With custom index
s3 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])

# From dictionary
s4 = pd.Series({'a': 1, 'b': 2, 'c': 3})
```

#### DataFrame Creation

```python
# From dictionary
df1 = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['NYC', 'LA', 'Chicago']
})

# From list of dictionaries
data = [
    {'Name': 'Alice', 'Age': 25, 'City': 'NYC'},
    {'Name': 'Bob', 'Age': 30, 'City': 'LA'},
    {'Name': 'Charlie', 'Age': 35, 'City': 'Chicago'}
]
df2 = pd.DataFrame(data)

# From numpy array
arr = np.random.randn(3, 3)
df3 = pd.DataFrame(arr, columns=['A', 'B', 'C'])
```

### 2. Reading and Writing Data

#### Reading Files

```python
# CSV files
df_csv = pd.read_csv('data.csv')

# Excel files
df_excel = pd.read_excel('data.xlsx', sheet_name='Sheet1')

# JSON files
df_json = pd.read_json('data.json')

# SQL databases
import sqlite3
conn = sqlite3.connect('database.db')
df_sql = pd.read_sql('SELECT * FROM table_name', conn)
```

#### Writing Files

```python
# To CSV
df.to_csv('output.csv', index=False)

# To Excel
df.to_excel('output.xlsx', sheet_name='Sheet1', index=False)

# To JSON
df.to_json('output.json')

# To SQL
df.to_sql('table_name', conn, if_exists='replace', index=False)
```

### 3. Data Inspection

```python
# Basic info
print(df.head())      # First 5 rows
print(df.tail())      # Last 5 rows
print(df.info())      # Data types and non-null counts
print(df.describe())  # Statistical summary

# Shape and size
print(df.shape)       # (rows, columns)
print(df.columns)     # Column names
print(df.index)       # Index
print(df.dtypes)      # Data types of each column
```

### 4. Indexing and Selection

#### Column Selection

```python
# Single column (returns Series)
names = df['Name']
ages = df.Age  # Alternative syntax

# Multiple columns (returns DataFrame)
subset = df[['Name', 'Age']]
```

#### Row Selection

```python
# By position (iloc)
first_row = df.iloc[0]      # First row
first_three = df.iloc[0:3]  # First 3 rows

# By label (loc)
row_by_index = df.loc[0]    # Row with index 0
rows_by_label = df.loc[[0, 2]]  # Rows 0 and 2
```

#### Boolean Indexing

```python
# Filter rows
adults = df[df['Age'] >= 18]
nyc_residents = df[df['City'] == 'NYC']

# Multiple conditions
young_nyc = df[(df['Age'] < 30) & (df['City'] == 'NYC')]
```

#### Advanced Indexing

```python
# Using query method
result = df.query('Age > 25 and City == "NYC"')

# Setting values conditionally
df.loc[df['Age'] < 18, 'Status'] = 'Minor'
df.loc[df['Age'] >= 18, 'Status'] = 'Adult'
```

### 5. Data Cleaning

#### Handling Missing Values

```python
# Check for missing values
print(df.isnull().sum())

# Drop rows with missing values
df_clean = df.dropna()

# Fill missing values
df_filled = df.fillna(0)  # Fill with 0
df_filled = df.fillna(df.mean())  # Fill with mean
df_filled = df.fillna(method='ffill')  # Forward fill
```

#### Data Type Conversion

```python
# Convert data types
df['Age'] = df['Age'].astype(int)
df['Price'] = df['Price'].astype(float)

# Convert to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Convert to category
df['Category'] = df['Category'].astype('category')
```

#### String Operations

```python
# String methods
df['Name_upper'] = df['Name'].str.upper()
df['Name_length'] = df['Name'].str.len()
df['Contains_alice'] = df['Name'].str.contains('Alice')
```

### 6. Data Operations

#### Adding/Removing Columns

```python
# Add new column
df['Age_in_months'] = df['Age'] * 12

# Remove column
df = df.drop('Age_in_months', axis=1)

# Rename columns
df = df.rename(columns={'Name': 'Full_Name', 'Age': 'Years'})
```

#### Mathematical Operations

```python
# Operations on columns
df['Double_Age'] = df['Age'] * 2
df['Age_plus_10'] = df['Age'] + 10

# Apply functions
df['Sqrt_Age'] = df['Age'].apply(np.sqrt)
df['Age_Category'] = df['Age'].apply(lambda x: 'Young' if x < 30 else 'Old')
```

### 7. Grouping and Aggregation

```python
# Group by single column
grouped = df.groupby('City')
print(grouped.mean())

# Group by multiple columns
grouped_multi = df.groupby(['City', 'Department'])

# Aggregation functions
result = df.groupby('City').agg({
    'Age': ['mean', 'min', 'max'],
    'Salary': 'sum'
})

# Custom aggregation
def range_func(x):
    return x.max() - x.min()

result = df.groupby('City')['Age'].agg(range_func)
```

### 8. Merging and Joining

#### Concatenation

```python
# Vertical concatenation (stack)
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
result = pd.concat([df1, df2])

# Horizontal concatenation (side by side)
result = pd.concat([df1, df2], axis=1)
```

#### Merging

```python
# Inner join (default)
result = pd.merge(df1, df2, on='key')

# Left join
result = pd.merge(df1, df2, on='key', how='left')

# Outer join
result = pd.merge(df1, df2, on='key', how='outer')

# Join on different column names
result = pd.merge(df1, df2, left_on='key1', right_on='key2')
```

### 9. Time Series

```python
# Create date range
dates = pd.date_range('2023-01-01', periods=100, freq='D')

# Create time series
ts = pd.Series(np.random.randn(100), index=dates)

# Resampling
monthly = ts.resample('M').mean()
quarterly = ts.resample('Q').sum()

# Rolling windows
rolling_mean = ts.rolling(window=7).mean()
rolling_std = ts.rolling(window=30).std()

# Shifting
shifted = ts.shift(1)  # Shift by 1 period
pct_change = ts.pct_change()  # Percentage change
```

### 10. Visualization

```python
# Basic plotting (requires matplotlib)
df['Age'].plot(kind='hist', title='Age Distribution')
df.plot.scatter(x='Age', y='Salary')

# Time series plotting
ts.plot(title='Time Series Data')

# Grouped plotting
df.groupby('City')['Salary'].mean().plot(kind='bar')
```

## Best Practices

### 1. Use Vectorized Operations

```python
# Good: Vectorized
df['new_column'] = df['column1'] * df['column2']

# Bad: Iterating over rows
df['new_column'] = [row['column1'] * row['column2'] for _, row in df.iterrows()]
```

### 2. Set Appropriate Data Types

```python
# Use categorical for low-cardinality string columns
df['category'] = df['category'].astype('category')

# Use appropriate numeric types
df['small_int'] = df['small_int'].astype(np.int8)
```

### 3. Handle Missing Data Properly

```python
# Don't just drop missing data without analysis
missing_analysis = df.isnull().sum() / len(df)

# Use appropriate imputation methods
df['numeric_col'] = df['numeric_col'].fillna(df['numeric_col'].median())
df['categorical_col'] = df['categorical_col'].fillna(df['categorical_col'].mode()[0])
```

### 4. Use Method Chaining

```python
# Good: Method chaining
result = (df
    .query('Age > 18')
    .groupby('City')
    .agg({'Salary': 'mean'})
    .reset_index()
    .sort_values('Salary', ascending=False)
)

# Bad: Multiple intermediate variables
filtered = df[df['Age'] > 18]
grouped = filtered.groupby('City')
aggregated = grouped.agg({'Salary': 'mean'})
reset = aggregated.reset_index()
result = reset.sort_values('Salary', ascending=False)
```

### 5. Avoid SettingWithCopyWarning

```python
# Good: Use .loc for assignment
df.loc[df['Age'] > 30, 'Senior'] = True

# Bad: Chained indexing
df[df['Age'] > 30]['Senior'] = True  # Warning!
```

### 6. Use Appropriate Indexing

```python
# Set meaningful index when appropriate
df = df.set_index('employee_id')

# Reset index when needed
df = df.reset_index()
```

### 7. Memory Management

```python
# Use chunks for large files
chunk_size = 10000
for chunk in pd.read_csv('large_file.csv', chunksize=chunk_size):
    process_chunk(chunk)

# Delete unused DataFrames
del large_df
```

### 8. Documentation and Type Hints

```python
from typing import Optional

def process_data(df: pd.DataFrame, threshold: Optional[float] = None) -> pd.DataFrame:
    """
    Process data by filtering and transforming.

    Parameters:
    df (pd.DataFrame): Input dataframe
    threshold (float, optional): Filtering threshold

    Returns:
    pd.DataFrame: Processed dataframe
    """
    if threshold is not None:
        df = df[df['value'] > threshold]

    df['processed'] = df['value'] * 2
    return df
```

## Common Pitfalls

### 1. Modifying Views vs Copies

```python
# This creates a view, modifying it affects original
subset = df[df['Age'] > 30]
subset['New_Column'] = 'Value'  # Modifies original df!

# Solution: Make a copy
subset = df[df['Age'] > 30].copy()
subset['New_Column'] = 'Value'  # Safe
```

### 2. Integer Division Issues

```python
# In Python 2, this would be integer division
df['ratio'] = df['a'] / df['b']  # Always float in Python 3
```

### 3. NaN Comparison Issues

```python
# This doesn't work as expected
df[df['column'] == np.nan]  # Never True

# Use isna() instead
df[df['column'].isna()]
```

### 4. Index Alignment Issues

```python
# Indexes must align for operations
s1 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
s2 = pd.Series([4, 5, 6], index=['a', 'b', 'd'])

result = s1 + s2  # Only 'a' and 'b' will have values, 'c' and 'd' will be NaN
```

### 5. Memory Usage with Large Datasets

```python
# object dtype uses more memory than necessary
df['category'] = df['category'].astype('category')  # Better

# Downcast numeric types
df['small_int'] = pd.to_numeric(df['small_int'], downcast='integer')
```

## Performance Tips

### 1. Use Efficient Data Types

```python
# Use category for strings with few unique values
df['status'] = df['status'].astype('category')

# Use appropriate numeric precision
df['price'] = df['price'].astype(np.float32)  # If float64 not needed
```

### 2. Avoid Loops, Use Vectorization

```python
# Vectorized operations are much faster
df['result'] = df['col1'] * df['col2'] + df['col3']
```

### 3. Use eval() for Complex Operations

```python
# For complex expressions
df.eval('result = col1 * col2 + col3', inplace=True)
```

### 4. Use query() for Filtering

```python
# query() is often faster than boolean indexing
result = df.query('age > 30 and city == "NYC"')
```

### 5. Consider Using Dask for Big Data

```python
# For datasets that don't fit in memory
import dask.dataframe as dd
df = dd.read_csv('large_file.csv')
```

### 6. Profile Your Code

```python
# Use pandas profiling tools
import pandas as pd
df.profile_report()  # Requires pandas-profiling package
```

## Integration with Other Libraries

### NumPy

```python
# Convert to numpy arrays
array = df.values
numpy_array = df.to_numpy()

# From numpy arrays
df = pd.DataFrame(numpy_array, columns=['A', 'B', 'C'])
```

### Matplotlib/Seaborn

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Basic plotting
df['column'].plot.hist()
plt.show()

# Seaborn integration
sns.scatterplot(data=df, x='col1', y='col2')
plt.show()
```

### Scikit-learn

```python
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Prepare features and target
X = df.drop('target', axis=1)
y = df['target']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

### SQL Databases

```python
import sqlalchemy as sa

# Create connection
engine = sa.create_engine('postgresql://user:pass@localhost/db')

# Read from SQL
df = pd.read_sql('SELECT * FROM table WHERE condition', engine)

# Write to SQL
df.to_sql('new_table', engine, if_exists='replace', index=False)
```

## Conclusion

Pandas is the Swiss Army knife of data manipulation in Python. Its powerful DataFrame and Series structures, combined with rich functionality for data cleaning, transformation, and analysis, make it indispensable for data science and analysis workflows.

**Key Takeaways:**

- **DataFrames are your primary tool** for structured data manipulation
- **Vectorize operations** whenever possible for performance
- **Chain methods** for readable, efficient code
- **Handle missing data** appropriately for your use case
- **Set correct data types** to optimize memory and performance
- **Use indexing wisely** for efficient data access

Mastering pandas will dramatically improve your ability to work with data in Python, making complex data manipulation tasks simple and efficient.
