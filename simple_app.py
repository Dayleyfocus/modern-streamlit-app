import streamlit as st
import time
from datetime import datetime
import random

def main():
    """Cookie Clicker Clone in Streamlit"""
    
    # Initialize session state variables
    if 'cookies' not in st.session_state:
        st.session_state.cookies = 0
    if 'cookies_per_click' not in st.session_state:
        st.session_state.cookies_per_click = 1
    if 'auto_clickers' not in st.session_state:
        st.session_state.auto_clickers = 0
    if 'grandmas' not in st.session_state:
        st.session_state.grandmas = 0
    if 'factories' not in st.session_state:
        st.session_state.factories = 0
    if 'last_update' not in st.session_state:
        st.session_state.last_update = datetime.now()
    if 'click_messages' not in st.session_state:
        st.session_state.click_messages = []
    
    # Calculate auto-cookies since last refresh
    now = datetime.now()
    elapsed_time = (now - st.session_state.last_update).total_seconds()
    cookies_to_add = int(elapsed_time * (st.session_state.auto_clickers + 
                                        st.session_state.grandmas * 5 + 
                                        st.session_state.factories * 20))
    
    if cookies_to_add > 0:
        st.session_state.cookies += cookies_to_add
        st.toast(f"Generated {cookies_to_add} cookies while you were away!")
    
    st.session_state.last_update = now
    
    # Title and description
    st.title("🍪 Cookie Clicker 🍪")
    st.markdown("_Click the cookie to earn more cookies!_")
    
    # Display current stats
    col1, col2 = st.columns([2, 3])
    
    with col1:
        st.subheader("Stats")
        st.metric("Cookies", f"{st.session_state.cookies:,}")
        st.metric("Per Click", f"{st.session_state.cookies_per_click:,}")
        
        cps = st.session_state.auto_clickers + (st.session_state.grandmas * 5) + (st.session_state.factories * 20)
        st.metric("Per Second", f"{cps:,}")
    
    with col2:
        # Cookie button - centered with CSS
        st.markdown(
            """
            <style>
            .cookie-btn {
                display: flex;
                justify-content: center;
            }
            </style>
            """, 
            unsafe_allow_html=True
        )
        
        st.markdown('<div class="cookie-btn">', unsafe_allow_html=True)
        
        # Make a large cookie button
        if st.button("🍪", key="cookie_button", use_container_width=True):
            earned = st.session_state.cookies_per_click
            st.session_state.cookies += earned
            
            # Add a random message for fun
            messages = [
                f"+{earned} cookies!",
                "Yummy!",
                "Keep clicking!",
                "More cookies!",
                "Delicious!",
                "Cookie time!",
                "That's a big cookie!",
                "Grandma approves!",
                "Sugar rush!",
                "Sweet!"
            ]
            
            # Show a small floating message
            st.session_state.click_messages.append({
                "message": random.choice(messages),
                "time": time.time()
            })
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Display click messages with animation
        for msg in list(st.session_state.click_messages):
            if time.time() - msg["time"] < 2:  # Show for 2 seconds
                opacity = 1 - (time.time() - msg["time"]) / 2
                st.markdown(
                    f"""
                    <div style="text-align: center; opacity: {opacity}; 
                              animation: float 2s ease-out; font-weight: bold; color: #FF9F1C;">
                        {msg["message"]}
                    </div>
                    <style>
                    @keyframes float {{
                        0% {{ transform: translateY(0); }}
                        100% {{ transform: translateY(-20px); }}
                    }}
                    </style>
                    """,
                    unsafe_allow_html=True
                )
            else:
                st.session_state.click_messages.remove(msg)
    
    # Shop section
    st.markdown("---")
    st.subheader("🛒 Cookie Shop")
    
    # Upgrades
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### Better Clicking")
        cost = (st.session_state.cookies_per_click * 10) + 10
        if st.button(f"Upgrade Clicker: {cost} cookies", 
                    disabled=st.session_state.cookies < cost):
            st.session_state.cookies -= cost
            st.session_state.cookies_per_click += 1
            st.balloons()
            st.experimental_rerun()
    
    with col2:
        st.markdown("### Auto Clickers")
        cost = (st.session_state.auto_clickers * 15) + 20
        if st.button(f"Buy Auto Clicker: {cost} cookies", 
                    disabled=st.session_state.cookies < cost):
            st.session_state.cookies -= cost
            st.session_state.auto_clickers += 1
            st.success("Auto Clicker purchased! +1 cookie per second.")
            st.experimental_rerun()
    
    with col3:
        st.markdown("### Grandma")
        cost = 100 + (st.session_state.grandmas * 50)
        if st.button(f"Hire Grandma: {cost} cookies", 
                    disabled=st.session_state.cookies < cost):
            st.session_state.cookies -= cost
            st.session_state.grandmas += 1
            st.success("Grandma hired! +5 cookies per second.")
            st.experimental_rerun()
    
    # More expensive upgrades
    st.markdown("---")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Cookie Factory")
        cost = 500 + (st.session_state.factories * 200)
        if st.button(f"Build Factory: {cost} cookies", 
                    disabled=st.session_state.cookies < cost):
            st.session_state.cookies -= cost
            st.session_state.factories += 1
            st.success("Factory built! +20 cookies per second.")
            st.experimental_rerun()
    
    with col2:
        if st.button("Free cookies (for testing)"):
            st.session_state.cookies += 1000
            st.success("Added 1,000 free cookies!")
            st.experimental_rerun()
    
    # Display current inventory
    st.markdown("---")
    st.subheader("Your Bakery")
    
    if st.session_state.auto_clickers > 0:
        st.markdown(f"🖱️ Auto Clickers: {st.session_state.auto_clickers}")
    
    if st.session_state.grandmas > 0:
        grandma_emojis = "👵 " * min(st.session_state.grandmas, 10)
        st.markdown(f"Grandmas: {st.session_state.grandmas}  {grandma_emojis}")
    
    if st.session_state.factories > 0:
        factory_emojis = "🏭 " * min(st.session_state.factories, 5)
        st.markdown(f"Factories: {st.session_state.factories}  {factory_emojis}")
    
    # Auto refresh to update cookies
    auto_refresh_container = st.empty()
    auto_refresh_container.markdown("Updating in 5...")
    
    # Reset button
    st.markdown("---")
    if st.button("Reset Game"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.experimental_rerun()

if __name__ == "__main__":
    # Set page config for a nicer appearance
    st.set_page_config(
        page_title="Cookie Clicker",
        page_icon="🍪",
        layout="centered",
        initial_sidebar_state="collapsed"
    )
    main() 