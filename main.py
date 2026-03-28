import pandas as pd

df = pd.read_csv('students.csv')

print("First 5 rows of the dataset:")
print(df.head())

print("\nLast 5 rows of the dataset:")
print(df.tail())

print("\nDataset Info:")
df.info()

print("\nStatistical Summary:")
print(df.describe())
