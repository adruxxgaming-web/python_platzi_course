from pathlib import Path

import kagglehub
import pandas as pd


path = kagglehub.dataset_download("tunguz/online-retail")

print("Path to dataset files:", path)

dataset_folder = Path(path)
dataset_path = list(dataset_folder.glob("*.csv"))[0]

retail_data = pd.read_csv(dataset_path, nrows=10000)

print(retail_data.shape)
print(retail_data.head())


# Exercise 1: inspect the DataFrame
print(retail_data.info())
print(retail_data.describe())
print(retail_data.columns)
print(retail_data.dtypes)


# Exercise 2: select one column and multiple columns
descriptions = retail_data["Description"]
basic_columns = retail_data[["InvoiceNo", "StockCode", "Quantity", "UnitPrice"]]

print(descriptions.head())
print(basic_columns.head())


# Exercise 3: use loc to select rows and columns by label
quantity_price = retail_data.loc[:, ["Quantity", "UnitPrice"]]
first_rows_with_country = retail_data.loc[0:10, ["InvoiceNo", "Country"]]

print(quantity_price.head())
print(first_rows_with_country)


# Exercise 4: use iloc to select rows and columns by position
first_five_rows = retail_data.iloc[0:5, :]
first_three_columns = retail_data.iloc[:, 0:3]
small_table = retail_data.iloc[0:10, [1, 2, 3, 5]]

print(first_five_rows)
print(first_three_columns.head())
print(small_table)


# Exercise 5: check missing values
missing_values = retail_data.isnull().sum()
rows_with_missing_customer = retail_data[retail_data["CustomerID"].isnull()]

print(missing_values)
print(rows_with_missing_customer.head())


# Exercise 6: fill missing descriptions and drop rows without CustomerID
retail_data["Description"] = retail_data["Description"].fillna("Unknown product")
retail_data_clean = retail_data.dropna(subset=["CustomerID"])

print(retail_data["Description"].isnull().sum())
print(retail_data_clean.shape)


# Exercise 7: check and remove duplicates
duplicate_rows = retail_data_clean.duplicated().sum()
retail_data_clean = retail_data_clean.drop_duplicates()

print(duplicate_rows)
print(retail_data_clean.shape)


# Exercise 8: filter sales, returns, and expensive products
sales = retail_data_clean[retail_data_clean["Quantity"] > 0]
returns = retail_data_clean[retail_data_clean["Quantity"] < 0]
expensive_products = retail_data_clean[retail_data_clean["UnitPrice"] > 10]

print(sales.head())
print(returns.head())
print(expensive_products.head())


# Exercise 9: create a total amount column
retail_data_clean["TotalAmount"] = (
    retail_data_clean["Quantity"] * retail_data_clean["UnitPrice"]
)

print(retail_data_clean[["Quantity", "UnitPrice", "TotalAmount"]].head())


# Exercise 10: convert InvoiceDate to datetime and create date columns
retail_data_clean["InvoiceDate"] = pd.to_datetime(retail_data_clean["InvoiceDate"])
retail_data_clean["Year"] = retail_data_clean["InvoiceDate"].dt.year
retail_data_clean["Month"] = retail_data_clean["InvoiceDate"].dt.month
retail_data_clean["Day"] = retail_data_clean["InvoiceDate"].dt.day

print(retail_data_clean[["InvoiceDate", "Year", "Month", "Day"]].head())
print(retail_data_clean.dtypes)


# Exercise 11: group sales by country
sales_by_country = retail_data_clean.groupby("Country")["TotalAmount"].sum()
sales_by_country = sales_by_country.sort_values(ascending=False)

print(sales_by_country.head(10))


# Exercise 12: group quantity by product
quantity_by_product = retail_data_clean.groupby("StockCode")["Quantity"].sum()
top_products = quantity_by_product.sort_values(ascending=False).head(10)

print(top_products)


# Exercise 13: create a pivot table by country and product
country_product_table = pd.pivot_table(
    retail_data_clean,
    values=["Quantity", "TotalAmount"],
    index=["Country", "StockCode"],
    aggfunc="sum",
)

print(country_product_table.head(15))


# Exercise 14: merge the top products with their descriptions
product_descriptions = retail_data_clean[["StockCode", "Description"]].drop_duplicates(
    subset="StockCode"
)
top_products_df = top_products.reset_index()
top_products_df = top_products_df.rename(columns={"Quantity": "TotalQuantity"})

top_products_with_description = pd.merge(
    top_products_df,
    product_descriptions,
    on="StockCode",
    how="left",
)

print(top_products_with_description)


# Exercise 15: make a simple final summary with Pandas
summary = {
    "rows": retail_data_clean.shape[0],
    "columns": retail_data_clean.shape[1],
    "countries": retail_data_clean["Country"].nunique(),
    "products": retail_data_clean["StockCode"].nunique(),
    "total_sales": retail_data_clean["TotalAmount"].sum(),
}

print(summary)
