import pandas as pd 

data = {
    'product': ['Mango', 'Avocado', 'Passion', 'Banana', 'Pineapple'],
    'price': [120, 45, 80, 15, 180],
    'stock': [22, 48, 9, 150, 14],
    'organic': [True, True, False, False, True]
}

df = pd.DataFrame(data)

filtered_more_100 = df[df['price']>100]

organic_product = df[df['organic']== True]
not_organic_stock_less_50 = df[(df['organic']== False)& (df['stock'] < 50)]

df['total_value'] = df['price'] * df['stock']

df['expensive'] = df ['price']>= 100
df['category'] = 'premium'
df.loc[(df['price'] >= 50) & (df['price'] < 150), 'category'] = 'medium'
df.loc[df['price'] < 50, 'category'] = 'cheap'
# df['category'] = 'premium'

# df.loc[df['price']>= 150,'category'] = 'premium'


print(df)