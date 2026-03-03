import pandas as pd 

df = pd.read_csv("data.csv")
#Select only the 'Make', 'Model', and 'Electric Vehicle Type' columns

selection_model_make = df[['Make', 'Model', 'Electric Vehicle Type']]


#Select rows 20-30 (inclusive)

row_20_30 = df.iloc[ 20:31]
row_20_30_loc = df.loc[20:30]

#Select all rows where the 'State' is 'WA'

state_WA = df[df['State'] == 'WA']

#Select the 'City' and 'County' columns for the first 50 rows

city_county = df[['City', 'County']].head(50)
print (city_county)