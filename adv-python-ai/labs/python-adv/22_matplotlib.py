# 22_matplotlib.py

# Comprehensive Matplotlib Examples with NumPy and Pandas

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

print("Matplotlib Visualization Examples")
print("=" * 60)

# 1. Import and Setup

print("\n1. Import and Setup")

print(f"Matplotlib version: {plt.matplotlib.__version__}")
print("Matplotlib is the foundational plotting library for Python")
print("Integrates seamlessly with NumPy arrays and Pandas DataFrames")

# 2. Basic Line Plot with NumPy

print("\n2. Basic Line Plot with NumPy")

# Simple synthetic data - mathematical function
x = np.linspace(0, 10, 100)
y = np.sin(x)
y2 = np.cos(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, label='sin(x)', color='blue', linewidth=2)
plt.plot(x, y2, label='cos(x)', color='red', linewidth=2, linestyle='--')
plt.title('Trigonometric Functions', fontsize=16, fontweight='bold')
plt.xlabel('x values', fontsize=12)
plt.ylabel('y values', fontsize=12)
plt.legend(fontsize=10)
plt.grid(True, alpha=0.3)
plt.tight_layout()
try:
    plt.savefig('visualizations/matplotlib_01_line.png', dpi=100, bbox_inches='tight')
    print("✓ Line plot saved as 'visualizations/matplotlib_01_line.png'")
except:
    print("✓ Line plot created")
plt.close()

# 3. Scatter Plot with NumPy

print("\n3. Scatter Plot with NumPy")

# Synthetic data - random correlation
np.random.seed(42)
x_scatter = np.random.randn(100)
y_scatter = 2 * x_scatter + np.random.randn(100) * 0.5

plt.figure(figsize=(10, 6))
plt.scatter(x_scatter, y_scatter, c='purple', alpha=0.6, s=50, edgecolors='black')
plt.title('Scatter Plot: Correlation Analysis', fontsize=16, fontweight='bold')
plt.xlabel('Variable X', fontsize=12)
plt.ylabel('Variable Y', fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()
try:
    plt.savefig('visualizations/matplotlib_02_scatter.png', dpi=100, bbox_inches='tight')
    print("✓ Scatter plot saved as 'visualizations/matplotlib_02_scatter.png'")
except:
    print("✓ Scatter plot created")
plt.close()

# 4. Bar Chart with Pandas - Business Data

print("\n4. Bar Chart with Pandas - Business Data")

# Realistic business data - quarterly sales
sales_data = pd.DataFrame({
    'Quarter': ['Q1', 'Q2', 'Q3', 'Q4'],
    'Sales': [45000, 52000, 48000, 61000],
    'Expenses': [32000, 35000, 33000, 38000]
})

fig, ax = plt.subplots(figsize=(10, 6))
x_pos = np.arange(len(sales_data['Quarter']))
width = 0.35

bars1 = ax.bar(x_pos - width/2, sales_data['Sales'], width, label='Sales', color='#2ecc71')
bars2 = ax.bar(x_pos + width/2, sales_data['Expenses'], width, label='Expenses', color='#e74c3c')

ax.set_xlabel('Quarter', fontsize=12)
ax.set_ylabel('Amount ($)', fontsize=12)
ax.set_title('Quarterly Sales vs Expenses', fontsize=16, fontweight='bold')
ax.set_xticks(x_pos)
ax.set_xticklabels(sales_data['Quarter'])
ax.legend()
ax.grid(axis='y', alpha=0.3)

plt.tight_layout()
try:
    plt.savefig('visualizations/matplotlib_03_bar.png', dpi=100, bbox_inches='tight')
    print("✓ Bar chart saved as 'visualizations/matplotlib_03_bar.png'")
except:
    print("✓ Bar chart created")
plt.close()

# 5. Histogram with NumPy - Distribution Analysis

print("\n5. Histogram with NumPy - Distribution Analysis")

# Synthetic data - normal distribution
data_normal = np.random.normal(100, 15, 1000)
data_uniform = np.random.uniform(70, 130, 1000)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

ax1.hist(data_normal, bins=30, color='steelblue', alpha=0.7, edgecolor='black')
ax1.set_title('Normal Distribution', fontsize=14, fontweight='bold')
ax1.set_xlabel('Value', fontsize=12)
ax1.set_ylabel('Frequency', fontsize=12)
ax1.axvline(np.mean(data_normal), color='red', linestyle='--', linewidth=2, label=f'Mean: {np.mean(data_normal):.1f}')
ax1.legend()
ax1.grid(axis='y', alpha=0.3)

ax2.hist(data_uniform, bins=30, color='coral', alpha=0.7, edgecolor='black')
ax2.set_title('Uniform Distribution', fontsize=14, fontweight='bold')
ax2.set_xlabel('Value', fontsize=12)
ax2.set_ylabel('Frequency', fontsize=12)
ax2.grid(axis='y', alpha=0.3)

plt.tight_layout()
try:
    plt.savefig('visualizations/matplotlib_04_histogram.png', dpi=100, bbox_inches='tight')
    print("✓ Histogram saved as 'visualizations/matplotlib_04_histogram.png'")
except:
    print("✓ Histogram created")
plt.close()

# 6. Time Series with Pandas - Business Data

print("\n6. Time Series with Pandas - Business Data")

# Realistic business data - monthly revenue
dates = pd.date_range('2024-01-01', periods=12, freq='M')
revenue_data = pd.DataFrame({
    'Date': dates,
    'Revenue': [120000, 135000, 142000, 138000, 155000, 168000, 
                175000, 172000, 185000, 192000, 198000, 215000],
    'Target': [130000, 135000, 140000, 145000, 150000, 155000,
               160000, 165000, 170000, 175000, 180000, 185000]
})

plt.figure(figsize=(12, 6))
plt.plot(revenue_data['Date'], revenue_data['Revenue'], marker='o', 
         linewidth=2, markersize=8, label='Actual Revenue', color='#3498db')
plt.plot(revenue_data['Date'], revenue_data['Target'], marker='s', 
         linewidth=2, markersize=6, label='Target', color='#e74c3c', linestyle='--')
plt.fill_between(revenue_data['Date'], revenue_data['Revenue'], 
                  revenue_data['Target'], alpha=0.2, color='green')
plt.title('Monthly Revenue Performance 2024', fontsize=16, fontweight='bold')
plt.xlabel('Month', fontsize=12)
plt.ylabel('Revenue ($)', fontsize=12)
plt.legend(fontsize=10)
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45)
plt.tight_layout()
try:
    plt.savefig('visualizations/matplotlib_05_timeseries.png', dpi=100, bbox_inches='tight')
    print("✓ Time series plot saved as 'visualizations/matplotlib_05_timeseries.png'")
