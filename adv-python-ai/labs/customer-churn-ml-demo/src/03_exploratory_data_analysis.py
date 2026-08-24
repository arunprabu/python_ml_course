import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create visualization directory if it doesn't exist
os.makedirs('visualizations', exist_ok=True)

# Load featured data
df = pd.read_csv('data/customer_churn_featured.csv')

# Visualize churn distribution
plt.figure(figsize=(8, 6))
df['churned'].value_counts().plot(kind='bar')
plt.title('Churn Distribution')
plt.xlabel('Churned')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('visualizations/churn_distribution.png', dpi=300, bbox_inches='tight')
plt.close()

# Correlation heatmap
plt.figure(figsize=(12, 10))
# Select only numeric columns for correlation
numeric_df = df.select_dtypes(include=['number'])
sns.heatmap(numeric_df.corr(), cmap='coolwarm', center=0, annot=False)
plt.title('Feature Correlation Heatmap')
plt.tight_layout()
plt.savefig('visualizations/correlation_heatmap.png', dpi=300, bbox_inches='tight')
plt.close()

print("✓ Visualizations saved to 'visualizations/' folder:")
print("  - churn_distribution.png")
print("  - correlation_heatmap.png")