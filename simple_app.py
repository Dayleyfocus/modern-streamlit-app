import streamlit as st

def main():
    """A simple Streamlit app that's guaranteed to deploy."""
    
    st.title("Simple Streamlit App")
    st.subheader("A minimal working example")
    
    st.write("This is a basic Streamlit app with no complex imports or file dependencies.")
    
    # Basic interactivity
    name = st.text_input("Enter your name:")
    if name:
        st.write(f"Hello, {name}!")
    
    # A simple counter
    if 'count' not in st.session_state:
        st.session_state.count = 0
        
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("Increment"):
            st.session_state.count += 1
    
    with col2:
        if st.button("Decrement"):
            st.session_state.count -= 1
            
    with col3:
        if st.button("Reset"):
            st.session_state.count = 0
    
    st.metric("Counter Value", st.session_state.count)
    
    # Simple data display
    st.subheader("Sample Data")
    data = {
        'Category': ['A', 'B', 'C', 'D'],
        'Value': [10, 25, 15, 30]
    }
    st.write(data)
    st.bar_chart(data)
    
    # Footer
    st.markdown("---")
    st.caption("A simple Streamlit app with no dependencies")

if __name__ == "__main__":
    main() 