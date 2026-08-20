# Project 1: Data Cleaning & Preparation

## 1. Project Objective
Clean a raw dataset by identifying and handling missing values, duplicates, incorrect data types, invalid values, inconsistent text formats, and incorrect dates.

## 2. Dataset
The dataset contains employee/student-style records with these fields:
- ID
- Name
- Email
- Age
- Gender
- Join_Date
- Salary
- City
- Active

The raw dataset was intentionally prepared with common real-world data quality problems so that the cleaning process can be demonstrated.

## 3. Problems Identified
1. Missing age and salary values.
2. Invalid age such as `twenty` and `-5`.
3. Invalid email address.
4. Missing email.
5. Duplicate record.
6. Mixed date formats such as `YYYY-MM-DD`, `DD/MM/YYYY`, `YYYY/MM/DD`, and text dates.
7. Invalid date such as `2026-02-30`.
8. Inconsistent gender values such as `Male`, `male`, `M`, `Female`, and `F`.
9. Numeric salary containing text (`abc`).

## 4. Cleaning Steps
### Step 1: Remove duplicates
Exact duplicate rows were detected and removed using pandas `drop_duplicates()`.

### Step 2: Standardize text
Names and cities were converted to title case. Gender values were standardized to `Male`, `Female`, or `Unknown`.

### Step 3: Convert numeric fields
Age and Salary were converted to numeric values using `pd.to_numeric(..., errors="coerce")`. Invalid values were converted to missing values.

### Step 4: Validate age
A reasonable age range of 18–100 was used. Values outside this range were treated as invalid.

### Step 5: Validate email
A simple email pattern was used to detect malformed email addresses.

### Step 6: Standardize dates
Mixed date formats were converted into a common `YYYY-MM-DD` format. Invalid dates were treated as missing and replaced with a project-level default date.

### Step 7: Handle missing values
- Age: median
- Salary: median
- Email: `unknown@example.com`
- Gender: `Unknown`
- Join_Date: `2026-02-01`
- Active: `Unknown`

## 5. Results
- Original rows: 26
- Duplicate rows removed: 1
- Final rows: 25
- Missing/invalid Age values handled: 3
- Missing/invalid Salary values handled: 2
- Invalid/missing Email values handled: 2
- Invalid/missing Join_Date values handled: 16

## 6. Output
The cleaned dataset is saved as `cleaned_dataset.csv`.

## 7. Tools Used
- Python
- Pandas
- NumPy
- CSV files
- Jupyter Notebook / VS Code

## 8. Conclusion
The project demonstrates how raw data can be transformed into a consistent, structured, and analysis-ready dataset. The cleaned data has standardized formats, fewer quality issues, and properly handled missing or invalid values.
