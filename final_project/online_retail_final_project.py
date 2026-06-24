from pathlib import Path

import kagglehub
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.dates import DateFormatter


path = kagglehub.dataset_download("tunguz/online-retail")
print("Path to dataset files:", path)

dataset_folder = Path(path)
dataset_path = list(dataset_folder.glob("*.csv"))[0]

retail_data = pd.read_csv(dataset_path)

print(retail_data.shape)
print(retail_data.head())
print(retail_data.info())
print(retail_data.describe())


# Step 1: clean the data with Pandas
retail_data["Description"] = retail_data["Description"].fillna("Unknown product")
retail_data = retail_data.dropna(subset=["CustomerID"])
retail_data = retail_data.drop_duplicates()

retail_data["InvoiceDate"] = pd.to_datetime(retail_data["InvoiceDate"])
retail_data["Year"] = retail_data["InvoiceDate"].dt.year
retail_data["Month"] = retail_data["InvoiceDate"].dt.month
retail_data["Day"] = retail_data["InvoiceDate"].dt.day
retail_data["TotalAmount"] = retail_data["Quantity"] * retail_data["UnitPrice"]

print(retail_data.isnull().sum())
print(retail_data.dtypes)
print(retail_data.head())


# Step 2: use NumPy arrays for basic statistics
quantities = retail_data["Quantity"].to_numpy()
prices = retail_data["UnitPrice"].to_numpy()
total_amount = retail_data["TotalAmount"].to_numpy()

positive_amounts = total_amount[total_amount > 0]
returns = quantities[quantities < 0]

print(quantities.ndim)
print(quantities.shape)
print(quantities.dtype)
print(prices.astype(np.float32).dtype)

print(np.sum(total_amount))
print(np.mean(positive_amounts))
print(np.std(positive_amounts))
print(np.min(prices))
print(np.max(prices))
print(returns.size)


# Step 3: answer business questions with Pandas
sales = retail_data[retail_data["Quantity"] > 0]
return_rows = retail_data[retail_data["Quantity"] < 0]

sales_by_country = sales.groupby("Country")["TotalAmount"].sum()
sales_by_country = sales_by_country.sort_values(ascending=False)

quantity_by_product = sales.groupby("StockCode")["Quantity"].sum()
top_products = quantity_by_product.sort_values(ascending=False).head(10)

product_descriptions = sales[["StockCode", "Description"]].drop_duplicates(
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

monthly_sales = sales.groupby(pd.Grouper(key="InvoiceDate", freq="M"))[
    "TotalAmount"
].sum()

country_product_table = pd.pivot_table(
    sales,
    values=["Quantity", "TotalAmount"],
    index=["Country", "StockCode"],
    aggfunc="sum",
)

summary = {
    "rows_after_cleaning": retail_data.shape[0],
    "sales_rows": sales.shape[0],
    "return_rows": return_rows.shape[0],
    "countries": retail_data["Country"].nunique(),
    "products": retail_data["StockCode"].nunique(),
    "total_sales": sales["TotalAmount"].sum(),
}

print(sales_by_country.head(10))
print(top_products_with_description)
print(monthly_sales.head())
print(country_product_table.head(15))
print(summary)


# Step 4: save charts with Matplotlib
output_folder = Path("final_project_outputs")
output_folder.mkdir(exist_ok=True)

plt.figure(figsize=(12, 6))
plt.bar(
    sales_by_country.head(10).index,
    sales_by_country.head(10).values,
    color="steelblue",
)
plt.title("Top 10 Countries by Sales")
plt.xlabel("Country")
plt.ylabel("Total Sales")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(output_folder / "top_countries_sales.png")
plt.close()

plt.figure(figsize=(10, 6))
plt.barh(
    top_products_with_description["StockCode"].astype(str),
    top_products_with_description["TotalQuantity"],
    color="darkseagreen",
)
plt.title("Top 10 Products by Quantity")
plt.xlabel("Quantity Sold")
plt.ylabel("Stock Code")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig(output_folder / "top_products_quantity.png")
plt.close()

labels = ["Sales", "Returns"]
sizes = [sales.shape[0], return_rows.shape[0]]

plt.figure(figsize=(7, 7))
plt.pie(
    sizes,
    labels=labels,
    colors=["lightgreen", "lightcoral"],
    autopct="%1.1f%%",
    startangle=140,
)
plt.title("Sales vs Returns")
plt.tight_layout()
plt.savefig(output_folder / "sales_vs_returns.png")
plt.close()

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(monthly_sales.index, monthly_sales.values, marker="o", color="orange")
ax.set_title("Monthly Sales")
ax.set_xlabel("Month")
ax.set_ylabel("Total Sales")
ax.xaxis.set_major_formatter(DateFormatter("%b %Y"))
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(output_folder / "monthly_sales.png")
plt.close()

normal_sales = sales[
    (sales["Quantity"] > 0)
    & (sales["UnitPrice"] > 0)
    & (sales["Quantity"] <= 200)
    & (sales["UnitPrice"] <= 50)
]

plt.figure(figsize=(10, 6))
plt.scatter(
    normal_sales["Quantity"],
    normal_sales["UnitPrice"],
    color="teal",
    alpha=0.3,
)
plt.title("Quantity vs Unit Price")
plt.xlabel("Quantity")
plt.ylabel("Unit Price")
plt.tight_layout()
plt.savefig(output_folder / "quantity_vs_unit_price.png")
plt.close()

for chart_file in output_folder.glob("*.png"):
    print(chart_file)
