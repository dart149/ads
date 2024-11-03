import pandas as pd
data = {
    'Age': [25, 30, None, 28, 30, None],
    'Salary': [50000, 54000, 58000, None, 54000, 58000],
    'Department': ['HR', 'Finance', None, 'IT', 'Finance', 'IT']
}
df = pd.DataFrame(data)
df = df.assign(
    Age=df["Age"].fillna(df["Age"].mean()),
    Salary=df["Salary"].fillna(df["Salary"].median()),
    Department=df["Department"].fillna(df["Department"].mode()[0])
)
print(df)
metadata={
    "Rows":df.shape[0],
    "Columns":df.shape[1],
    "DataTypes":df.dtypes,
    "Null":df.isnull().sum()
}
print(metadata)
