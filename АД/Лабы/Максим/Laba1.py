import pandas as pd
import matplotlib.pyplot as plt
print('_____________________________')
df = pd.read_excel('Product Gallery.xlsx', sheet_name='Лист1')

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

