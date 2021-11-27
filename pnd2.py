import pandas as pd

df= pd.read_csv('GooglePlayStore_wild.csv')

df= df['Price']

print(df)
exit()
df.dropna(inplace=True)

df.info()
def m(v):
    v= v.replace()
    return float(v)

df['Price']= df['Price'].apply(m)
av= df['Rating'].mean()

df['Rating'].fillna(av, inplace=True)

ftr= df[pd.isnull(df['Rating'])]
print(ftr.head())

df.info()