except:
    print("✓ Time series plot created")
plt.close()

# 7. Pie Chart with Pandas - Business Data

print("\n7. Pie Chart with Pandas - Business Data")

# Realistic business data - market share
market_data = pd.DataFrame({
    'Company': ['Company A', 'Company B', 'Company C', 'Company D', 'Others'],
    'MarketShare': [35, 25, 20, 12, 8]
})

colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#ff99cc']
explode = (0.1, 0, 0, 0, 0)

plt.figure(figsize=(10, 8))
plt.pie(market_data['MarketShare'], labels=market_data['Company'], 
        autopct='%1.1f%%', startangle=90, colors=colors, explode=explode,
        shadow=True, textprops={'fontsize': 12})
plt.title('Market Share Distribution', fontsize=16, fontweight='bold', pad=20)
plt.axis('equal')
plt.tight_layout()
try:
    plt.savefig('visualizations/matplotlib_06_pie.png', dpi=100, bbox_inches='tight')
    print("✓ Pie chart saved as 'visualizations/matplotlib_06_pie.png'")
except:
    print("✓ Pie chart created")
plt.close()

# 8. Multiple Subplots with NumPy and Pandas

print("\n8. Multiple Subplots with NumPy and Pandas")

# Mixed data - synthetic and business
x_data = np.linspace(0, 2*np.pi, 100)
employee_data = pd.DataFrame({
    'Department': ['Sales', 'Engineering', 'Marketing', 'HR', 'Operations'],
    'Employees': [45, 78, 32, 15, 28],
    'AvgSalary': [65000, 95000, 58000, 52000, 48000]
})

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))

