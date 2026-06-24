from pathlib import Path

import kagglehub
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.dates import DateFormatter


path = kagglehub.dataset_download("tunguz/online-retail")

print("Path to dataset files:", path)

dataset_folder = Path(path)
dataset_path = list(dataset_folder.glob("*.csv"))[0]

retail_data = pd.read_csv(dataset_path, nrows=20000)

print(retail_data.shape)
print(retail_data.head())


# Exercise 1: clean basic data before plotting
retail_data["Description"] = retail_data["Description"].fillna("Unknown product")
retail_data = retail_data.dropna(subset=["CustomerID"])
retail_data = retail_data.drop_duplicates()
retail_data["InvoiceDate"] = pd.to_datetime(retail_data["InvoiceDate"])
retail_data["TotalAmount"] = retail_data["Quantity"] * retail_data["UnitPrice"]
retail_data["Year"] = retail_data["InvoiceDate"].dt.year
retail_data["Month"] = retail_data["InvoiceDate"].dt.month

print(retail_data.shape)
print(retail_data[["InvoiceDate", "Quantity", "UnitPrice", "TotalAmount"]].head())


# Exercise 2: create a folder to save the charts
output_folder = Path("outputs")
output_folder.mkdir(exist_ok=True)

print(output_folder)


# Exercise 3: make a bar chart with sales by country
sales_by_country = retail_data.groupby("Country")["TotalAmount"].sum()
sales_by_country = sales_by_country.sort_values(ascending=False).head(10)

plt.figure(figsize=(12, 6))
plt.bar(sales_by_country.index, sales_by_country.values, color="steelblue")
plt.title("Top 10 Countries by Sales")
plt.xlabel("Country")
plt.ylabel("Total Sales")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(output_folder / "country_sales_bar.png")
plt.close()


# Exercise 4: make a horizontal bar chart with top products
quantity_by_product = retail_data.groupby("StockCode")["Quantity"].sum()
top_products = quantity_by_product.sort_values(ascending=False).head(10)

plt.figure(figsize=(10, 6))
plt.barh(top_products.index.astype(str), top_products.values, color="darkseagreen")
plt.title("Top 10 Products by Quantity")
plt.xlabel("Quantity Sold")
plt.ylabel("Stock Code")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig(output_folder / "top_products_barh.png")
plt.close()


# Exercise 5: make a pie chart for sales and returns
sales_count = retail_data[retail_data["Quantity"] >= 0].shape[0]
returns_count = retail_data[retail_data["Quantity"] < 0].shape[0]

labels = ["Sales", "Returns"]
sizes = [sales_count, returns_count]
colors = ["lightgreen", "lightcoral"]

plt.figure(figsize=(7, 7))
plt.pie(sizes, labels=labels, colors=colors, autopct="%1.1f%%", startangle=140)
plt.title("Sales vs Returns")
plt.tight_layout()
plt.savefig(output_folder / "sales_returns_pie.png")
plt.close()


# Exercise 6: make a line chart with daily sales
daily_sales = retail_data.groupby(retail_data["InvoiceDate"].dt.date)["TotalAmount"].sum()
daily_sales.index = pd.to_datetime(daily_sales.index)

plt.figure(figsize=(12, 6))
plt.plot(daily_sales.index, daily_sales.values, color="purple", linestyle="-")
plt.title("Daily Sales")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(output_folder / "daily_sales_line.png")
plt.close()


# Exercise 7: use marker and DateFormatter for monthly sales
monthly_sales = retail_data.groupby(pd.Grouper(key="InvoiceDate", freq="M"))[
    "TotalAmount"
].sum()

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(monthly_sales.index, monthly_sales.values, marker="o", color="orange")
ax.set_title("Monthly Sales")
ax.set_xlabel("Month")
ax.set_ylabel("Total Sales")
ax.xaxis.set_major_formatter(DateFormatter("%b %Y"))
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(output_folder / "monthly_sales_line.png")
plt.close()


# Exercise 8: make a scatter plot with quantity and unit price
positive_sales = retail_data[
    (retail_data["Quantity"] > 0) & (retail_data["UnitPrice"] > 0)
]

plt.figure(figsize=(10, 6))
plt.scatter(
    positive_sales["Quantity"],
    positive_sales["UnitPrice"],
    color="teal",
    alpha=0.4,
)
plt.title("Quantity vs Unit Price")
plt.xlabel("Quantity")
plt.ylabel("Unit Price")
plt.xlim(0, 200)
plt.ylim(0, 50)
plt.tight_layout()
plt.savefig(output_folder / "quantity_unit_price_scatter.png")
plt.close()


# Exercise 9: make a histogram with total amount
normal_amounts = positive_sales[
    (positive_sales["TotalAmount"] > 0) & (positive_sales["TotalAmount"] <= 200)
]

plt.figure(figsize=(10, 6))
plt.hist(normal_amounts["TotalAmount"], bins=30, color="slateblue", edgecolor="black")
plt.title("Distribution of Total Amount")
plt.xlabel("Total Amount")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig(output_folder / "total_amount_histogram.png")
plt.close()


# Exercise 10: make subplots with sales and returns
sales_by_month = retail_data[retail_data["Quantity"] >= 0].groupby("Month")[
    "TotalAmount"
].sum()
returns_by_month = retail_data[retail_data["Quantity"] < 0].groupby("Month")[
    "TotalAmount"
].sum()

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].bar(sales_by_month.index, sales_by_month.values, color="mediumseagreen")
axes[0].set_title("Sales by Month")
axes[0].set_xlabel("Month")
axes[0].set_ylabel("Total Sales")

axes[1].bar(returns_by_month.index, returns_by_month.values, color="indianred")
axes[1].set_title("Returns by Month")
axes[1].set_xlabel("Month")
axes[1].set_ylabel("Return Amount")

plt.tight_layout()
plt.savefig(output_folder / "sales_returns_subplots.png")
plt.close()


# Exercise 11: print the chart files created
chart_files = list(output_folder.glob("*.png"))

for chart_file in chart_files:
    print(chart_file)
