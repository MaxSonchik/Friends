import pandas as pd
print('_____________________________')
df = pd.read_excel('Product Gallery.xlsx', sheet_name='Лист1')

print(df.head(10))
print(df.info())


# print(df.shape[0],df.shape[1])

# print("^ЗАДАНИЕ 1_________________________________________________")


# unique_cities = df['City'].unique()  
# print("Уникальные города:")
# print(unique_cities)


# print("^ ЗАДАНИЕ 2_________________________________________________")

# category_count = df['Category'].value_counts() 
# print("Количество товаров в каждой категории:")
# print(category_count)

# print("^ ЗАДАНИЕ  3_________________________________________________")


# average_units_in_stock = df['UnitsInStock'].mean()  
# print(f"Среднее количество единиц товара на складе: {average_units_in_stock}")

# print("^ ЗАДАНИЕ 4___________________________________________________")

max_price = df['UnitPrice (Products)'].max()
item = df[df['UnitPrice (Products)'] == max_price].iloc[0]
print(f"Максимальная цена товара: {max_price}")
print(item[['Product', 'Category']])
print("^ ЗАДАНИЕ 5____________________________________________________")

