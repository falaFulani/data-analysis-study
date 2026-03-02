import pandas as pd 

df = pd.read_csv("Electric_Vehicle_Population_Data.csv")

# df.head(8)
# df.info()

# df.describe() 

df["Make"].value_counts().head(12)
df["Electric Vehicle Type"].value_counts()

df ["Model"].value_counts().head(10)
tesla_king = df[(df["Make"] == "TESLA") & (df["County"] == "King")]
print (tesla_king)