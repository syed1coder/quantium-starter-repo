import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

# Load processed data
df = pd.read_csv("data/processed_data.csv")

# Convert date column to datetime format
df["date"] = pd.to_datetime(df["date"])

# Initialize Dash app
app = dash.Dash(__name__)

# Layout of the Dash app
app.layout = html.Div([
    html.H1("Soul Foods: Pink Morsel Sales Analysis", style={"text-align": "center"}),

    html.H3("Sales Trend Before & After Price Increase (15th Jan 2021)", style={"text-align": "center"}),

    dcc.Graph(
        id="sales-line-chart",
        figure=px.line(
            df, x="date", y="sales",
            title="Total Sales Over Time",
            labels={"date": "Date", "sales": "Total Sales"},
            markers=True
        ).add_vline(x="2021-01-15", line_dash="dash", line_color="red")
    ),
])

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
