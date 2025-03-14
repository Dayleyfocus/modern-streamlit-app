"""
Dashboard feature for the Streamlit application.
"""
import streamlit as st
import pandas as pd
import numpy as np
from app.core.utils import create_chart, get_sample_data


def render():
    """Render the dashboard page."""
    # Header
    st.markdown("<h1 class='main-header'>Interactive Dashboard</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subheader'>Explore data with interactive visualizations</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    # Filters in sidebar
    with st.sidebar:
        st.markdown("## Dashboard Settings")
        
        chart_type = st.selectbox(
            "Chart Type",
            options=["bar", "line", "scatter", "pie"],
            index=0
        )
        
        # Sample filter
        show_details = st.toggle("Show Details", value=True)
        
        # Time period filter
        time_period = st.select_slider(
            "Time Period",
            options=["Day", "Week", "Month", "Quarter", "Year"],
            value="Month"
        )
        
        st.markdown("---")
        st.markdown("### Data Settings")
        
        # Option to generate random data
        if st.button("Generate Random Data", use_container_width=True):
            st.session_state.random_data = True
        else:
            if 'random_data' not in st.session_state:
                st.session_state.random_data = False
    
    # Main dashboard area
    main_container = st.container()
    with main_container:
        # Overview metrics
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<h2 class='feature-header'>Key Metrics</h2>", unsafe_allow_html=True)
        
        # Create metrics row
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric(
                label="Total Revenue",
                value="$12,345",
                delta="18.2%"
            )
        
        with col2:
            st.metric(
                label="Active Users",
                value="1,234",
                delta="12.1%"
            )
        
        with col3:
            st.metric(
                label="Conversion Rate",
                value="3.2%",
                delta="-0.5%",
                delta_color="inverse"
            )
        
        with col4:
            st.metric(
                label="Avg. Session",
                value="2m 45s",
                delta="0.6%"
            )
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Charts section
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<h2 class='feature-header'>Data Visualization</h2>", unsafe_allow_html=True)
        
        # Chart tabs
        tab1, tab2 = st.tabs(["Performance Charts", "Detailed Analysis"])
        
        with tab1:
            # Sample or random data based on state
            if st.session_state.random_data:
                # Generate random data
                categories = ["Product A", "Product B", "Product C", "Product D", "Product E"]
                data = pd.DataFrame({
                    'Category': categories,
                    'Values': np.random.randint(10, 100, size=5),
                    'Growth': np.random.randint(-20, 30, size=5)
                })
            else:
                # Use sample data
                data = get_sample_data()
            
            # Create main chart based on selected type
            fig = create_chart(
                data=data,
                chart_type=chart_type,
                x='Category',
                y='Values',
                color='Category' if chart_type != 'pie' else None,
                title=f"{time_period}ly Performance"
            )
            
            if fig:
                st.plotly_chart(fig, use_container_width=True)
            
            # Show details if toggled
            if show_details:
                st.markdown("### Data Table")
                st.dataframe(data, use_container_width=True)
                
                # Additional chart for growth
                if chart_type != 'pie':
                    growth_fig = create_chart(
                        data=data,
                        chart_type='bar',
                        x='Category',
                        y='Growth',
                        title=f"{time_period}ly Growth (%)"
                    )
                    st.plotly_chart(growth_fig, use_container_width=True)
        
        with tab2:
            # Generate more complex data for detailed analysis
            dates = pd.date_range(start='2023-01-01', periods=30, freq='D')
            detailed_data = pd.DataFrame({
                'Date': dates,
                'Visitors': np.random.randint(100, 1000, size=30),
                'Conversions': np.random.randint(10, 100, size=30),
                'Revenue': np.random.randint(1000, 10000, size=30)
            })
            
            # Time series chart
            time_fig = create_chart(
                data=detailed_data,
                chart_type='line',
                x='Date',
                y='Visitors',
                title=f"Daily Visitors ({time_period})"
            )
            st.plotly_chart(time_fig, use_container_width=True)
            
            # Correlation chart
            scatter_fig = create_chart(
                data=detailed_data,
                chart_type='scatter',
                x='Visitors',
                y='Conversions',
                title="Visitors vs Conversions"
            )
            st.plotly_chart(scatter_fig, use_container_width=True)
            
            # Data table with more details
            st.markdown("### Detailed Data")
            st.dataframe(detailed_data, use_container_width=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Analysis section
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<h2 class='feature-header'>Insights</h2>", unsafe_allow_html=True)
        
        # Some placeholder insights
        st.info("📈 **Performance Trend**: Overall positive growth trend observed in the selected time period.")
        st.success("🎯 **Key Finding**: Product C shows the highest growth rate at 15%.")
        st.warning("⚠️ **Watch Out**: Conversion rates have slightly decreased in the last period.")
        
        st.markdown("</div>", unsafe_allow_html=True) 