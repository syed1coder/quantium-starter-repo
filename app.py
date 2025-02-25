import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

# Define constants
DATA_PATH = "./data/processed_data.csv"  # Update with the correct file path
COLORS = {
    "primary": "#FEDBFF",
    "secondary": "#D598EB",
    "font": "#522A61"
}

# Load and preprocess data
data = pd.read_csv(DATA_PATH)
data = data.sort_values(by="date")

# Initialize Dash app
dash_app = Dash(__name__)

# Function to generate line chart
def generate_figure(chart_data):
    fig = px.line(chart_data, x="date", y="sales", title="Quantium Sales Trends")
    fig.update_layout(
        plot_bgcolor=COLORS["secondary"],
        paper_bgcolor=COLORS["primary"],
        font_color=COLORS["font"]
    )
    return fig

# Create visualization
visualization = dcc.Graph(id="visualization", figure=generate_figure(data))

# Create header
header = html.H1(
    "Quantium Sales Dashboard",
    id="header",
    style={"backgroundColor": COLORS["secondary"], "color": COLORS["font"], "borderRadius": "20px"}
)

region_picker = dcc.Dropdown(
    options=[
        {"label": "North", "value": "north"},
        {"label": "East", "value": "east"},
        {"label": "South", "value": "south"},
        {"label": "West", "value": "west"},
        {"label": "All Regions", "value": "all"}
    ],
    value="all",
    id="region_picker"
)

# Define callback to update graph
@dash_app.callback(
    Output("visualization", "figure"),
    Input("region_picker", "value")
)
def update_graph(region):
    filtered_data = data if region == "all" else data[data["region"] == region]
    return generate_figure(filtered_data)

# Define app layout
dash_app.layout = html.Div([
    header,
    visualization,
    region_picker
], style={"textAlign": "center", "backgroundColor": COLORS["primary"], "borderRadius": "20px"})

# Run app
if __name__ == "__main__":
    dash_app.run_server(debug=True)
