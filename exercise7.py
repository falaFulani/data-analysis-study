# Create new columns and transform existing data.

import pandas as pd 

df = pd.read_csv("data.csv")

df.columns

print (df.columns)

# Tasks:

#     Extract the year from the 'Model Year' column (if not already numeric)

year_from = pd.to_numeric(df['Model Year'])

print(year_from)
#     Create a new column 'Vehicle Age' (current year - model year, assume current year is 2026)
df['Vechile Age'] = 2026 - df['Model Year']

print(df['Vechile Age'])
#     Create a categorical column 'Range Category' (Short: <100, Medium: 100-200, Long: 200-300, Extended: 300+)

#     Extract city and state from 'Vehicle Location' (if needed, or just note the format)

#     Create a binary column 'Is_Tesla' (True/False)