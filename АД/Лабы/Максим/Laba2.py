import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('Product Gallery.xlsx')


top10 = df.groupby('Customer')['Profit'].sum().nlargest(10)


plt.figure(figsize=(10, 6))
plt.bar(top10.index, top10.values, color='skyblue')
plt.title('Топ-10 выгодных клиентов')
plt.xlabel('Клиенты')
plt.ylabel('Прибыль')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


unitCountry = df.groupby('Country')['UnitsInStock'].sum()

plt.figure(figsize=(10, 6))
plt.bar(unitCountry.index, unitCountry.values, color='orange')
plt.title('Количество единиц на складе по странам')
plt.xlabel('Страна')
plt.ylabel('Количество на складе')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

salesDiscount = df.groupby(['Category', 'Discount'])['Sales'].sum().unstack()

plt.figure(figsize=(14, 9))
salesDiscount.plot(kind='bar', stacked=True, ax=plt.gca(), colormap='coolwarm')
plt.title('Продажи по категориям товаров с учетом скидок')
plt.xlabel('Категория товара')
plt.ylabel('Продажи')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# ---- Задание 4



df['SalesEff'] = df['Profit'] / df['Quantity']
salesEff = df.groupby('Category')['SalesEff'].mean()

plt.figure(figsize=(10, 6))
plt.bar(salesEff.index, salesEff.values, color='green')
plt.title('Эффективность продаж по категориям товаров (прибыль на единицу)')
plt.xlabel('Категория товара')
plt.ylabel('Эффективность продаж (прибыль на единицу)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
