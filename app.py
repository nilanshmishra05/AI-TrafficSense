import streamlit as st
import pickle
from PIL import Image
import requests
response = requests.get("http://localhost:5000/current_count")
count = response.json()['count']

# Load model
with open("traffic_model.pkl", "rb") as f:
    model = pickle.load(f)

# Page setup
st.set_page_config(page_title="AI-TrafficSense", page_icon="🚦", layout="wide")

# Custom Title
st.markdown("<h1 style='text-align: center; color: #36fba1;'>🚦 AI-TrafficSense</h1>", unsafe_allow_html=True)
st.markdown("---")

# Dashboard layout
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📊 Live Traffic Simulation")
    car_count = st.slider("Select number of vehicles on the road:", 0, 120, 30)
    
    prediction = model.predict([[car_count]])[0]
    status_map = {0: "Clear", 1: "Busy", 2: "Traffic Jam"}
    result = status_map[prediction]

    if result == "Clear":
        st.success("✅ Road is Clear. Vehicles can move freely.")
    elif result == "Busy":
        st.warning("⚠️ Road is getting busy. Moderate traffic detected.")
    else:
        st.error("🚨 Traffic Jam! Congestion is high.")

    st.markdown(f"### 🔍 Prediction Result: **{result}**")
    
    st.markdown("##### 📌 Traffic Condition Based on Vehicle Count:")
    st.markdown("""
    - 0–30 vehicles → **Clear**
    - 31–60 vehicles → **Busy**
    - 61+ vehicles → **Traffic Jam**
    """)

with col2:
    st.subheader("📈 Traffic Insights")

    st.metric(label="🚗 Vehicle Count", value=car_count)
    if result == "Clear":
        st.metric(label="⏱️ Avg Wait Time", value="0 - 1 min", delta="-2 min")
        st.metric(label="🌍 Pollution Level", value="Low")
    elif result == "Busy":
        st.metric(label="⏱️ Avg Wait Time", value="3 - 5 min", delta="+1 min")
        st.metric(label="🌍 Pollution Level", value="Moderate")
    else:
        st.metric(label="⏱️ Avg Wait Time", value="8+ min", delta="+5 min")
        st.metric(label="🌍 Pollution Level", value="High")

    st.markdown("---")
    st.info("Real-time predictions help in adjusting signal timers dynamically.")

# Optional Footer Section
st.markdown("---")
st.markdown("#### 🤖 How It Works")
'''st.markdown("""
This system uses a **machine learning model** trained on traffic data. You adjust the number of vehicles,
and it predicts traffic conditions. These predictions can help smart cities:
- Dynamically change signal timings
- Reduce fuel wastage and emissions
- Improve overall traffic flow
""")'''
