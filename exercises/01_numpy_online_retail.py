from pathlib import Path

import kagglehub
import numpy as np
import pandas as pd


path = kagglehub.dataset_download("tunguz/online-retail")

print("Path to dataset files:", path)

dataset_folder = Path(path)
dataset_path = list(dataset_folder.glob("*.csv"))[0]

retail_data = pd.read_csv(dataset_path, nrows=5000)

print(retail_data.shape)
print(retail_data.head())


# Exercise 1: create NumPy arrays from DataFrame columns
quantities = retail_data["Quantity"].to_numpy()
prices = retail_data["UnitPrice"].to_numpy()

print(quantities[:10])
print(prices[:10])
print(type(quantities))
print(prices.dtype)


# Exercise 2: check the dimensions, shape, and size of an array
numeric_data = retail_data[["Quantity", "UnitPrice"]].to_numpy()

print(numeric_data.ndim)
print(numeric_data.shape)
print(numeric_data.size)
print(numeric_data[:5])


# Exercise 3: change data types with astype
quantities_float = quantities.astype(np.float64)
prices_float32 = prices.astype(np.float32)

print(quantities.dtype)
print(quantities_float.dtype)
print(prices_float32.dtype)


# Exercise 4: calculate basic statistics
print(np.sum(quantities))
print(np.mean(quantities))
print(np.std(quantities))
print(np.min(prices))
print(np.max(prices))


# Exercise 5: use indexing and slicing
print(quantities[0])
print(quantities[4])
print(quantities[-1])
print(quantities[:10])
print(quantities[10:21])
print(quantities[:20:2])


# Exercise 6: filter data with boolean conditions
positive_quantities = quantities[quantities > 0]
expensive_prices = prices[prices > 10]
returns = quantities[quantities < 0]

print(positive_quantities.size)
print(expensive_prices.size)
print(returns.size)
print(returns[:10])


# Exercise 7: calculate the total amount per row using NumPy
total_amount = quantities * prices

print(total_amount[:10])
print(np.sum(total_amount))
print(np.mean(total_amount))


# Exercise 8: get unique values
countries = retail_data["Country"].to_numpy()
stock_codes = retail_data["StockCode"].to_numpy()

unique_countries = np.unique(countries)
unique_products = np.unique(stock_codes)

print(unique_countries)
print(unique_products.size)


# Exercise 9: practice reshape, split, hstack, and vstack
small_quantities = quantities[:12]
small_prices = prices[:12]

matrix_quantities = small_quantities.reshape(3, 4)
split_quantities = np.split(small_quantities, 3)
horizontal_array = np.hstack((small_quantities[:4], small_prices[:4]))
vertical_array = np.vstack((small_quantities[:4], small_prices[:4]))

print(small_quantities)
print(matrix_quantities)
print(split_quantities)
print(horizontal_array)
print(vertical_array)


# Exercise 10: find the 5 rows with the highest total amount
top_positions = np.argsort(total_amount)[-5:][::-1]

for position in top_positions:
    print(
        stock_codes[position],
        quantities[position],
        prices[position],
        round(total_amount[position], 2),
    )
