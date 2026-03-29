import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("bmw_global_sales_2018_2025.csv")

# Basic check
print(df.head())
print(df.shape)
print(df.columns.tolist())

# Aggregate to yearly regional level
year_region = (
    df.groupby(["Year", "Region"], as_index=False)
      .agg(
          Units_Sold=("Units_Sold", "sum"),
          Revenue_EUR=("Revenue_EUR", "sum"),
          BEV_Share=("BEV_Share", "mean"),
          GDP_Growth=("GDP_Growth", "mean"),
          Fuel_Price_Index=("Fuel_Price_Index", "mean")
      )
      .sort_values(["Region", "Year"])
)

print("\nYear-Region aggregated data:")
print(year_region.head(12))

# Correlation + transition summary
rows = []

for region, g in year_region.groupby("Region"):
    g = g.sort_values("Year").reset_index(drop=True)

    corr_units = g["BEV_Share"].corr(g["Units_Sold"])
    corr_revenue = g["BEV_Share"].corr(g["Revenue_EUR"])

    bev_start = g.loc[0, "BEV_Share"]
    bev_end = g.loc[len(g) - 1, "BEV_Share"]
    bev_increase = bev_end - bev_start

    units_start = g.loc[0, "Units_Sold"]
    units_end = g.loc[len(g) - 1, "Units_Sold"]
    units_growth_pct = (units_end - units_start) / units_start

    rev_start = g.loc[0, "Revenue_EUR"]
    rev_end = g.loc[len(g) - 1, "Revenue_EUR"]
    rev_growth_pct = (rev_end - rev_start) / rev_start

    rows.append({
        "Region": region,
        "corr_BEV_vs_Units": corr_units,
        "corr_BEV_vs_Revenue": corr_revenue,
        "BEV_2018": bev_start,
        "BEV_2025": bev_end,
        "BEV_Increase": bev_increase,
        "Units_Growth_Pct": units_growth_pct,
        "Revenue_Growth_Pct": rev_growth_pct
    })

summary_qA = pd.DataFrame(rows).sort_values("BEV_Increase", ascending=False)

print("\nQuestion A summary:")
print(summary_qA.to_string(index=False))

# Optional: prettier formatting
summary_fmt = summary_qA.copy()
for col in ["corr_BEV_vs_Units", "corr_BEV_vs_Revenue", "BEV_2018", "BEV_2025", "BEV_Increase"]:
    summary_fmt[col] = summary_fmt[col].map(lambda x: round(x, 4))
for col in ["Units_Growth_Pct", "Revenue_Growth_Pct"]:
    summary_fmt[col] = summary_fmt[col].map(lambda x: f"{x:.2%}")

print("\nFormatted summary:")
print(summary_fmt.to_string(index=False))

# ---------- Visualisations ----------
# 1) BEV share trend by region
plt.figure(figsize=(10, 6))
for region, g in year_region.groupby("Region"):
    plt.plot(g["Year"], g["BEV_Share"], marker="o", label=region)

plt.title("BEV Share Trend by Region (2018-2025)")
plt.xlabel("Year")
plt.ylabel("Average BEV Share")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# 2) Units sold trend by region
plt.figure(figsize=(10, 6))
for region, g in year_region.groupby("Region"):
    plt.plot(g["Year"], g["Units_Sold"], marker="o", label=region)

plt.title("Units Sold by Region (2018-2025)")
plt.xlabel("Year")
plt.ylabel("Units Sold")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# 3) Revenue trend by region
plt.figure(figsize=(10, 6))
for region, g in year_region.groupby("Region"):
    plt.plot(g["Year"], g["Revenue_EUR"], marker="o", label=region)

plt.title("Revenue by Region (2018-2025)")
plt.xlabel("Year")
plt.ylabel("Revenue (EUR)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# 4) Scatter plots: BEV vs Units, BEV vs Revenue
for region, g in year_region.groupby("Region"):
    plt.figure(figsize=(6, 4))
    plt.scatter(g["BEV_Share"], g["Units_Sold"])
    for _, row in g.iterrows():
        plt.annotate(int(row["Year"]), (row["BEV_Share"], row["Units_Sold"]))
    plt.title(f"BEV Share vs Units Sold - {region}")
    plt.xlabel("BEV Share")
    plt.ylabel("Units Sold")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

for region, g in year_region.groupby("Region"):
    plt.figure(figsize=(6, 4))
    plt.scatter(g["BEV_Share"], g["Revenue_EUR"])
    for _, row in g.iterrows():
        plt.annotate(int(row["Year"]), (row["BEV_Share"], row["Revenue_EUR"]))
    plt.title(f"BEV Share vs Revenue - {region}")
    plt.xlabel("BEV Share")
    plt.ylabel("Revenue (EUR)")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()