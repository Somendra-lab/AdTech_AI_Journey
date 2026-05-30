import pandas as pd

# Load dataset
data = pd.read_csv("datasets/ads.csv")

# Create new metrics
data["CTR"] = (data["Clicks"] / data["Impressions"]) * 100
data["CPC"] = data["Cost"] / data["Clicks"]

# Best campaign by CTR
best_ctr = data.loc[data["CTR"].idxmax()]

# Output
print("\n=== Ad Campaign Analysis ===\n")
print(data)

print("\nBest Campaign Based on CTR:")
print(best_ctr)