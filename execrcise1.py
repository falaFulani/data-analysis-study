import pandas as pd 

df = pd.read_csv("Electric_Vehicle_Population_Data.csv")

#Display the first 10 rows
first_10_rows=df.head(10)

#Check the shape of the dataset (number of rows and columns)
shape_df = df.shape

#Display column names and their data types

colunms_names = df.columns
#Get basic statistical summary of numerical columns

stats_numeric = df.describe()
print(stats_numeric)
