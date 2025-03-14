"""
About page feature for the Streamlit application.
"""
import streamlit as st
import time


def render():
    """Render the about page."""
    # Header
    st.markdown("<h1 class='main-header'>About This Application</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subheader'>Learn more about this modern Streamlit app</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    # About the application
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<h2 class='feature-header'>Project Overview</h2>", unsafe_allow_html=True)
    
    st.write("""
    This application demonstrates a modern approach to building Streamlit web applications with a focus on:
    
    * **Feature Isolation**: Each feature is isolated with clear boundaries to ensure adding/modifying one doesn't affect others
    * **Plug-and-Play Architecture**: The system is designed so new features can be "plugged in" without modifying existing code
    * **Extension Points**: The architecture includes proactive design of extension points for future features
    * **Feature Toggles**: Features are implemented behind toggles for safe integration
    
    The application follows a modular architecture that enables long-term maintainability and feature extensibility.
    """)
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Technical details
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<h2 class='feature-header'>Technical Details</h2>", unsafe_allow_html=True)
    
    # Create tabs for different technical aspects
    tech_tab1, tech_tab2, tech_tab3 = st.tabs(["Architecture", "Technologies", "Design Principles"])
    
    with tech_tab1:
        st.markdown("### Application Architecture")
        st.write("""
        The application follows a feature-based architecture:
        
        ```
        app/
        ├── main.py                    # Main application entry point
        ├── config.py                  # Configuration settings
        ├── core/                      # Core application utilities
        ├── features/                  # Feature modules
        │   ├── home/                  # Home page feature
        │   ├── dashboard/             # Dashboard feature
        │   └── about/                 # About page feature
        └── static/                    # Static assets
            ├── css/                   # CSS files
            └── images/                # Image assets
        ```
        
        Each feature is self-contained, with its own rendering logic and dependencies.
        """)
    
    with tech_tab2:
        st.markdown("### Key Technologies")
        
        # Create two columns for technologies
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Frontend")
            st.write("""
            - **Streamlit** - Main web application framework
            - **Streamlit Components** - For enhanced UI elements
            - **Plotly** - For interactive data visualizations
            - **Custom CSS** - For UI styling and theming
            """)
        
        with col2:
            st.markdown("#### Backend")
            st.write("""
            - **Python** - Core programming language
            - **Pandas** - For data manipulation
            - **NumPy** - For numerical operations
            - **Pillow** - For image processing
            """)
    
    with tech_tab3:
        st.markdown("### Design Principles")
        st.write("""
        The application adheres to the following design principles:
        
        1. **Modular Monolith**: The application is structured as independent modules that can evolve separately
        2. **Composition over Inheritance**: Uses composition patterns to extend functionality
        3. **Dependency Inversion**: High-level modules don't depend on low-level modules; both depend on abstractions
        4. **Configuration-Driven Features**: Features are configurable rather than hardcoded
        5. **Event-Driven Communication**: Uses events for cross-feature communication to minimize direct dependencies
        """)
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # System status
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<h2 class='feature-header'>System Status</h2>", unsafe_allow_html=True)
    
    # Display system metrics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(label="System Status", value="Operational", delta=None)
    
    with col2:
        st.metric(label="Response Time", value="42ms", delta="-3ms")
    
    with col3:
        st.metric(label="Version", value="1.0.0", delta=None)
    
    # Add a simple progress bar as a visual element
    st.markdown("### System Resources")
    st.progress(0.7)
    st.caption("CPU Usage: 70%")
    
    st.progress(0.45)
    st.caption("Memory Usage: 45%")
    
    st.progress(0.23)
    st.caption("Disk Usage: 23%")
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Contact and resources
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<h2 class='feature-header'>Resources & Contact</h2>", unsafe_allow_html=True)
    
    # Resources section with expanders
    with st.expander("Documentation"):
        st.write("""
        Comprehensive documentation for this application can be found at our GitHub repository.
        It includes setup instructions, architecture details, and guides for adding new features.
        """)
    
    with st.expander("Contributing"):
        st.write("""
        We welcome contributions to this project! Please check the contribution guidelines in our repository.
        """)
    
    with st.expander("Support"):
        st.write("""
        For support or bug reports, please open an issue in our GitHub repository or contact the development team.
        """)
    
    # Contact form
    st.markdown("### Contact Us")
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        
        submitted = st.form_submit_button("Submit")
        if submitted:
            # Simulate sending (would be an actual API call in production)
            with st.spinner("Sending..."):
                time.sleep(1)  # Simulate processing
            st.success("Thank you for your message! We'll get back to you soon.")
    
    st.markdown("</div>", unsafe_allow_html=True) 