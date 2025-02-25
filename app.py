import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html

# ✅ Load the processed data
df = pd.read_csv("data/processed_data.csv")

# ✅ Create the Dash app
app = dash.Dash(__name__)

# ✅ Create the figure (using 'sales' instead of 'price')
figure = px.line(df, x="date", y="sales", color="region", title="Total Sales Over Time")

# ✅ Define the layout
app.layout = html.Div(children=[
    html.H1(children="Sales Dashboard", style={"textAlign": "center"}),

    dcc.Graph(id="sales-graph", figure=figure),
])

# ✅ Run the app
if __name__ == "__main__":
    print("Starting the Dash app...")
    app.run_server(debug=True)
