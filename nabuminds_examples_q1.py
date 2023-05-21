#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np

np.random.seed(42)  # For reproducibility

# Generate dummy data for NDCs
n_samples = 1000

acquisition_channels = ["Affiliate", "Search Ads", "Social Media"]
markets = ["Market A", "Market B", "Market C"]
churn_status = [0, 1]  # 0 = not churned, 1 = churned
brands = ["Brand X", "Brand Y", "Brand Z"]

data = {
    "NDC_ID": np.random.choice([1, 2, 3, 4, 5], size=n_samples),
    "Acquisition_Channel": np.random.choice(acquisition_channels, n_samples),
    "Market": np.random.choice(markets, n_samples),
    "Brand": np.random.choice(brands, n_samples),
    "Turnover": np.random.uniform(100, 1000, n_samples),
    "Revenue": np.random.uniform(50, 500, n_samples),
    "Bonus_Cost": np.random.uniform(10, 100, n_samples),
    "Churn": np.random.choice(churn_status, n_samples, p=[0.8, 0.2])
}

df = pd.DataFrame(data)
print(df)

# Question_1
# Calculate CLV and ARPU by acquisition channel, brand, and market
clv_by_channel_brand_market = df.groupby(["Acquisition_Channel", "Brand", "Market"]).agg({
    "Turnover": "sum",
    "Revenue": "sum",
    "NDC_ID": "count"
})

clv_by_channel_brand_market["CLV"] = clv_by_channel_brand_market["Revenue"] / clv_by_channel_brand_market["NDC_ID"]
clv_by_channel_brand_market["ARPU"] = clv_by_channel_brand_market["Revenue"] / clv_by_channel_brand_market["Turnover"]

# Identify the acquisition channel, brand, and market combination with the highest CLV and ARPU
most_profitable_combination_clv = clv_by_channel_brand_market["CLV"].idxmax()
most_profitable_combination_arpu = clv_by_channel_brand_market["ARPU"].idxmax()

# Print the result
print("Most profitable acquisition channel, brand, and market combination (CLV):", most_profitable_combination_clv)
print("Most profitable acquisition channel, brand, and market combination (ARPU):", most_profitable_combination_arpu)
print(clv_by_channel_brand_market)


# In[ ]:





# In[ ]:




