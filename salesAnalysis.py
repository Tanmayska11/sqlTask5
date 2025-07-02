

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#  Load the Excel file
file_path = "sales dataset.xlsx"
df = pd.read_excel(file_path, sheet_name='List of Orders')

#  data cleaning
print(df.head())
print(df.info())
print(df.describe())
print("Shape of dataset:", df.shape)
print("Null values:\n", df.isnull().sum())
print(df.columns)

# Ensure Order Date is datetime
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
df['Month'] = df['Order Date'].dt.to_period('M')

# Total Sales per Month
monthly_sales = df.groupby('Month')['Sales'].sum()
print(monthly_sales)

# Line plot: Monthly Sales
monthly_sales.plot(kind='line', marker='o', figsize=(10,5), title='Monthly Sales Trend')
plt.ylabel('Total Sales')
plt.xlabel('Month')
plt.show()

# Total Sales per Category
category_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
print(category_sales)

# Bar plot: Sales by Category
plt.figure(figsize=(8,5))
sns.barplot(x=category_sales.index, y=category_sales.values)
plt.title('Total Sales by Category')
plt.ylabel('Sales')
plt.xlabel('Category')
plt.show()

# Total Sales by Sub-Category
subcategory_sales = df.groupby('Sub-Category')['Sales'].sum().sort_values(ascending=False)
print(subcategory_sales)

# Bar plot: Sales by Sub-Category
plt.figure(figsize=(12,6))
sns.barplot(x=subcategory_sales.index, y=subcategory_sales.values)
plt.xticks(rotation=45)
plt.title('Total Sales by Sub-Category')
plt.ylabel('Sales')
plt.xlabel('Sub-Category')
plt.show()

# Top 10 Products by Sales
product_sales = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)
print(product_sales)

# Bar plot: Top 10 Products
plt.figure(figsize=(12,6))
sns.barplot(x=product_sales.index, y=product_sales.values)
plt.xticks(rotation=90)
plt.title('Top 10 Products by Sales')
plt.ylabel('Sales')
plt.xlabel('Product Name')
plt.show()

# Total Quantity Sold by Product
quantity_sold = df.groupby('Product Name')['Quantity'].sum().sort_values(ascending=False).head(10)
print(quantity_sold)

# Bar plot: Top 10 Products by Quantity
plt.figure(figsize=(12,6))
sns.barplot(x=quantity_sold.index, y=quantity_sold.values)
plt.xticks(rotation=90)
plt.title('Top 10 Products by Quantity Sold')
plt.ylabel('Quantity Sold')
plt.xlabel('Product Name')
plt.show()

# Regional Sales Analysis
region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
print(region_sales)

# Pie Chart: Sales Distribution by Region
region_sales.plot(kind='pie', autopct='%1.1f%%', figsize=(7,7), title='Sales Distribution by Region')
plt.ylabel('')
plt.show()

print("✅ Task 5 analysis completed")
