"""
Main entry point for the Streamlit application.
"""
import os
import sys

# Add app directory to path - this is crucial for resolving imports when running from different directories
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

import streamlit as st
from streamlit_option_menu import option_menu
import hydralit_components as hc
from config import FEATURES, APP_TITLE, APP_ICON
from core.utils import set_page_config, load_css, create_footer
from features.home import home
from features.dashboard import dashboard
from features.about import about


def main():
    """Render the main application."""
    # Set page configuration
    set_page_config()
    
    # Load custom CSS
    load_css()
    
    # Sidebar configuration
    with st.sidebar:
        st.image("static/images/logo.png", width=100)
        st.markdown(f"# {APP_TITLE}")
        st.markdown("---")
        
        # Navigation menu
        selected_feature = option_menu(
            menu_title="Navigation",
            options=["Home", "Dashboard", "About"],
            icons=["house", "graph-up", "info-circle"],
            menu_icon="list",
            default_index=0,
            orientation="vertical"
        )
        
        # Theme selector
        st.markdown("---")
        st.markdown("### Theme")
        theme_options = {
            "Light": "light",
            "Dark": "dark",
            "Blue": "blue",
        }
        
        # Use streamlit's native radio button for theme selection instead of hydralit_components
        selected_theme = st.radio(
            "Select Theme",
            options=list(theme_options.keys()),
            label_visibility="collapsed",
            horizontal=True,
            index=0
        )
        
        # Here we would typically set the theme based on selection
        # This is just for UI demonstration
        st.markdown(f"Selected: {selected_theme}")
    
    # Main content area - render the selected feature
    if selected_feature == "Home":
        home.render()
    elif selected_feature == "Dashboard":
        dashboard.render()
    elif selected_feature == "About":
        about.render()
    
    # Add footer
    create_footer()


# When the script is run directly, execute the main function
if __name__ == "__main__":
    main() 