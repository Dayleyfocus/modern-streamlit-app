"""
About page feature for the Streamlit application.
"""
import streamlit as st
from ...core.utils import load_image


def render():
    """Render the about page."""
    # Header
    st.markdown("<h1 class='main-header'>About This App</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subheader'>Learn more about this modern Streamlit application</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    # Main content
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ## Project Overview
        
        This is a modern Streamlit application showcasing best practices for building 
        professional-grade web applications with Streamlit. The application demonstrates:
        
        - **Modular Architecture**: Organized code with separation of concerns
        - **Professional UI/UX**: Clean, responsive design with consistent styling
        - **Interactive Features**: Dynamic components and data visualizations
        - **Performance Optimization**: Efficient data handling and caching
        
        ## Key Features
        
        - 🏠 **Home Page**: Application overview and quick navigation
        - 📊 **Interactive Dashboard**: Data visualization with customizable charts  
        - ℹ️ **About Page**: Project information and documentation
        
        ## Technical Implementation
        
        The application is built with:
        
        - **Streamlit** for the web application framework
        - **Plotly** for interactive data visualizations
        - **Pandas** for data manipulation
        - **Custom CSS** for styling enhancements
        
        The codebase follows a feature-based architecture with a core module for shared utilities.
        """)
        
        # Expandable sections for more details
        with st.expander("Development Approach"):
            st.markdown("""
            ### Modern Python Development
            
            This project follows modern Python development practices:
            
            - Type hints for better code quality
            - Modular architecture for maintainability
            - Proper documentation with docstrings
            - Clean code principles
            
            ### UI/UX Considerations
            
            The UI is designed with these principles in mind:
            
            - Consistent visual language
            - Responsive layouts that work on different devices
            - Intuitive navigation
            - Progressive disclosure of complex features
            """)
        
        with st.expander("Future Enhancements"):
            st.markdown("""
            ### Planned Features
            
            - User authentication system
            - Advanced data analysis tools
            - PDF report generation
            - API integrations with external data sources
            - Dark/light theme toggle
            - Performance monitoring dashboard
            """)
    
    with col2:
        # About image
        image = load_image("about_illustration.png")
        st.image(image, use_column_width=True)
        
        # Tech stack badges
        st.markdown("### Tech Stack")
        st.markdown("""
        - Python 3.9+
        - Streamlit 1.15+
        - Pandas 1.5+
        - Plotly 5.10+
        - NumPy 1.23+
        """)
        
        # Contact info
        st.markdown("### Connect & Contribute")
        st.markdown("""
        - [GitHub Repository](https://github.com/username/repo)
        - [Documentation](https://docs.example.com)
        - [Report an Issue](https://github.com/username/repo/issues)
        """)
    
    # Bottom section with cards
    st.markdown("---")
    st.markdown("<h2 class='feature-header'>Project Timeline</h2>", unsafe_allow_html=True)
    
    # Project timeline cards
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("### Phase 1: Foundation")
        st.markdown("""
        - Initial application architecture
        - Core feature implementation
        - Basic UI/UX design
        - Documentation setup
        """)
        st.markdown("<span class='badge'>Completed</span>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("### Phase 2: Enhancement")
        st.markdown("""
        - Advanced data visualizations
        - Performance optimization
        - Responsive design improvements
        - User feedback integration
        """)
        st.markdown("<span class='badge'>In Progress</span>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col3:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("### Phase 3: Expansion")
        st.markdown("""
        - Additional feature modules
        - API integrations
        - Authentication system
        - Advanced analytics
        """)
        st.markdown("<span class='badge badge-future'>Planned</span>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Footer quote
    st.markdown("---")
    st.markdown("""
    <div class='quote'>
    "The best way to predict the future is to invent it." — Alan Kay
    </div>
    """, unsafe_allow_html=True) 