import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load processed data
df = pd.read_csv("data/processed_data.csv")

# Convert 'date' column to datetime format
df["date"] = pd.to_datetime(df["date"])

# Group by date and calculate total daily sales
daily_sales = df.groupby("date")["sales"].sum().reset_index()


# Plot the sales trend
plt.figure(figsize=(12, 6))
sns.lineplot(data=daily_sales, x="date", y="sales", label="Daily Sales", color="blue")

# Mark the price increase date
cutoff_date = pd.to_datetime("2021-01-15")
plt.axvline(x=cutoff_date, color="red", linestyle="--", label="Price Increase")
plt.title("Sales Trend of Pink Morsel Before and After Price Increase")


# Customize plot
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.title("Sales Trend of Pink Morsel Before and After Price Increase")
plt.legend()
plt.xticks(rotation=45)

# Show plot
plt.show()