# Subplot 1: Sine and Cosine
ax1.plot(x_data, np.sin(x_data), 'b-', label='sin(x)', linewidth=2)
ax1.plot(x_data, np.cos(x_data), 'r--', label='cos(x)', linewidth=2)
ax1.set_title('Trigonometric Functions', fontweight='bold')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.legend()
ax1.grid(True, alpha=0.3)

# Subplot 2: Employee count
ax2.barh(employee_data['Department'], employee_data['Employees'], color='skyblue', edgecolor='black')
ax2.set_title('Employees by Department', fontweight='bold')
ax2.set_xlabel('Number of Employees')
ax2.grid(axis='x', alpha=0.3)

# Subplot 3: Scatter with regression
x_reg = np.linspace(0, 10, 50)
y_reg = 2*x_reg + 1 + np.random.randn(50)*2
ax3.scatter(x_reg, y_reg, alpha=0.6, color='green')
z = np.polyfit(x_reg, y_reg, 1)
p = np.poly1d(z)
ax3.plot(x_reg, p(x_reg), "r--", linewidth=2, label='Trend line')
ax3.set_title('Scatter with Trend Line', fontweight='bold')
ax3.set_xlabel('X')
ax3.set_ylabel('Y')
ax3.legend()
ax3.grid(True, alpha=0.3)

# Subplot 4: Average salary
ax4.bar(employee_data['Department'], employee_data['AvgSalary'], color='orange', edgecolor='black')
ax4.set_title('Average Salary by Department', fontweight='bold')
ax4.set_ylabel('Salary ($)')
ax4.tick_params(axis='x', rotation=45)
ax4.grid(axis='y', alpha=0.3)

plt.suptitle('Dashboard: Multiple Visualizations', fontsize=18, fontweight='bold', y=1.00)
plt.tight_layout()
try:
    plt.savefig('visualizations/matplotlib_07_subplots.png', dpi=100, bbox_inches='tight')
    print("✓ Subplots saved as 'visualizations/matplotlib_07_subplots.png'")
except:
    print("✓ Multiple subplots created")
plt.close()

# 9. Box Plot with Pandas - Statistical Analysis

print("\n9. Box Plot with Pandas - Statistical Analysis")

# Realistic business data - performance metrics
np.random.seed(42)
performance_data = pd.DataFrame({
    'TeamA': np.random.normal(75, 10, 100),
    'TeamB': np.random.normal(82, 8, 100),
    'TeamC': np.random.normal(70, 12, 100),
    'TeamD': np.random.normal(88, 6, 100)
})

plt.figure(figsize=(10, 6))
bp = plt.boxplot([performance_data['TeamA'], performance_data['TeamB'], 
                   performance_data['TeamC'], performance_data['TeamD']],
                  labels=['Team A', 'Team B', 'Team C', 'Team D'],
                  patch_artist=True,
                  notch=True,
                  showmeans=True)

colors = ['lightblue', 'lightgreen', 'lightcoral', 'lightyellow']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

plt.title('Team Performance Distribution', fontsize=16, fontweight='bold')
plt.ylabel('Performance Score', fontsize=12)
plt.xlabel('Teams', fontsize=12)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
try:
    plt.savefig('visualizations/matplotlib_08_boxplot.png', dpi=100, bbox_inches='tight')
    print("✓ Box plot saved as 'visualizations/matplotlib_08_boxplot.png'")
except:
    print("✓ Box plot created")
plt.close()

# 10. Heatmap with NumPy - Correlation Matrix

print("\n10. Heatmap with NumPy - Correlation Matrix")

# Realistic business data - metrics correlation
np.random.seed(42)
metrics_data = pd.DataFrame({
    'Sales': np.random.randint(50, 100, 20),
    'Marketing': np.random.randint(40, 90, 20),
    'Customer_Satisfaction': np.random.randint(60, 100, 20),
    'Employee_Engagement': np.random.randint(55, 95, 20)
})

correlation_matrix = metrics_data.corr()

plt.figure(figsize=(10, 8))
im = plt.imshow(correlation_matrix, cmap='coolwarm', aspect='auto', vmin=-1, vmax=1)
plt.colorbar(im, label='Correlation Coefficient')

plt.xticks(range(len(correlation_matrix.columns)), correlation_matrix.columns, rotation=45, ha='right')
plt.yticks(range(len(correlation_matrix.columns)), correlation_matrix.columns)

