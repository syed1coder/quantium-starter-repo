#!/bin/bash

# Activate the virtual environment
source venv/Scripts/activate

# Execute the test suite
pytest test_app.py

# Capture the exit code
EXIT_CODE=$?

# Return the exit code
exit $EXIT_CODE
