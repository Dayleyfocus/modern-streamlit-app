"""
Home page feature for the Streamlit application.
"""
import streamlit as st
from core.utils import load_image


def render():
    """Render the home page."""
    # Header
    st.markdown("<h1 class='main-header'>Welcome to Modern Streamlit App</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subheader'>A powerful, extensible web application built with Streamlit</p>", unsafe_allow_html=True)
    
    # Introduction
    st.markdown("---")
    with st.container():
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.markdown("<h2 class='feature-header'>Modern Design & Architecture</h2>", unsafe_allow_html=True)
            st.write("""
            This application demonstrates a modern approach to building Streamlit apps with:
            
            * 🏗️ **Modular Architecture** - Features are isolated and independently extensible
            * 🎨 **Modern UI/UX** - Clean, responsive design with custom styling
            * 🔌 **Plug-and-Play Features** - Easily add new capabilities
            * 🌓 **Theme Support** - Light and dark mode
            
            Explore the different features through the sidebar navigation!
            """)
            
            # Call-to-action button
            if st.button("Explore Dashboard →", use_container_width=True):
                st.session_state.active_page = "dashboard"
                st.experimental_rerun()
            st.markdown("</div>", unsafe_allow_html=True)
        
        with col2:
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.markdown("<h3>Quick Stats</h3>", unsafe_allow_html=True)
            
            # Display some metrics
            col_a, col_b = st.columns(2)
            with col_a:
                st.metric(label="Users", value="1,204", delta="16%")
                st.metric(label="Engagement", value="89%", delta="4%")
            
            with col_b:
                st.metric(label="Features", value="3", delta="+1 this week")
                st.metric(label="Uptime", value="99.99%", delta="-0.01%", delta_color="off")
            st.markdown("</div>", unsafe_allow_html=True)
    
    # Feature highlights
    st.markdown("---")
    st.markdown("<h2 class='feature-header'>Key Features</h2>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("### 📊 Interactive Dashboard")
        st.write("Explore data with interactive visualizations and analytics tools.")
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("### 🔍 Data Analysis")
        st.write("Powerful data analysis capabilities with support for various data formats.")
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col3:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("### 📱 Responsive Design")
        st.write("Optimized for both desktop and mobile viewing experiences.")
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Call to action
    st.markdown("---")
    with st.container():
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<h2 class='feature-header' style='text-align:center;'>Get Started Today</h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center;'>Ready to explore more? Visit our dashboard to see interactive data visualizations.</p>", unsafe_allow_html=True)
        
        # Center the button using columns
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("Go to Dashboard", use_container_width=True):
                st.session_state.active_page = "dashboard"
                st.experimental_rerun()
        st.markdown("</div>", unsafe_allow_html=True) 