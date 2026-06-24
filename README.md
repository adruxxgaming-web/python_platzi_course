# Python Platzi Course

This repository contains Python practice files for a data science course.

The exercises use the Online Retail dataset from Kaggle and are written as simple practice scripts, like a junior data engineer student would build while learning each library step by step.

## Current File

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
pip install kagglehub numpy pandas
```

## Run

```bash
python exercises/01_numpy_online_retail.py
```
