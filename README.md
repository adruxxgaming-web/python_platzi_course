# Python Platzi Course

This repository contains Python practice files for a data science course.

The exercises use the Online Retail dataset from Kaggle and are written as simple practice scripts, like a junior data engineer student would build while learning each library step by step.

## Current Files

### `exercises/01_numpy_online_retail.py`

This first document focuses on NumPy.

It practices:

- Creating NumPy arrays from DataFrame columns
- Checking array dimensions, shape, and size
- Changing data types with `astype`
- Calculating basic statistics
- Using indexing and slicing
- Filtering arrays with boolean conditions
- Creating calculated arrays
- Finding unique values
- Practicing `reshape`, `split`, `hstack`, and `vstack`
- Finding rows with the highest total amount

### `exercises/02_pandas_online_retail.py`

This second document focuses on Pandas.

It practices:

- Inspecting a DataFrame with `head`, `info`, `describe`, columns, and dtypes
- Selecting one column and multiple columns
- Using `loc` and `iloc`
- Checking missing values
- Filling missing descriptions and dropping rows without customer IDs
- Checking and removing duplicates
- Filtering sales, returns, and expensive products
- Creating a `TotalAmount` column
- Converting dates with `pd.to_datetime`
- Creating year, month, and day columns
- Grouping sales by country
- Grouping quantity by product
- Creating a pivot table
- Merging top products with their descriptions
- Creating a simple summary dictionary

### `exercises/03_matplotlib_online_retail.py`

This third document focuses on Matplotlib.

It practices:

- Preparing retail data before plotting
- Saving charts into an `outputs` folder
- Creating vertical bar charts
- Creating horizontal bar charts
- Creating pie charts
- Creating line charts
- Using markers and date formatting
- Creating scatter plots
- Creating histograms
- Creating subplots
- Printing the chart files created

## Repository Structure

```text
exercises/
  Course practice files by topic.

final_project/
  Final project files that will combine the course libraries.
```

## Dataset

The script downloads the dataset with KaggleHub:

```python
import kagglehub

path = kagglehub.dataset_download("tunguz/online-retail")
```

## Requirements

Install the required libraries:

```bash
pip install kagglehub numpy pandas matplotlib
```

## Run

```bash
python exercises/01_numpy_online_retail.py
python exercises/02_pandas_online_retail.py
python exercises/03_matplotlib_online_retail.py
```
