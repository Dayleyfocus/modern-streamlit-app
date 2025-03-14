"""
Configuration settings for the Streamlit application.
"""

# Application settings
APP_TITLE = "Modern Streamlit App"
APP_ICON = "🚀"
APP_SIDEBAR_EXPANDED = True

# Feature toggles
FEATURES = {
    "home": {
        "enabled": True,
        "name": "Home",
        "icon": "house",
        "order": 1
    },
    "dashboard": {
        "enabled": True,
        "name": "Dashboard",
        "icon": "bar-chart",
        "order": 2
    },
    "about": {
        "enabled": True,
        "name": "About",
        "icon": "info-circle",
        "order": 3
    }
}

# Theme settings
THEME = {
    "primaryColor": "#FF4B4B",
    "backgroundColor": "#FFFFFF",
    "secondaryBackgroundColor": "#F0F2F6",
    "textColor": "#262730",
    "font": "sans serif"
}

# Custom CSS
CUSTOM_CSS = """
<style>
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    .main-header {
        font-size: 2.5rem;
        margin-bottom: 1rem;
    }
    .subheader {
        font-size: 1.5rem;
        margin-bottom: 1rem;
        color: #6c757d;
    }
    .card {
        padding: 20px;
        border-radius: 10px;
        background-color: #ffffff;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    .feature-header {
        font-size: 1.8rem;
        font-weight: 600;
        margin-bottom: 1rem;
    }
    .footer {
        text-align: center;
        margin-top: 50px;
        color: #6c757d;
        font-size: 0.8rem;
    }
</style>
""" 