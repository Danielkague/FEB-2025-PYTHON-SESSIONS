import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Task 1: Load and Explore the Dataset
# Create DataFrame from the provided data
data = pd.read_csv('Medicaldataset.csv')

df = pd.DataFrame(data)

# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(df.head())

# Explore the structure of the dataset
print("\nDataset Information:")
print(df.info())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# No missing values in this dataset, so no cleaning needed

# Task 2: Basic Data Analysis
# Compute basic statistics
print("\nBasic Statistics:")
print(df.describe())

# Perform grouping on the categorical column 'Result' and compute means
print("\nGrouped Means by Result:")
grouped_means = df.groupby('Result').mean()
print(grouped_means)

# Task 3: Data Visualization
plt.figure(figsize=(15, 10))

# 1. Line chart - Heart Rate vs Age
plt.subplot(2, 2, 1)
plt.plot(df['Age'], df['Heart rate'], marker='o', linestyle='-', color='blue')
plt.title('Heart Rate vs Age')
plt.xlabel('Age')
plt.ylabel('Heart Rate (bpm)')
plt.grid(True)

# 2. Bar chart - Average Blood Pressure by Result
plt.subplot(2, 2, 2)
result_means = df.groupby(
    'Result')[['Systolic blood pressure', 'Diastolic blood pressure']].mean()
result_means.plot(kind='bar', ax=plt.gca())
plt.title('Average Blood Pressure by Result')
plt.xlabel('Result')
plt.ylabel('Blood Pressure (mmHg)')
plt.legend(['Systolic', 'Diastolic'])

# 3. Histogram - Blood Sugar Distribution
plt.subplot(2, 2, 3)
plt.hist(df['Blood sugar'], bins=3, color='green', alpha=0.7)
plt.title('Blood Sugar Distribution')
plt.xlabel('Blood Sugar (mg/dL)')
plt.ylabel('Frequency')

# 4. Scatter plot - CK-MB vs Troponin with Result coloring
plt.subplot(2, 2, 4)
colors = {'negative': 'blue', 'positive': 'red'}
for result in df['Result'].unique():
    subset = df[df['Result'] == result]
    plt.scatter(subset['CK-MB'], subset['Troponin'],
                label=result, color=colors[result], alpha=0.7)
plt.title('CK-MB vs Troponin by Result')
plt.xlabel('CK-MB')
plt.ylabel('Troponin')
plt.legend()
# Using log scale for better visualization due to large range
plt.yscale('log')

plt.tight_layout()
plt.show()

# Additional Analysis: Correlation Matrix
plt.figure(figsize=(10, 8))
# Convert 'Result' to numeric for correlation analysis (positive=1, negative=0)
df['Result_numeric'] = df['Result'].map({'positive': 1, 'negative': 0})
# Select only numeric columns
numeric_df = df.select_dtypes(include=[np.number])
# Create correlation matrix
corr_matrix = numeric_df.corr()
# Plot heatmap
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix of Heart Health Metrics')
plt.tight_layout()
plt.show()

# Findings summary
print("\nKey Findings:")
print("1. Positive cases have significantly higher cardiac markers (CK-MB and Troponin)")
print("2. Average systolic blood pressure is higher in negative cases")
print("3. Average heart rate is higher in positive cases")
print("4. Blood sugar levels appear elevated in all patients, but more so in positive cases")
print("5. The strongest positive correlations with a positive result are with CK-MB and Troponin levels")
