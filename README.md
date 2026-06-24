# Python Platzi Course

This repository contains Python practice files for a data science course.

The exercises use the Online Retail dataset from Kaggle and are written as simple practice scripts, like a junior data engineer student would build while learning each library step by step.

## Current Files

### `exercises/01_numpy_online_retail.py`

This first document focuses on NumPy using real columns from the Online Retail dataset. It practices creating arrays from Pandas columns, checking dimensions, shape, size, and data types, converting values with `astype`, calculating basic statistics, using indexing and slicing, filtering with boolean conditions, creating calculated arrays, finding unique values, using `reshape`, `split`, `hstack`, and `vstack`, and finding the rows with the highest total amount.

### `exercises/02_pandas_online_retail.py`

This second document focuses on Pandas for DataFrame work. It practices inspecting data with `head`, `info`, `describe`, columns, and dtypes, selecting columns, using `loc` and `iloc`, checking missing values, filling missing descriptions, dropping rows without customer IDs, removing duplicates, filtering sales and returns, creating a `TotalAmount` column, converting dates with `pd.to_datetime`, creating year, month, and day columns, grouping sales by country and product, building a pivot table, merging product descriptions, and creating a small summary dictionary.

### `exercises/03_matplotlib_online_retail.py`

This third document focuses on Matplotlib for basic data visualization. It prepares the retail data before plotting, saves charts into an `outputs` folder, and creates vertical bar charts, horizontal bar charts, pie charts, line charts, scatter plots, histograms, and subplots. It also practices using markers, formatting dates on the x-axis, adjusting labels and titles, rotating ticks, applying `tight_layout`, saving figures with `savefig`, closing plots, and printing the chart files that were created.

### `final_project/online_retail_final_project.py`

This final project combines the course libraries in one script without adding topics outside the course. It uses KaggleHub to download the Online Retail dataset, Pandas to inspect, clean, filter, group, pivot, and merge data, NumPy to work with arrays and basic statistics, and Matplotlib to save charts about sales, returns, products, countries, and monthly results. The project keeps the code compact and saves chart images into `final_project_outputs/` when it runs.

## Certification

The course diploma is included here:

```text
certification/diploma-python-data-science.pdf
```

## Repository Structure

```text
exercises/
  Course practice files by topic.

final_project/
  Final project files that will combine the course libraries.

certification/
  Course diploma.
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
python final_project/online_retail_final_project.py
```
