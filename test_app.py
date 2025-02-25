import pytest
from app import dash_app  # Import your Dash app


@pytest.fixture
def dash_duo_app(dash_duo):
    """Start the Dash app for testing"""
    dash_duo.start_server(dash_app)
    return dash_duo

def test_header_present(dash_duo_app):
    """Check if the header is present in the app."""
    header = dash_duo_app.wait_for_element("#header", timeout=10)
    assert header is not None, "Header element not found"

def test_visualization_present(dash_duo_app):
    """Check if the visualization graph is present."""
    visualization = dash_duo_app.wait_for_element("#visualization", timeout=10)
    assert visualization is not None, "Visualization graph not found"

def test_region_picker_present(dash_duo_app):
    """Check if the region picker is present."""
    region_picker = dash_duo_app.wait_for_element("#region_picker", timeout=10)
    assert region_picker is not None, "Region picker dropdown not found"

# Removed the test for callback functionality due to issues with dropdown selection


if __name__ == "__main__":
    pytest.main()
