"""
Core utility functions for the Streamlit application.
"""
import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
import os


def load_css():
    """Load custom CSS from config."""
    from config import CUSTOM_CSS
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)


def set_page_config():
    """Configure the Streamlit page settings."""
    from config import APP_TITLE, APP_ICON, THEME
    
    st.set_page_config(
        page_title=APP_TITLE,
        page_icon=APP_ICON,
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            'Get Help': 'https://github.com/yourusername/modern-streamlit-app',
            'Report a bug': 'https://github.com/yourusername/modern-streamlit-app/issues',
            'About': f"# {APP_TITLE}\nA modern Streamlit web application."
        }
    )
    
    # Set theme
    for k, v in THEME.items():
        st.config.set_option(f"theme.{k}", v)


def create_footer():
    """Add a footer to the page."""
    st.markdown("""
    <div class="footer">
        <p>© 2023 Modern Streamlit App. All rights reserved.</p>
    </div>
    """, unsafe_allow_html=True)


def load_image(image_path):
    """Load an image from the static directory."""
    try:
        # Get the app directory path
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
        # If the path doesn't already include 'static/images', add it
        if not image_path.startswith(('static/', '/static/', 'app/static/')):
            image_path = os.path.join('static', 'images', image_path)
        
        # Construct the absolute path
        absolute_path = os.path.join(base_path, image_path)
        
        # Check if file exists
        if not os.path.exists(absolute_path):
            st.warning(f"Image not found: {image_path}")
            return Image.new('RGB', (300, 200), color=(240, 240, 240))
            
        # Open the image
        image = Image.open(absolute_path)
        return image
    except Exception as e:
        # Use a placeholder if the image can't be loaded
        st.error(f"Error loading image: {e}")
        # Create a simple colored placeholder image
        placeholder = Image.new('RGB', (300, 200), color=(240, 240, 240))
        return placeholder


def create_chart(data, chart_type='bar', x=None, y=None, color=None, title=None):
    """Create a Plotly chart based on the given data and type."""
    if x is None or y is None:
        st.error("X and Y values must be provided for the chart.")
        return None
    
    if chart_type == 'bar':
        fig = px.bar(data, x=x, y=y, color=color, title=title)
    elif chart_type == 'line':
        fig = px.line(data, x=x, y=y, color=color, title=title)
    elif chart_type == 'scatter':
        fig = px.scatter(data, x=x, y=y, color=color, title=title)
    elif chart_type == 'pie':
        fig = px.pie(data, values=y, names=x, title=title)
    else:
        st.error(f"Unsupported chart type: {chart_type}")
        return None
    
    fig.update_layout(
        title_font_size=22,
        xaxis_title_font_size=16,
        yaxis_title_font_size=16,
        legend_title_font_size=14,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        margin=dict(l=20, r=20, t=40, b=20),
    )
    
    return fig


def get_sample_data():
    """Return sample data for demonstration purposes."""
    df = pd.DataFrame({
        'Category': ['A', 'B', 'C', 'D', 'E'],
        'Values': [10, 25, 15, 30, 20],
        'Growth': [5, -2, 7, 10, -5]
    })
    return df


def feature_toggle(feature_name):
    """Check if a feature is enabled in the config."""
    from config import FEATURES
    feature = FEATURES.get(feature_name, {})
    return feature.get('enabled', False) 