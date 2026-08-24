# 23_seaborn.py

# Comprehensive Seaborn Examples - Statistical Data Visualization

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

print("Seaborn Statistical Visualization Examples")
print("=" * 60)

# 1. Import and Setup

print("\n1. Import and Setup")

print(f"Seaborn version: {sns.__version__}")
print(f"Matplotlib version: {plt.matplotlib.__version__}")
print("Seaborn: High-level statistical visualization built on matplotlib")
print("Key advantages: Beautiful defaults, statistical focus, DataFrame integration")

# Set default seaborn theme
sns.set_theme(style="darkgrid")

# 2. Distribution Plots - Histogram and KDE

print("\n2. Distribution Plots - Histogram and KDE")

# Load seaborn built-in dataset
tips = sns.load_dataset('tips')
print(f"Tips dataset shape: {tips.shape}")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Histogram with hue
sns.histplot(data=tips, x='total_bill', hue='time', kde=True, ax=ax1, alpha=0.6)
ax1.set_title('Bill Distribution by Time', fontsize=14, fontweight='bold')
ax1.set_xlabel('Total Bill ($)')

# KDE plot
sns.kdeplot(data=tips, x='total_bill', hue='time', fill=True, ax=ax2, alpha=0.5)
ax2.set_title('Bill Density by Time', fontsize=14, fontweight='bold')
ax2.set_xlabel('Total Bill ($)')

plt.tight_layout()
try:
    plt.savefig('visualizations/seaborn_01_distribution.png', dpi=100, bbox_inches='tight')
    print("✓ Distribution plots saved as 'visualizations/seaborn_01_distribution.png'")
except:
    print("✓ Distribution plots created")
plt.close()

# 3. Distribution Plots - Advanced with Faceting

print("\n3. Distribution Plots - Advanced with Faceting")

# Using displot for faceted distributions
g = sns.displot(data=tips, x='total_bill', hue='sex', col='time', 
                kde=True, height=5, aspect=1.2)
g.fig.suptitle('Bill Distribution: Faceted by Time and Gender', 
               fontsize=16, fontweight='bold', y=1.02)

try:
    plt.savefig('visualizations/seaborn_02_faceted_dist.png', dpi=100, bbox_inches='tight')
    print("✓ Faceted distribution saved as 'visualizations/seaborn_02_faceted_dist.png'")
except:
    print("✓ Faceted distribution created")
plt.close()

# 4. Categorical Plots - Bar and Count Plots

print("\n4. Categorical Plots - Bar and Count Plots")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Bar plot with confidence intervals
sns.barplot(data=tips, x='day', y='total_bill', hue='time', 
            errorbar='ci', ax=ax1, palette='Set2')
ax1.set_title('Average Bill by Day and Time', fontsize=14, fontweight='bold')
ax1.set_ylabel('Average Bill ($)')

# Count plot
sns.countplot(data=tips, x='day', hue='sex', ax=ax2, palette='Set1')
ax2.set_title('Customer Count by Day and Gender', fontsize=14, fontweight='bold')
ax2.set_ylabel('Count')

plt.tight_layout()
try:
    plt.savefig('visualizations/seaborn_03_categorical.png', dpi=100, bbox_inches='tight')
    print("✓ Categorical plots saved as 'visualizations/seaborn_03_categorical.png'")
except:
    print("✓ Categorical plots created")
plt.close()

# 5. Categorical Plots - Box and Violin Plots

print("\n5. Categorical Plots - Box and Violin Plots")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Box plot
sns.boxplot(data=tips, x='day', y='total_bill', hue='time', ax=ax1, palette='pastel')
ax1.set_title('Bill Distribution by Day (Box Plot)', fontsize=14, fontweight='bold')
ax1.set_ylabel('Total Bill ($)')

# Violin plot
sns.violinplot(data=tips, x='day', y='tip', hue='time', split=True, 
               ax=ax2, palette='muted')
ax2.set_title('Tip Distribution by Day (Violin Plot)', fontsize=14, fontweight='bold')
ax2.set_ylabel('Tip ($)')

plt.tight_layout()
try:
    plt.savefig('visualizations/seaborn_04_box_violin.png', dpi=100, bbox_inches='tight')
    print("✓ Box and violin plots saved as 'visualizations/seaborn_04_box_violin.png'")
except:
    print("✓ Box and violin plots created")
plt.close()

# 6. Categorical Plots - Swarm and Strip Plots

print("\n6. Categorical Plots - Swarm and Strip Plots")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Swarm plot with violin overlay
sns.violinplot(data=tips, x='day', y='tip', ax=ax1, color='lightgray', alpha=0.5)
sns.swarmplot(data=tips, x='day', y='tip', hue='time', ax=ax1, size=4, palette='Set2')
ax1.set_title('Individual Tips by Day (Swarm Plot)', fontsize=14, fontweight='bold')
ax1.set_ylabel('Tip ($)')
ax1.legend(title='Time', loc='upper right')

