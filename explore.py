import requests
import pandas as pd
from extract import extract


df = extract()

# Briefly look at the data
print(df.shape)
print(df.head())
print("---")

# What columns exist and what type is each?
print(df.dtypes)
print("---")

# Are there any missing values?
print(df.isnull().sum())
print("---")

# What are the unique values in categorical columns?
print(df["Rndrng_Prvdr_Type"].value_counts())
print("---")

