import pandas as pd
import numpy as np
import re

INPUT_FILE = "raw_dataset.csv"
OUTPUT_FILE = "cleaned_dataset.csv"

df = pd.read_csv(INPUT_FILE)

print("Original shape:", df.shape)

# Remove duplicates
print("Duplicate rows:", df.duplicated().sum())
df = df.drop_duplicates().copy()

# Standardize text
df["Name"] = df["Name"].astype(str).str.strip().str.title()
df["City"] = df["City"].astype(str).str.strip().str.title()

df["Gender"] = (
    df["Gender"].astype(str).str.strip().str.lower()
    .replace({"m": "Male", "male": "Male", "f": "Female", "female": "Female"})
)

# Convert numeric columns
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
df["Salary"] = pd.to_numeric(df["Salary"], errors="coerce")

# Validate age
df.loc[(df["Age"] < 18) | (df["Age"] > 100), "Age"] = np.nan

# Validate email
email_pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
df.loc[~df["Email"].astype(str).str.match(email_pattern, na=False), "Email"] = np.nan

# Standardize dates
df["Join_Date"] = pd.to_datetime(df["Join_Date"], errors="coerce")
df["Join_Date"] = df["Join_Date"].fillna(pd.Timestamp("2026-02-01"))

# Fill missing values
df["Age"] = df["Age"].fillna(df["Age"].median()).round().astype(int)
df["Salary"] = df["Salary"].fillna(df["Salary"].median())
df["Email"] = df["Email"].fillna("unknown@example.com")
df["Gender"] = df["Gender"].fillna("Unknown")
df["Active"] = df["Active"].replace("", np.nan).fillna("Unknown")

# Final date format
df["Join_Date"] = df["Join_Date"].dt.strftime("%Y-%m-%d")

# Save cleaned data
df.to_csv(OUTPUT_FILE, index=False)

print("Cleaned shape:", df.shape)
print("Saved:", OUTPUT_FILE)
print("\nMissing values after cleaning:")
print(df.isnull().sum())
