import pandas as pd 

df = pd.read_csv("data.csv")

df_columns = df.columns

info = df.info()
# Identify and handle missing data.

# Tasks:

#     Check for null values in each column

is_null_col = df.isna().sum()


#     Calculate the percentage of missing values per column
missing = df.isna().mean()*100
#     Fill missing 'Electric Utility' values with "Unknown"
electric_utility = df['Electric Utility'].fillna("Unknown")
#     Drop rows where 'Legislative District' is missing
drop_district = df.dropna(subset=['Legislative District'],inplace=True)
print(drop_district)
print(df.isna().sum())