import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv('train.csv')



df['date'] = pd.to_datetime(df['date'])

print(df.dtypes)

print(df['sales'].mean())
print(df['sales'].max())
print(df['sales'].min())

print(df.head(5))



print(df.groupby('store_nbr')['sales'].sum().sort_values(ascending=False))


print(df.groupby('family')['sales'].sum().sort_values(ascending=False).head(5))

print(df.groupby('date')['sales'].sum().sort_index(ascending=True).head(5))

daily_sales = df.groupby('date')['sales'].sum().sort_index(ascending=True)

#plt.plot(daily_sales.index, daily_sales.values)
#.xlabel('Date')
# .ylabel('Total Sales')
# plt.title('Daily Sales Over Time')
# plt.show()

old = (df[df['date'] == '2017-01-01']['sales'].sum())  

new = (df[df['date'] == '2017-01-02']['sales'].sum())  


print(old)
print(new)


percentage_change = ((new - old) / old) * 100
print(percentage_change)

df['month'] = df['date'].dt.month

print(df.groupby('month')['sales'].sum().sort_values(ascending=False).head(12)) 


print(daily_sales.groupby(daily_sales.index.month).mean().sort_values(ascending=False).head(12))

df['day_of_week'] = df['date'].dt.dayofweek

print(daily_sales.groupby(daily_sales.index.dayofweek).mean().sort_values(ascending=False))