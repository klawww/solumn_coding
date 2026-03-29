import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("bmw_global_sales_2018_2025.csv")

# Clean data (important for interview signal)
df = df.dropna(subset=["Units_Sold", "Avg_Price_EUR", "GDP_Growth"])
df = df[(df["Units_Sold"] > 0) & (df["Avg_Price_EUR"] > 0)]

# Add log columns
df["log_units"] = np.log(df["Units_Sold"])
df["log_price"] = np.log(df["Avg_Price_EUR"])

# ---- Step 1: Elasticity per model ----
elasticity_results = []

for model, g in df.groupby("Model"):
    if len(g) < 10:
        continue  # avoid noisy small samples

    slope = np.polyfit(g["log_price"], g["log_units"], 1)[0]

    elasticity_results.append({
        "Model": model,
        "Elasticity": slope,
        "Samples": len(g)
    })

elasticity_df = pd.DataFrame(elasticity_results)

# Sort by most elastic (most negative)
elasticity_df = elasticity_df.sort_values("Elasticity")

print("\nTop elastic models (most price sensitive):")
print(elasticity_df.head(10))

print("\nLeast elastic / premium models:")
print(elasticity_df.tail(10))


# GDP buckets
def gdp_bucket(x):
    if x < 1:
        return "Low"
    elif x < 3:
        return "Medium"
    else:
        return "High"

df["GDP_Bucket"] = df["GDP_Growth"].apply(gdp_bucket)

elasticity_gdp = []

for (model, bucket), g in df.groupby(["Model", "GDP_Bucket"]):
    if len(g) < 8:
        continue

    slope = np.polyfit(g["log_price"], g["log_units"], 1)[0]

    elasticity_gdp.append({
        "Model": model,
        "GDP_Bucket": bucket,
        "Elasticity": slope,
        "Samples": len(g)
    })

elasticity_gdp_df = pd.DataFrame(elasticity_gdp)

print("\nElasticity by GDP condition:")
print(elasticity_gdp_df.head(20))

top_models = elasticity_df.head(5)["Model"].tolist()

for model in top_models:
    g = df[df["Model"] == model]

    plt.figure(figsize=(6,4))
    plt.scatter(g["Avg_Price_EUR"], g["Units_Sold"])

    plt.title(f"{model}: Price vs Units")
    plt.xlabel("Avg Price EUR")
    plt.ylabel("Units Sold")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()