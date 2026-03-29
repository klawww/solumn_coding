import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("bmw_global_sales_2018_2025.csv")

# Clean
df = df.dropna(subset=["Units_Sold", "Revenue_EUR", "GDP_Growth", "Fuel_Price_Index"])

# ---- Global monthly aggregation ----
monthly = (
    df.groupby("Month", as_index=False)
      .agg(
          Units_Sold=("Units_Sold", "mean"),
          Revenue_EUR=("Revenue_EUR", "mean"),
          GDP_Growth=("GDP_Growth", "mean"),
          Fuel_Price_Index=("Fuel_Price_Index", "mean")
      )
      .sort_values("Month")
)

print("\nMonthly patterns:")
print(monthly)

plt.figure(figsize=(10,5))
plt.plot(monthly["Month"], monthly["Units_Sold"], marker="o")
plt.title("Seasonality: Units Sold by Month")
plt.xlabel("Month")
plt.ylabel("Units Sold (avg)")
plt.grid(True, alpha=0.3)
plt.show()

plt.figure(figsize=(10,5))
plt.plot(monthly["Month"], monthly["Revenue_EUR"], marker="o")
plt.title("Seasonality: Revenue by Month")
plt.xlabel("Month")
plt.ylabel("Revenue (avg)")
plt.grid(True, alpha=0.3)
plt.show()

monthly_region = (
    df.groupby(["Month", "Region"], as_index=False)
      .agg(
          Units_Sold=("Units_Sold", "mean"),
          Revenue_EUR=("Revenue_EUR", "mean")
      )
)

for region, g in monthly_region.groupby("Region"):
    plt.figure(figsize=(8,4))
    plt.plot(g["Month"], g["Units_Sold"], marker="o")
    plt.title(f"{region}: Units Sold Seasonality")
    plt.xlabel("Month")
    plt.ylabel("Units Sold")
    plt.grid(True, alpha=0.3)
    plt.show()

# GDP buckets
def gdp_bucket(x):
    if x < 1:
        return "Low"
    elif x < 3:
        return "Medium"
    else:
        return "High"

# Fuel price buckets
def fuel_bucket(x):
    if x < df["Fuel_Price_Index"].quantile(0.33):
        return "Low"
    elif x < df["Fuel_Price_Index"].quantile(0.66):
        return "Medium"
    else:
        return "High"

df["GDP_Bucket"] = df["GDP_Growth"].apply(gdp_bucket)
df["Fuel_Bucket"] = df["Fuel_Price_Index"].apply(fuel_bucket)

monthly_gdp = (
    df.groupby(["Month", "GDP_Bucket"], as_index=False)
      .agg(
          Units_Sold=("Units_Sold", "mean"),
          Revenue_EUR=("Revenue_EUR", "mean")
      )
)

for bucket, g in monthly_gdp.groupby("GDP_Bucket"):
    plt.figure(figsize=(8,4))
    plt.plot(g["Month"], g["Units_Sold"], marker="o")
    plt.title(f"Units Seasonality under GDP={bucket}")
    plt.xlabel("Month")
    plt.ylabel("Units Sold")
    plt.grid(True, alpha=0.3)
    plt.show()

monthly_fuel = (
    df.groupby(["Month", "Fuel_Bucket"], as_index=False)
      .agg(
          Units_Sold=("Units_Sold", "mean"),
          Revenue_EUR=("Revenue_EUR", "mean")
      )
)

for bucket, g in monthly_fuel.groupby("Fuel_Bucket"):
    plt.figure(figsize=(8,4))
    plt.plot(g["Month"], g["Units_Sold"], marker="o")
    plt.title(f"Units Seasonality under Fuel={bucket}")
    plt.xlabel("Month")
    plt.ylabel("Units Sold")
    plt.grid(True, alpha=0.3)
    plt.show()