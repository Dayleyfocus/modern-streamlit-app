import streamlit as st
import time
import random
from datetime import datetime
import math

def main():
    """Galactic Miner - A Space Mining Clicker Game"""
    
    # Initialize session state variables
    if 'minerals' not in st.session_state:
        st.session_state.minerals = 0
    if 'minerals_per_click' not in st.session_state:
        st.session_state.minerals_per_click = 1
    if 'last_update' not in st.session_state:
        st.session_state.last_update = datetime.now()
    if 'click_messages' not in st.session_state:
        st.session_state.click_messages = []
    if 'achievements' not in st.session_state:
        st.session_state.achievements = []
    
    # Initialize all buildings/upgrades with default values of 0
    buildings = [
        "hand_miners", "mini_drones", "mining_rovers", "auto_extractors", 
        "orbital_stations", "asteroid_rigs", "planetary_harvesters", "dyson_spheres"
    ]
    
    for building in buildings:
        if building not in st.session_state:
            st.session_state[building] = 0
    
    # Initialize research upgrades
    research_types = ["mining_efficiency", "drone_ai", "refining", "quantum_extraction"]
    for research in research_types:
        if f"{research}_level" not in st.session_state:
            st.session_state[f"{research}_level"] = 0
    
    # Function to calculate minerals per second
    def get_minerals_per_second():
        # Base production values for each building
        building_production = {
            "hand_miners": 0.1,
            "mini_drones": 1,
            "mining_rovers": 8,
            "auto_extractors": 47,
            "orbital_stations": 260,
            "asteroid_rigs": 1400,
            "planetary_harvesters": 7800,
            "dyson_spheres": 44000
        }
        
        # Calculate production with research multipliers
        mining_multiplier = 1 + (st.session_state.mining_efficiency_level * 0.1)
        drone_multiplier = 1 + (st.session_state.drone_ai_level * 0.05)
        refining_multiplier = 1 + (st.session_state.refining_level * 0.15)
        quantum_multiplier = 1 + (st.session_state.quantum_extraction_level * 0.2)
        
        # Apply multipliers to appropriate buildings
        total_mps = 0
        for building, base_prod in building_production.items():
            count = st.session_state[building]
            multiplier = 1
            
            # Apply specific multipliers based on building type
            if building in ["hand_miners", "mini_drones"]:
                multiplier = mining_multiplier * drone_multiplier
            elif building in ["mining_rovers", "auto_extractors"]:
                multiplier = mining_multiplier * refining_multiplier
            elif building in ["orbital_stations", "asteroid_rigs"]:
                multiplier = refining_multiplier * quantum_multiplier
            else:
                multiplier = mining_multiplier * quantum_multiplier
                
            total_mps += base_prod * count * multiplier
            
        return total_mps
    
    # Process offline/idle production
    now = datetime.now()
    elapsed_time = (now - st.session_state.last_update).total_seconds()
    minerals_per_second = get_minerals_per_second()
    minerals_to_add = int(elapsed_time * minerals_per_second)
    
    if minerals_to_add > 0:
        st.session_state.minerals += minerals_to_add
        st.toast(f"Your mining operation generated {minerals_to_add:,} minerals while you were away!")
    
    st.session_state.last_update = now
    
    # Check for achievements
    achievements_data = [
        {"id": "first_click", "name": "First Contact", "desc": "Mine your first mineral", "threshold": 1},
        {"id": "hundred_minerals", "name": "Promising Start", "desc": "Accumulate 100 minerals", "threshold": 100},
        {"id": "first_drone", "name": "Automation Begins", "desc": "Purchase your first mini drone", "threshold": 1},
        {"id": "mineral_baron", "name": "Mineral Baron", "desc": "Accumulate 10,000 minerals", "threshold": 10000},
        {"id": "space_tycoon", "name": "Space Tycoon", "desc": "Own 10 orbital stations", "threshold": 10},
        {"id": "galactic_empire", "name": "Galactic Empire", "desc": "Purchase your first Dyson Sphere", "threshold": 1}
    ]
    
    # Check for new achievements
    for achievement in achievements_data:
        if achievement["id"] not in st.session_state.achievements:
            if achievement["id"] == "first_click" and st.session_state.minerals >= achievement["threshold"]:
                st.session_state.achievements.append(achievement["id"])
                st.balloons()
                st.success(f"🏆 Achievement Unlocked: {achievement['name']} - {achievement['desc']}")
            elif achievement["id"] == "hundred_minerals" and st.session_state.minerals >= achievement["threshold"]:
                st.session_state.achievements.append(achievement["id"])
                st.success(f"🏆 Achievement Unlocked: {achievement['name']} - {achievement['desc']}")
            elif achievement["id"] == "first_drone" and st.session_state.mini_drones >= achievement["threshold"]:
                st.session_state.achievements.append(achievement["id"])
                st.success(f"🏆 Achievement Unlocked: {achievement['name']} - {achievement['desc']}")
            elif achievement["id"] == "mineral_baron" and st.session_state.minerals >= achievement["threshold"]:
                st.session_state.achievements.append(achievement["id"])
                st.success(f"🏆 Achievement Unlocked: {achievement['name']} - {achievement['desc']}")
            elif achievement["id"] == "space_tycoon" and st.session_state.orbital_stations >= achievement["threshold"]:
                st.session_state.achievements.append(achievement["id"])
                st.balloons()
                st.success(f"🏆 Achievement Unlocked: {achievement['name']} - {achievement['desc']}")
            elif achievement["id"] == "galactic_empire" and st.session_state.dyson_spheres >= achievement["threshold"]:
                st.session_state.achievements.append(achievement["id"])
                st.snow()
                st.success(f"🏆 Achievement Unlocked: {achievement['name']} - {achievement['desc']}")
    
    # Page header and main UI
    st.title("🪐 Galactic Miner 🚀")
    st.markdown("_Click the asteroid to mine precious space minerals!_")
    
    # Main stats area
    col1, col2 = st.columns([2, 3])
    
    with col1:
        st.subheader("Mining Stats")
        st.metric("💎 Minerals", f"{st.session_state.minerals:,.0f}")
        st.metric("⛏️ Per Click", f"{st.session_state.minerals_per_click:,.1f}")
        
        mps = get_minerals_per_second()
        st.metric("⏱️ Per Second", f"{mps:,.1f}")
    
    with col2:
        # Main clicker button with CSS for better visibility
        st.markdown(
            """
            <style>
            .mining-btn {
                display: flex;
                justify-content: center;
                margin-top: 20px;
            }
            .stButton button {
                background: linear-gradient(45deg, #3d5a80, #98c1d9);
                border: 2px solid #293241;
            }
            </style>
            """, 
            unsafe_allow_html=True
        )
        
        st.markdown('<div class="mining-btn">', unsafe_allow_html=True)
        
        # Make a large asteroid button
        if st.button("🌑", key="mine_button", use_container_width=True):
            # Apply click multipliers from research
            multiplier = 1 + (st.session_state.mining_efficiency_level * 0.1)
            earned = st.session_state.minerals_per_click * multiplier
            st.session_state.minerals += earned
            
            # Add a random message for fun
            messages = [
                f"+{earned:,.1f} minerals!",
                "Rich deposit!",
                "Keep mining!",
                "Precious minerals!",
                "Space riches!",
                "Mining success!",
                "Asteroid cracked!",
                "Mineral vein!",
                "Jackpot!",
                "Pure crystals!"
            ]
            
            # Show a floating message
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
                              animation: float 2s ease-out; font-weight: bold; color: #ee6c4d;">
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
    
    # Tabs for different categories
    tab1, tab2, tab3 = st.tabs(["Mining Operations", "Research Lab", "Achievements"])
    
    with tab1:
        st.subheader("🛒 Purchase Mining Equipment")
        
        # Function to handle building purchases
        def buy_building(building_id, building_name, base_cost, description, production):
            current_count = st.session_state[building_id]
            cost = math.floor(base_cost * (1.15 ** current_count))
            
            with st.container():
                col1, col2 = st.columns([3, 1])
                with col1:
                    st.markdown(f"### {building_name}")
                    st.markdown(f"{description}")
                    st.caption(f"Produces {production:,.1f} minerals per second")
                    st.caption(f"You own: {current_count}")
                
                with col2:
                    if st.button(f"Buy: {cost:,} 💎", key=f"buy_{building_id}", 
                               disabled=st.session_state.minerals < cost):
                        st.session_state.minerals -= cost
                        st.session_state[building_id] += 1
                        st.success(f"Purchased 1 {building_name}!")
                        st.experimental_rerun()
                
                st.markdown("---")
        
        # List available buildings
        buy_building("hand_miners", "Hand Miner", 15, 
                     "Basic mining tool for small-scale mineral extraction", 0.1)
        
        buy_building("mini_drones", "Mini Mining Drone", 100, 
                     "Autonomous drones that mine without supervision", 1)
        
        buy_building("mining_rovers", "Mining Rover", 1100, 
                     "Surface vehicles that extract minerals from planetary surfaces", 8)
        
        buy_building("auto_extractors", "Automated Extractor", 12000, 
                     "Advanced mining rigs with AI-controlled extraction protocols", 47)
        
        buy_building("orbital_stations", "Orbital Mining Station", 130000, 
                     "Space stations dedicated to processing asteroids", 260)
        
        buy_building("asteroid_rigs", "Asteroid Mining Rig", 1400000, 
                     "Massive drilling platforms attached to mineral-rich asteroids", 1400)
        
        buy_building("planetary_harvesters", "Planetary Harvester", 20000000, 
                     "Planet-scale devices that extract minerals from entire worlds", 7800)
        
        buy_building("dyson_spheres", "Dyson Sphere", 330000000, 
                     "Megastructures that harness the power of stars for mining operations", 44000)
    
    with tab2:
        st.subheader("🔬 Research Technologies")
        
        # Function to handle research upgrades
        def research_upgrade(research_id, name, description, base_cost, effect):
            current_level = st.session_state[f"{research_id}_level"]
            cost = math.floor(base_cost * (2 ** current_level))
            
            with st.container():
                col1, col2 = st.columns([3, 1])
                with col1:
                    st.markdown(f"### {name} (Level {current_level})")
                    st.markdown(f"{description}")
                    st.caption(f"Effect: {effect}")
                
                with col2:
                    if st.button(f"Research: {cost:,} 💎", key=f"research_{research_id}", 
                               disabled=st.session_state.minerals < cost):
                        st.session_state.minerals -= cost
                        st.session_state[f"{research_id}_level"] += 1
                        st.success(f"Researched {name} to level {current_level + 1}!")
                        st.experimental_rerun()
                
                st.markdown("---")
        
        # List available research
        research_upgrade("mining_efficiency", "Advanced Mining Techniques", 
                         "Improve the efficiency of all mining operations", 
                         500, "+10% minerals per click and improved hand miners & drones")
        
        research_upgrade("drone_ai", "Drone AI Optimization", 
                         "Enhance the artificial intelligence of your mining drones", 
                         2000, "+5% production from automated mining equipment")
        
        research_upgrade("refining", "Mineral Refining Process", 
                         "Develop better ways to process raw minerals", 
                         10000, "+15% production from rovers and extractors")
        
        research_upgrade("quantum_extraction", "Quantum Extraction", 
                         "Harness quantum mechanics for mineral extraction", 
                         50000, "+20% production from advanced mining structures")
        
        # Upgrade mining power
        st.markdown("### 🔨 Upgrade Mining Tools")
        click_upgrade_cost = 25 * (2 ** (st.session_state.minerals_per_click - 1))
        
        if st.button(f"Upgrade Mining Power: {click_upgrade_cost:,} 💎", 
                   disabled=st.session_state.minerals < click_upgrade_cost):
            st.session_state.minerals -= click_upgrade_cost
            st.session_state.minerals_per_click += 1
            st.success(f"Mining power upgraded to {st.session_state.minerals_per_click}!")
            st.experimental_rerun()
    
    with tab3:
        st.subheader("🏆 Achievements")
        
        # Display unlocked achievements
        if not st.session_state.achievements:
            st.info("No achievements unlocked yet. Keep mining!")
        else:
            for achievement in achievements_data:
                if achievement["id"] in st.session_state.achievements:
                    st.success(f"**{achievement['name']}**: {achievement['desc']}")
        
        # Display locked achievements (but don't show the secret ones)
        st.markdown("---")
        st.markdown("### Locked Achievements")
        
        locked = [a for a in achievements_data if a["id"] not in st.session_state.achievements]
        if not locked:
            st.success("You've unlocked all achievements! You're a true galactic mining legend!")
        else:
            for achievement in locked:
                st.caption(f"❓ **{achievement['name']}**: {achievement['desc']}")
    
    # Developer options (for testing)
    with st.expander("Developer Options"):
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("Add 1,000 Minerals"):
                st.session_state.minerals += 1000
                st.success("Added 1,000 minerals for testing")
                st.experimental_rerun()
                
            if st.button("Add 1,000,000 Minerals"):
                st.session_state.minerals += 1000000
                st.success("Added 1,000,000 minerals for testing")
                st.experimental_rerun()
        
        with col2:
            if st.button("Reset Game", type="primary"):
                for key in list(st.session_state.keys()):
                    del st.session_state[key]
                st.success("Game reset! Starting fresh...")
                st.experimental_rerun()
    
    # Footer
    st.markdown("---")
    st.caption("Galactic Miner v1.0 | Made with Streamlit")

if __name__ == "__main__":
    # Set page config for a nicer appearance
    st.set_page_config(
        page_title="Galactic Miner",
        page_icon="🪐",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    main() 