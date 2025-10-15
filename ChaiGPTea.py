import streamlit as st
import random
from streamlit_folium import st_folium
import folium
from geopy.geocoders import Nominatim

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="ChaiGPTea - AI-Powered Chai Experience",
    page_icon="🍵",
    layout="wide",
)

# --- BACKGROUND CSS ---
tea_bg = "https://images.unsplash.com/photo-1564890369478-c89ca6d9cde9?w=1920&q=80"
st.markdown(
    f"""
    <style>
    .stApp {{
        background: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.6)), url("{tea_bg}");
        background-size: cover;
        background-attachment: fixed;
        color: white;
        font-family: 'Poppins', sans-serif;
    }}
    .main-title {{
        font-size: 64px;
        font-weight: 900;
        text-align: center;
        color: #fff;
        text-shadow: 0 0 30px #8B4513;
    }}
    .slogan {{
        text-align: center;
        font-size: 22px;
        color: #f5deb3;
        margin-top: -15px;
        margin-bottom: 40px;
    }}
    .custom-card {{
        background: rgba(255,255,255,0.85);
        color: #3e2723;
        border-radius: 20px;
        padding: 30px;
        box-shadow: 0 6px 20px rgba(0,0,0,0.3);
    }}
    .credits {{
        text-align: center;
        color: #f5deb3;
        margin-top: 30px;
        font-size: 14px;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# --- HEADER ---
st.markdown("<h1 class='main-title'>🍵 ChaiGPTea</h1>", unsafe_allow_html=True)
st.markdown("<p class='slogan'>Perfection in every sip – AI meets traditional chai ☕</p>", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.header("🧠 Customize Your Perfect Chai")
    tea_strength = st.radio("Tea Strength", ["Weak", "Medium", "Strong"])
    sweetness = st.radio("Sweetness", ["None", "Light", "Medium", "Sweet"])
    spice = st.radio("Spice Level", ["Mild", "Medium", "Strong"])
    milk = st.slider("Milk Quantity (ml)", 50, 250, 150, 10)
    sugar = st.slider("Sugar Quantity (tsp)", 0, 5, 2, 1)
    temp = st.selectbox("Temperature", ["Hot", "Warm", "Cold"])
    addons = st.multiselect(
        "Special Add-ons",
        ["Cardamom", "Ginger", "Cloves", "Cinnamon", "Saffron", "Mint", "Tulsi", "Lemongrass"],
    )

# --- AI SUGGESTIONS ---
suggestions = [
    "Add a hint of cardamom for a classic aroma 🌿",
    "Try ginger for that spicy winter vibe 🔥",
    "Perfect blend achieved – ready to brew 🍯",
    "Saffron can give royal flavor notes 👑",
    "Add tulsi for a healing herbal twist 🌿",
    "Lemongrass adds a refreshing tang 🍋",
]
ai_feedback = random.choice(suggestions)

# --- CHAI SUMMARY CARD ---
col1, col2 = st.columns([1, 1])
with col1:
    st.markdown("<div class='custom-card'>", unsafe_allow_html=True)
    st.subheader("☕ Your Chai Summary")
    st.write(f"**Tea Strength:** {tea_strength}")
    st.write(f"**Sweetness:** {sweetness}")
    st.write(f"**Spice Intensity:** {spice}")
    st.write(f"**Milk:** {milk} ml")
    st.write(f"**Sugar:** {sugar} tsp")
    st.write(f"**Temperature:** {temp}")
    st.write(f"**Add-ons:** {', '.join(addons) if addons else 'None'}")
    st.info(f"**AI Suggestion:** {ai_feedback}")
    st.markdown("</div>", unsafe_allow_html=True)

# --- LOCATION SECTION ---
with col2:
    st.markdown("<div class='custom-card'>", unsafe_allow_html=True)
    st.subheader("📍 Select Your Delivery Location (OpenStreetMap)")
    st.caption("Zoom in, drag, or click to choose your exact chai delivery spot 🍵")

    default_location = [22.3039, 70.8022]  # Rajkot as default
    m = folium.Map(location=default_location, zoom_start=12)
    map_data = st_folium(m, height=350, width=550)

    if map_data and map_data.get("last_clicked"):
        lat = map_data["last_clicked"]["lat"]
        lon = map_data["last_clicked"]["lng"]
        geolocator = Nominatim(user_agent="chai-gpt")
        location = geolocator.reverse((lat, lon), language="en")
        address = location.address if location else "Could not find address"
        st.success(f"📦 Delivering to: {address}")
    else:
        st.warning("Click on the map to select your location.")
    st.markdown("</div>", unsafe_allow_html=True)

# --- ORDER BUTTON ---
if st.button("🍯 Brew My Chai!"):
    st.balloons()
    st.success("🎉 Your chai is brewing! It’ll reach your doorstep soon. ☕")

# --- FOOTER ---
st.markdown("<p class='credits'>Crafted with ❤️ by Shubhranshu Jha & Parikshitsinh Jadeja</p>", unsafe_allow_html=True)
