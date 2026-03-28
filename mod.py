import pandas as pd

data = {
    'Name': ['Zayn', 'Malik', 'Atharv', 'Nasar'],
    'Age': [19, None, 20, 22],
    'Marks': [80,95, None,85]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

df.fillna(0, inplace=True)

df['Total'] = df['Marks'] + 5

df.rename(columns={'Marks': 'Score'}, inplace=True)

print("\nModified Data:")
print(df)

