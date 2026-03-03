
import pandas as pd 

df = pd.read_csv("data.csv")
# Sort and rank the data.

# Tasks:

#     Sort vehicles by Model Year (descending)
_model_year_des = df.sort_values(by='Model Year', ascending=False)
#     Sort by Electric Range (highest to lowest)
highest_lowest = df.sort_values(by='Electric Range', ascending=False)
#     Find top 10 vehicles with highest electric range
highest_range = df.sort_values(by='Electric Range', ascending=False).head(10)
#     Sort by Make, then by Model, then by Model Year
model_model_year = df.sort_values(by=['Make', 'Model', 'Model Year'])
print (highest_lowest)