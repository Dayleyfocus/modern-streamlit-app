"""
Entry point for Streamlit Cloud deployment
"""
import os
import sys

# Add the current directory to the path so app can be imported as a module
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Import the app's main function from the app package
from app.main import main

# Run the app
if __name__ == "__main__":
    main() 