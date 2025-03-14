"""
Root-level entry point for Streamlit Cloud deployment.
This file is used for deploying to Streamlit Cloud and redirects to the actual application.
"""
import os
import sys
import streamlit as st

# Add the app directory to the path to resolve import issues
app_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "app")
if app_dir not in sys.path:
    sys.path.insert(0, app_dir)

# Import the main function from the actual app
from app.main import main

# Run the application
if __name__ == "__main__":
    main() 