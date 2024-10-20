import pandas as pd
import matplotlib.pyplot as plt
print('_____________________________')





df = pd.read_excel('Product Gallery.xlsx', sheet_name='Лист1')


print([f"'{col}'" for col in df.columns])


print(df.head(10))
print(df.info())


print(df.shape[0],df.shape[1])


print("^ЗАДАНИЕ 1_________________________________________________")


unique_cities = df['City'].unique()  
print("Уникальные города:")
print(unique_cities)



print("^ ЗАДАНИЕ 2_________________________________________________")

category_count = df['Category'].value_counts() 
print("Количество товаров в каждой категории:")
print(category_count)


print("^ ЗАДАНИЕ  3_________________________________________________")


average_units_in_stock = df['UnitsInStock'].mean()  
print(f"Среднее количество единиц товара на складе: {average_units_in_stock}")


print("^ ЗАДАНИЕ 4___________________________________________________")

max_price = df['UnitPrice (Products)'].max()
item = df[df['UnitPrice (Products)'] == max_price].iloc[0]
print(f"Максимальная цена товара: {max_price}")
print(item[['Product', 'Category']])


print("^ ЗАДАНИЕ 5____________________________________________________")

country_profit=df.groupby('Country')['Profit'].sum()
print(country_profit)

print("^ ЗАДАНИЕ 6 _____________________________________________________")

sales=df.groupby('Country')["Sales"].sum()

sales.plot(kind="bar")
plt.title('Продажи по странам')
plt.xlabel('Country')
plt.ylabel('Sales')
#plt.show()!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Раскоментить для графика


print("^ ЗАДАНИЕ 7 _____________________________________")


uniq_CityAnd_country = df['City and Counry'].unique()
print(uniq_CityAnd_country)


print("^^^ ЗАДАНИЕ 8__________________________________________________________")

avg_cost=df.groupby('Category')['UnitCost'].mean()
print(avg_cost)


print("^^^ ЗАДАНИЕ 9 _______________________________________")

top3=df.groupby('Customer Company')['Profit'].sum().nlargest(3)
print(top3)

print("^^^ ЗАДАНИЕ 10 ___________________________________")


unit30=df[df['Quantity']>30]
print(unit30['Quantity'])

print("^^^ ЗАДАНИЕ 11________________________________________________")

top5 = df[['Product','UnitsOnOrder']].nlargest(5,'UnitsOnOrder')
print(top5)

print("^^^ЗАДАНИЕ 12______________________________________________")

salesCustomer = df.groupby('Customer')['Quantity'].sum()
print(salesCustomer)

print("^^^ЗАДАНИЕ 13_______________________________________________")

df = df.groupby('City')['Category'].unique()
print(df)

print("^^^ ЗАДАНИЕ 14_______________________________________________")


print("^^^ ЗАДАНИЕ 14_______________________________________________")


df['Margin'] = df['UnitPrice'] - df['UnitCost']
max_marg = df.loc[df['Margin'].idxmax()]
print(max_marg)


print("^^^ ЗАДАНИЕ 15_________________________________________________")




for i in df['Category'].unique():
    i_data = df[df['Category'] == i]
    plt.scatter(i_data['Category'], i_data['Profit'], label = i)

plt.title('Прибыль vs Количество')
plt.xlabel('Количество')
plt.ylabel('Прибыль')
plt.legend()
plt.show()


print("^^^ ЗАДАНИЕ 16__________________________________________________")




CPrices = df.groupby('Customer')['UnitPrice (Products)'].agg(['mean', 'median'])

topC = CPrices['mean'].idxmax()
print(f'Самый богатый клиент: {topC}')


print("^^^ЗАДАНИЕ 17_______________________________________________________")




df['OrderDate'] = pd.to_datetime(df['OrderDate'])
df['Month'] = df['OrderDate'].dt.to_period('M')

sales = df.groupby('Month')['Sales'].sum()

sales.plot()
plt.title('Продажи по месяцам')
plt.xlabel('Месяц')
plt.ylabel('Продажи')
plt.show()

print("^^^ЗАДАНИЕ 18_____________________________________________________")


companyCust = df.groupby('Customer Company')['Customer'].nunique()
companyCust = companyCust.sort_values(ascending=False)
print(companyCust)
topComp = companyCust.head(1)
print(f"Компания с наибольшим количеством различных клиентов: {topComp}")

print("^^^ЗАДАНИЕ 19_____________________________________________________")



top_sales = df.loc[df.groupby('Category')['Sales'].idxmax()]

print(top_sales[['Product', 'Category', 'Sales']])



print("^^^ЗАДАНИЕ 20_____________________________________________________")





table = df.pivot_table(values='Profit', index='Category', columns='City', aggfunc='sum')
print(table)



print("^^^ЗАДАНИЕ 21_____________________________________________________")




df['OrderDate'] = pd.to_datetime(df['OrderDate'])
print(df['OrderDate'])
last_date = df['OrderDate'].max()
last_6_months = df[df['OrderDate'] >= (last_date - pd.DateOffset(months=6))]
print("Количество записей за последние 6 месяцев:", len(last_6_months))
top3 = last_6_months.groupby('City')['Sales'].sum().nlargest(3)
print(top3)

print("^^^ЗАДАНИЕ 22_____________________________________________________")




df['AvgProfit'] = df.groupby('Category')['Profit'].transform('mean')


df['DfProfit'] = df['Profit'] - df['AvgProfit']
top5 = df.nlargest(5, 'DfProfit')

print(f'Компании с наибольшей разницей: {top5}')

id = [1622, 527, 1413, 452, 436]
ch = df.loc[id]['DfProfit']
print("___________________________", ch)



print("^^^ЗАДАНИЕ 23_____________________________________________________")