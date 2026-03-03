import pandas as pd 

df = pd.read_csv("data.csv")
df_columns = df.columns
# Find all Tesla vehicles

all_tesla = df[df['Make']== 'TESLA'] 



# Find all Battery Electric Vehicles (BEV) with range > 200 miles

bev_range = df[df['Electric Range'] > 200]

# correct answer

bev_range1 = df[(df['Electric Vehicle Type'] == 'Battery Electric Vehicle (BEV)') & 
               (df['Electric Range'] > 200)]

# Find all vehicles in King County
king_county = df[df['County'] == 'King']
# Find vehicles manufactured in 2023 or later
_2023_or_later = df[df['Model Year'] >= 2023]
# Find vehicles that are "Clean Alternative Fuel Vehicle Eligible

clean = df[df['Clean Alternative Fuel Vehicle (CAFV) Eligibility'] == 'Clean Alternative Fuel Vehicle Eligible']

print(_2023_or_later)