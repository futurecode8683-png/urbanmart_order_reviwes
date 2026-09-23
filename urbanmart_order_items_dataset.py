import pandas as pd
import numpy as np

df = pd.read_csv(
    r"E:\New folder\olist_order_items_dataset.xlsx",
    sep="\t"
)


# First 5 rows
print(df.head())

# Last 5 rows
print(df.tail())

# Dataset rows and columns
print(df.shape)

# Column names
print(df.columns)

# Data types and non-null counts
print(df.info())

# Statistical summary
print(df.describe())




# Missing values in each column
print(df.isnull().sum())

# Total missing values
print(df.isnull().sum().sum())

# Missing value percentage
missing_percent = (df.isnull().sum() / len(df)) * 100

print(missing_percent)



# Exact duplicate rows
print("Duplicate Rows:", df.duplicated().sum())

# Duplicate order-item combinations
print(
    "Duplicate Order-Item Keys:",
    df.duplicated(
        subset=["order_id", "order_item_id"]
    ).sum()
)




# Check data types
print(df.dtypes)

# Convert shipping limit date to datetime
df["shipping_limit_date"] = pd.to_datetime(
    df["shipping_limit_date"],
    errors="coerce"
)

# Check data types again
print(df.dtypes)



# Negative prices
print("Negative Prices:", (df["price"] < 0).sum())

# Negative freight values
print(
    "Negative Freight:",
    (df["freight_value"] < 0).sum()
)

# Zero prices
print("Zero Prices:", (df["price"] == 0).sum())

# Zero freight
print(
    "Zero Freight:",
    (df["freight_value"] == 0).sum()
)



total_records = len(df)

unique_orders = df["order_id"].nunique()

unique_products = df["product_id"].nunique()

unique_sellers = df["seller_id"].nunique()

total_item_sales = df["price"].sum()

total_freight = df["freight_value"].sum()

average_item_price = df["price"].mean()

average_freight = df["freight_value"].mean()

print("Total Records:", total_records)
print("Unique Orders:", unique_orders)
print("Unique Products:", unique_products)
print("Unique Sellers:", unique_sellers)
print("Total Item Sales:", round(total_item_sales, 2))
print("Total Freight:", round(total_freight, 2))
print("Average Item Price:", round(average_item_price, 2))
print("Average Freight:", round(average_freight, 2))



order_sales = df.groupby("order_id")["price"].sum()

aov = order_sales.mean()

print("Average Order Value:", round(aov, 2))



top_products = (
    df.groupby("product_id")["price"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_products)



top_sellers = (
    df.groupby("seller_id")["price"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_sellers)




df["price_category"] = pd.cut(
    df["price"],
    bins=[-1, 50, 100, 500, float("inf")],
    labels=["Low", "Medium", "High", "Premium"]
)

price_analysis = df.groupby(
    "price_category",
    observed=False
).agg(
    total_items=("order_item_id", "count"),
    total_sales=("price", "sum")
)

print(price_analysis)




