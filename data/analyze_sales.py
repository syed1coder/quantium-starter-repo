import pandas as pd

# Load processed data
df = pd.read_csv("data/processed_data.csv")

# Convert 'date' column to datetime format
df["date"] = pd.to_datetime(df["date"])

# Filter data for 'pink morsel' only
df_pink_morsel = df[df["product"] == "pink morsel"]

# Define the cutoff date
cutoff_date = pd.to_datetime("2021-01-15")

# Split data into before and after price increase
before_price_increase = df_pink_morsel[df_pink_morsel["date"] < cutoff_date]
after_price_increase = df_pink_morsel[df_pink_morsel["date"] >= cutoff_date]

# Calculate total sales (price × quantity)
total_sales_before = (before_price_increase["price"] * before_price_increase["quantity"]).sum()
total_sales_after = (after_price_increase["price"] * after_price_increase["quantity"]).sum()

# Display results
print(f"Total Sales Before Jan 15, 2021: ${total_sales_before:,.2f}")
print(f"Total Sales After Jan 15, 2021: ${total_sales_after:,.2f}")

# Determine if sales increased or decreased
if total_sales_after > total_sales_before:
    print("Sales increased after the price increase.")
else:
    print("Sales decreased after the price increase.")
