import pandas as pd

df= pd.read_csv('GoogleApps.csv')

grp= df.groupby(by=['Type', 'Content Rating'])
series = grp['Size'].agg([max, min,])
print(series)
series2 = series.reset_index()
print(series2)
tbl = series.pivot_table(
    columns='Type',
    index='Content Rating',
    values='min'
)
print(tbl)