# Strip plot
sns.stripplot(data=tips, x='day', y='total_bill', hue='sex', 
              dodge=True, ax=ax2, alpha=0.7, palette='dark')
ax2.set_title('Bills by Day and Gender (Strip Plot)', fontsize=14, fontweight='bold')
ax2.set_ylabel('Total Bill ($)')

plt.tight_layout()
try:
    plt.savefig('visualizations/seaborn_05_swarm_strip.png', dpi=100, bbox_inches='tight')
    print("✓ Swarm and strip plots saved as 'visualizations/seaborn_05_swarm_strip.png'")
except:
    print("✓ Swarm and strip plots created")
plt.close()

# 7. Relational Plots - Scatter with Multiple Dimensions

print("\n7. Relational Plots - Scatter with Multiple Dimensions")

plt.figure(figsize=(12, 6))
sns.scatterplot(data=tips, x='total_bill', y='tip', hue='time', 
                size='size', style='sex', sizes=(50, 250), 
                alpha=0.7, palette='deep')
plt.title('Restaurant Bills: Multi-dimensional Analysis', fontsize=16, fontweight='bold')
plt.xlabel('Total Bill ($)', fontsize=12)
plt.ylabel('Tip ($)', fontsize=12)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

try:
    plt.savefig('visualizations/seaborn_06_scatter.png', dpi=100, bbox_inches='tight')
    print("✓ Multi-dimensional scatter saved as 'visualizations/seaborn_06_scatter.png'")
except:
    print("✓ Multi-dimensional scatter created")
plt.close()

# 8. Relational Plots - Line Plots with Confidence Intervals

print("\n8. Relational Plots - Line Plots with Confidence Intervals")

# Custom time series business data
np.random.seed(42)
months = pd.date_range('2024-01', periods=12, freq='M')
regions = ['North', 'South', 'East', 'West']
timeseries_data = pd.DataFrame({
    'Month': np.tile(months, len(regions)),
    'Region': np.repeat(regions, len(months)),
    'Revenue': np.random.randint(80, 200, len(months) * len(regions)) * 1000 + 
               np.repeat([0, 10000, -5000, 5000], len(months))
})

plt.figure(figsize=(12, 6))
sns.lineplot(data=timeseries_data, x='Month', y='Revenue', hue='Region', 
             marker='o', linewidth=2.5, markersize=8, errorbar=('ci', 95))
plt.title('Monthly Revenue by Region (with 95% CI)', fontsize=16, fontweight='bold')
plt.ylabel('Revenue ($)', fontsize=12)
plt.xticks(rotation=45)
plt.legend(title='Region', title_fontsize=11)
plt.tight_layout()

try:
    plt.savefig('visualizations/seaborn_07_lineplot.png', dpi=100, bbox_inches='tight')
    print("✓ Line plot with CI saved as 'visualizations/seaborn_07_lineplot.png'")
except:
    print("✓ Line plot with CI created")
plt.close()

# 9. Matrix Plots - Heatmap

print("\n9. Matrix Plots - Heatmap")

# Load iris dataset for correlation
iris = sns.load_dataset('iris')
iris_corr = iris.drop('species', axis=1).corr()

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Correlation heatmap
sns.heatmap(iris_corr, annot=True, fmt='.2f', cmap='coolwarm', 
            center=0, square=True, linewidths=1, ax=ax1, cbar_kws={'label': 'Correlation'})
ax1.set_title('Iris Features Correlation', fontsize=14, fontweight='bold')

# Pivot table heatmap - flights data
flights = sns.load_dataset('flights')
flights_pivot = flights.pivot(index='month', columns='year', values='passengers')
sns.heatmap(flights_pivot, annot=True, fmt='d', cmap='YlGnBu', ax=ax2)
ax2.set_title('Monthly Passengers by Year', fontsize=14, fontweight='bold')

plt.tight_layout()
try:
    plt.savefig('visualizations/seaborn_08_heatmap.png', dpi=100, bbox_inches='tight')
    print("✓ Heatmaps saved as 'visualizations/seaborn_08_heatmap.png'")
except:
    print("✓ Heatmaps created")
plt.close()

# 10. Matrix Plots - Clustermap

print("\n10. Matrix Plots - Clustermap")

# Clustermap with hierarchical clustering
g = sns.clustermap(flights_pivot, cmap='viridis', figsize=(10, 8),
                   dendrogram_ratio=0.15, cbar_pos=(0.02, 0.8, 0.03, 0.15),
                   linewidths=0.5, annot=False)
g.fig.suptitle('Hierarchical Clustering of Flight Patterns', 
               fontsize=16, fontweight='bold', y=0.98)

try:
    plt.savefig('visualizations/seaborn_09_clustermap.png', dpi=100, bbox_inches='tight')
    print("✓ Clustermap saved as 'visualizations/seaborn_09_clustermap.png'")
except:
    print("✓ Clustermap created")
plt.close()

# 11. Regression Plots

print("\n11. Regression Plots")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Simple linear regression
sns.regplot(data=tips, x='total_bill', y='tip', ax=ax1, 
            scatter_kws={'alpha': 0.5}, line_kws={'color': 'red', 'linewidth': 2})
