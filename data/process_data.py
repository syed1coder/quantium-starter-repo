import pandas as pd
import os

# Define folder path
folder_path = "data"

# Get all CSV files in the folder
file_names = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

# Read and concatenate all CSVs
dfs = [pd.read_csv(os.path.join(folder_path, file)) for file in file_names]
df = pd.concat(dfs, ignore_index=True)

# ✅ Filter only Pink Morsels
df = df[df["product"] == "pink morsel"]

# ✅ Convert price to numeric (remove $ symbol)
df["price"] = df["price"].replace("[\$,]", "", regex=True).astype(float)

# ✅ Compute total sales
df["sales"] = df["price"] * df["quantity"]

# ✅ Keep only required columns
df = df[["sales", "date", "region"]]

# ✅ Save cleaned data
df.to_csv("data/processed_data.csv", index=False)
print("✅ Processed data saved successfully!")