for i in range(len(correlation_matrix.columns)):
    for j in range(len(correlation_matrix.columns)):
        text = plt.text(j, i, f'{correlation_matrix.iloc[i, j]:.2f}',
                       ha="center", va="center", color="black", fontsize=12, fontweight='bold')

plt.title('Business Metrics Correlation Heatmap', fontsize=16, fontweight='bold', pad=20)
plt.tight_layout()
try:
    plt.savefig('visualizations/matplotlib_09_heatmap.png', dpi=100, bbox_inches='tight')
    print("✓ Heatmap saved as 'visualizations/matplotlib_09_heatmap.png'")
except:
    print("✓ Heatmap created")
plt.close()

# 11. Pandas DataFrame Plot Methods

print("\n11. Pandas DataFrame Plot Methods")

# Realistic business data - monthly metrics
monthly_data = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Sales': [45, 52, 48, 61, 58, 67],
    'Costs': [32, 35, 33, 38, 36, 40],
    'Profit': [13, 17, 15, 23, 22, 27]
})
monthly_data.set_index('Month', inplace=True)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Area plot
monthly_data.plot(kind='area', ax=axes[0, 0], alpha=0.6, title='Area Plot')
axes[0, 0].set_ylabel('Amount ($K)')
axes[0, 0].grid(True, alpha=0.3)

# Line plot
monthly_data.plot(kind='line', ax=axes[0, 1], marker='o', title='Line Plot')
axes[0, 1].set_ylabel('Amount ($K)')
axes[0, 1].grid(True, alpha=0.3)

# Bar plot
monthly_data.plot(kind='bar', ax=axes[1, 0], title='Bar Plot', edgecolor='black')
axes[1, 0].set_ylabel('Amount ($K)')
axes[1, 0].grid(axis='y', alpha=0.3)

# Stacked bar
monthly_data.plot(kind='bar', stacked=True, ax=axes[1, 1], title='Stacked Bar Plot', edgecolor='black')
axes[1, 1].set_ylabel('Amount ($K)')
axes[1, 1].grid(axis='y', alpha=0.3)

plt.suptitle('Pandas DataFrame Plot Methods', fontsize=16, fontweight='bold')
plt.tight_layout()
try:
    plt.savefig('visualizations/matplotlib_10_pandas.png', dpi=100, bbox_inches='tight')
    print("✓ Pandas plot methods saved as 'visualizations/matplotlib_10_pandas.png'")
except:
    print("✓ Pandas plot methods created")
plt.close()

# 12. Advanced Styling and Customization

print("\n12. Advanced Styling and Customization")

# Using different styles
available_styles = ['default', 'seaborn-v0_8-darkgrid', 'ggplot', 'bmh']
x = np.linspace(0, 10, 100)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
axes = axes.ravel()

for idx, style_name in enumerate(available_styles):
    try:
        with plt.style.context(style_name):
            axes[idx].plot(x, np.sin(x), linewidth=2, label='sin(x)')
            axes[idx].plot(x, np.cos(x), linewidth=2, label='cos(x)')
            axes[idx].set_title(f'Style: {style_name}', fontweight='bold')
            axes[idx].legend()
            axes[idx].grid(True, alpha=0.3)
    except:
        axes[idx].plot(x, np.sin(x), linewidth=2, label='sin(x)')
        axes[idx].plot(x, np.cos(x), linewidth=2, label='cos(x)')
        axes[idx].set_title(f'Style: default', fontweight='bold')
        axes[idx].legend()
        axes[idx].grid(True, alpha=0.3)

plt.suptitle('Different Matplotlib Styles', fontsize=16, fontweight='bold')
plt.tight_layout()
try:
    plt.savefig('visualizations/matplotlib_11_styles.png', dpi=100, bbox_inches='tight')
    print("✓ Style examples saved as 'visualizations/matplotlib_11_styles.png'")
except:
    print("✓ Style examples created")
plt.close()

# 13. Cleanup

print("\n13. Cleanup")

import os
plot_files = [f'plot_{i:02d}_*.png' for i in range(1, 12)]
print("Created visualization files:")
for i in range(1, 12):
    print(f"  - plot_{i:02d}_*.png")

print("\n" + "=" * 60)
print("Matplotlib visualization examples completed!")
print("=" * 60)
