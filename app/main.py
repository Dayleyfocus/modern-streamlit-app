"""
Main entry point for the Streamlit application.
"""
import streamlit as st
from streamlit_option_menu import option_menu
import hydralit_components as hc
from config import FEATURES, APP_TITLE, APP_ICON
from core.utils import set_page_config, load_css, create_footer
from features.home import home
from features.dashboard import dashboard
from features.about import about


def main():
    """Main application entry point."""
    # Initialize session state for active page
    if 'active_page' not in st.session_state:
        st.session_state.active_page = "home"
    
    # Set page config
    set_page_config()
    
    # Load custom CSS
    load_css()
    
    # Create header with logo and title
    st.markdown(f"<h1 style='text-align: center;'>{APP_ICON} {APP_TITLE}</h1>", unsafe_allow_html=True)
    
    # Create sidebar navigation using option_menu with icons
    with st.sidebar:
        # Create a list of enabled features
        enabled_features = [
            (feature_id, feature['name'], feature['icon'], feature['order'])
            for feature_id, feature in FEATURES.items()
            if feature['enabled']
        ]
        
        # Sort by order
        enabled_features.sort(key=lambda x: x[3])
        
        # Extract data for menu
        feature_ids = [f[0] for f in enabled_features]
        feature_names = [f[1] for f in enabled_features]
        feature_icons = [f[2] for f in enabled_features]
        
        # Create the menu
        selected = option_menu(
            menu_title="Navigation",
            options=feature_names,
            icons=feature_icons,
            menu_icon="list",
            default_index=feature_ids.index(st.session_state.active_page) if st.session_state.active_page in feature_ids else 0,
        )
        
        # Update session state based on selection
        selected_index = feature_names.index(selected)
        st.session_state.active_page = feature_ids[selected_index]
        
        # Information section
        st.markdown("---")
        st.markdown("### Theme")
        
        # Use simpler theme selector with radio buttons 
        theme_mode = st.radio(
            "Select theme:",
            ["Light", "Dark"],
            horizontal=True,
            label_visibility="collapsed"
        )
        
        # Store theme selection in session state
        st.session_state.theme = theme_mode.lower()
        
        # Information
        with st.expander("About This App", expanded=False):
            st.write("""
            This is a modern Streamlit application with a modular, feature-based architecture.
            Navigate through different features using the menu above.
            """)
    
    # Render the active feature
    if st.session_state.active_page == "home":
        home.render()
    elif st.session_state.active_page == "dashboard":
        dashboard.render()
    elif st.session_state.active_page == "about":
        about.render()
    else:
        st.error(f"Unknown feature: {st.session_state.active_page}")
    
    # Create footer
    create_footer()


if __name__ == "__main__":
    main() 