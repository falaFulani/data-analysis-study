import pandas as pd 

df = pd.read_csv("data.csv")

# Count number of vehicles by Make
vechile_byMake = df.groupby('Make').size()
print("Top 5 Makes by count:")
print(vechile_byMake.head())

# Find average electric range by Electric Vehicle Type
avg_elec_range = df.groupby('Electric Vehicle Type')['Electric Range'].mean()
print("\nAverage range by vehicle type:")
print(avg_elec_range)
# Find maximum electric range by Make
max_range = df.groupby('Make')['Electric Range'].max().sort_values(ascending=False)
print("\nTop 5 Makes by max range:")
print(max_range.head())
# Count vehicles by County, sorted by count descending
by_county = df.groupby('County').size().sort_values(ascending=False)
print("\nTop 5 Counties by vehicle count:")
print(by_county.head())
# Find the most common Model for each Make

common_model = df.groupby('Make')['Model'].agg(lambda x: x.value_counts().index[0])

print("\nMost common model for top 5 Makes:")
print(common_model.head())

print(common_model)