ax1.set_title('Tip vs Total Bill (Linear Regression)', fontsize=14, fontweight='bold')
ax1.set_xlabel('Total Bill ($)')
ax1.set_ylabel('Tip ($)')

# Polynomial regression
sns.regplot(data=tips, x='total_bill', y='tip', order=2, ax=ax2,
            scatter_kws={'alpha': 0.5}, line_kws={'color': 'green', 'linewidth': 2})
ax2.set_title('Tip vs Total Bill (Polynomial Regression)', fontsize=14, fontweight='bold')
ax2.set_xlabel('Total Bill ($)')
ax2.set_ylabel('Tip ($)')

plt.tight_layout()
try:
    plt.savefig('visualizations/seaborn_10_regression.png', dpi=100, bbox_inches='tight')
    print("✓ Regression plots saved as 'visualizations/seaborn_10_regression.png'")
except:
    print("✓ Regression plots created")
plt.close()

# 12. Regression Plots with Faceting - lmplot

print("\n12. Regression Plots with Faceting - lmplot")

# Faceted regression
g = sns.lmplot(data=tips, x='total_bill', y='tip', hue='time', 
               col='sex', row='smoker', height=4, aspect=1.2,
               scatter_kws={'alpha': 0.5}, line_kws={'linewidth': 2})
g.fig.suptitle('Regression Analysis: Faceted by Multiple Variables', 
               fontsize=16, fontweight='bold', y=1.01)

try:
    plt.savefig('visualizations/seaborn_11_lmplot.png', dpi=100, bbox_inches='tight')
    print("✓ Faceted regression saved as 'visualizations/seaborn_11_lmplot.png'")
except:
    print("✓ Faceted regression created")
plt.close()

# 13. Pair Plots and Multi-Plot Grids

print("\n13. Pair Plots and Multi-Plot Grids")

# Pairplot with iris data
g = sns.pairplot(iris, hue='species', diag_kind='kde', 
                 palette='husl', height=2.5, aspect=1,
                 plot_kws={'alpha': 0.6}, diag_kws={'alpha': 0.7})
g.fig.suptitle('Iris Dataset: Pairwise Feature Relationships', 
               fontsize=16, fontweight='bold', y=1.01)

try:
    plt.savefig('visualizations/seaborn_12_pairplot.png', dpi=100, bbox_inches='tight')
    print("✓ Pairplot saved as 'visualizations/seaborn_12_pairplot.png'")
except:
    print("✓ Pairplot created")
plt.close()

# 14. Advanced Styling - Themes and Context

print("\n14. Advanced Styling - Themes and Context")

# Demonstrate different themes
styles = ['darkgrid', 'whitegrid', 'dark', 'white']
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
axes = axes.ravel()

for idx, style in enumerate(styles):
    sns.set_theme(style=style)
    sns.scatterplot(data=tips, x='total_bill', y='tip', hue='time', 
                    ax=axes[idx], palette='Set2', alpha=0.7)
    axes[idx].set_title(f'Style: {style}', fontsize=12, fontweight='bold')
    axes[idx].set_xlabel('Total Bill ($)')
    axes[idx].set_ylabel('Tip ($)')

plt.suptitle('Seaborn Themes Comparison', fontsize=16, fontweight='bold')
plt.tight_layout()

try:
    plt.savefig('visualizations/seaborn_13_themes.png', dpi=100, bbox_inches='tight')
    print("✓ Theme comparison saved as 'visualizations/seaborn_13_themes.png'")
except:
    print("✓ Theme comparison created")
plt.close()

# Reset to default
sns.set_theme(style='darkgrid')

# 15. Color Palettes Showcase

print("\n15. Color Palettes Showcase")

palettes = ['deep', 'muted', 'bright', 'pastel', 'dark', 'colorblind']
fig, axes = plt.subplots(3, 2, figsize=(14, 12))
axes = axes.ravel()

for idx, palette_name in enumerate(palettes):
    sns.barplot(data=tips, x='day', y='total_bill', hue='time', 
                ax=axes[idx], palette=palette_name, errorbar=None)
    axes[idx].set_title(f'Palette: {palette_name}', fontsize=12, fontweight='bold')
    axes[idx].set_ylabel('Average Bill ($)')
    axes[idx].legend(title='Time', loc='upper right', fontsize=8)

plt.suptitle('Seaborn Color Palettes Comparison', fontsize=16, fontweight='bold')
plt.tight_layout()

try:
    plt.savefig('visualizations/seaborn_14_palettes.png', dpi=100, bbox_inches='tight')
    print("✓ Color palettes saved as 'visualizations/seaborn_14_palettes.png'")
except:
    print("✓ Color palettes created")
plt.close()

# Cleanup

print("\n16. Cleanup")

print("Created visualization files:")
for i in range(1, 15):
    print(f"  - seaborn_{i:02d}_*.png")

print("\n" + "=" * 60)
print("Seaborn statistical visualization examples completed!")
print("=" * 60)
