!pip install seaborn
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = {
    "ID": [1, 2, 3, 4, 5, 6, 7],
    "Name": ["Alice", "Bob", "Carol", "Dave", "Eve", "Alice", "Frank"],
    "Age": [25, 30, None, 28, 29, 25, None],
    "Salary": [50000, 60000, 55000, None, 62000, 50000, None],
    "Department": ["HR", "Finance", "HR", "Marketing", "Finance", "HR", "IT"]
}
df = pd.DataFrame(data)

# Handle missing values
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())

# Remove duplicates
df.drop_duplicates(inplace=True)

# Display statistical summary
print("Statistical Summary:")
print(df.describe(include='all'))

# Visualization
sns.set(style="whitegrid")

# Bar plot for Salary by Department
plt.figure(figsize=(8, 6))
sns.barplot(x="Department", y="Salary", data=df, estimator="mean")
plt.title("Average Salary by Department")
plt.show()

# Histogram for Age distribution
plt.figure(figsize=(8, 6))
sns.histplot(df['Age'], bins=5, kde=True)
plt.title("Distribution of Age")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# Pie chart for Department distribution
plt.figure(figsize=(8, 6))
df['Department'].value_counts().plot.pie(autopct='%1.1f%%')
plt.title("Department Distribution")
plt.ylabel("")  # Hide the y-label
plt.show()
